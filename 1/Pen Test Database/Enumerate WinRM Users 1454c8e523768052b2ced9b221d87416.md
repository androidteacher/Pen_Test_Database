# Enumerate WinRM Users

OS: Active_Directory, Windows
Description: Enumerate WinRM Users
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21), PowerView (https://www.notion.so/PowerView-1454c8e523768011a934c27c986b7ef4?pvs=21)

### Enumerate WinRM

```jsx
 Get-NetLocalGroupMember -ComputerName SOC1-101 -GroupName "Remote Management Users"
```
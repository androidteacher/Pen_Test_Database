# Add user to group using credential object for authentication

OS: Active_Directory
Description: Add user to group using credential object for authentication
Security Domains: Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
Target_Technology: PowerView (https://www.notion.so/PowerView-1454c8e523768011a934c27c986b7ef4?pvs=21), PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### Add User to Group (After Creating $cred2 credential Object)

```jsx
Add-DomainGroupMember -Identity 'Help Desk Level 1' -Members 'damundsen' -Credential $Cred2 -Verbose
```
# PowerView: Get-DomainUser Syntax

OS: Active_Directory
Description: Powerview: Get-DomainUser
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: PowerView (https://www.notion.so/PowerView-1454c8e523768011a934c27c986b7ef4?pvs=21)

```jsx
Get-DomainUser -Identity mmorgan -Domain inlanefreight.local | Select-Object -Property name,samaccountname,description,memberof,whencreated,pwdlastset,lastlogontimestamp,accountexpires,admincount,userprincipalname,serviceprincipalname,useraccountcontrol
```
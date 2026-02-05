# Check for Reversible Encryption

OS: Windows
Description: Check for Reversible Encryption
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21), Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21), PowerView (https://www.notion.so/PowerView-1454c8e523768011a934c27c986b7ef4?pvs=21)

### Check for accounts with reversible encryption set

```jsx
Get-ADUser -Filter 'userAccountControl -band 128' -Properties userAccountControl
```

```jsx
Get-DomainUser -Identity * | ? {$_.useraccountcontrol -like '*ENCRYPTED_TEXT_PWD_ALLOWED*'} |select samaccountname,useraccountcontrol
```
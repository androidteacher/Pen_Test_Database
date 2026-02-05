# PowerShell Active Directory Module

OS: Active_Directory, Windows
Description: Active Directory PowerShell Module
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### Install RSAT to get access to this module if not on a domain controller.

### PowerShell Active Directory

```jsx
import-module activedirectory
get-module
```

```jsx
Get-ADDomain
Get-ADGroup -Filter * | select name
Get-ADGroup -Identity "Backup Operators"
Get-ADGroupMember -Identity "Backup Operators"
```
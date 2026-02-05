# dsquery: find all domain controllers

OS: Active_Directory, Windows
Description: Enumerate all domain controllers
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
dsquery * -filter "(userAccountControl:1.2.840.113556.1.4.803:=8192)" -limit 5 -attr sAMAccountName
```
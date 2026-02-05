# Search for files that contain the string ‘password’.

OS: Windows
Description: Search for files containing strings
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
findstr /SIM /C:"password" *.txt *ini *.cfg *.config *.xml
```
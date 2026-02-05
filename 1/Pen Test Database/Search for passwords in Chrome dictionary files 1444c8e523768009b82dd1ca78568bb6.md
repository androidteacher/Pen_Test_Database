# Search for passwords in Chrome dictionary files

OS: Windows
Description: Search for passwords in Chrome dictionary files
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21), chrome (https://www.notion.so/chrome-1444c8e523768047a9f6d659e705cadf?pvs=21)

```jsx
gc 'C:\Users\student\AppData\Local\Google\Chrome\User Data\Default\Custom Dictionary.txt' | Select-String password
```
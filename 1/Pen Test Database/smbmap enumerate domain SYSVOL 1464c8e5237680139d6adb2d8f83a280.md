# smbmap enumerate domain SYSVOL

OS: Active_Directory, Windows
Description: smbmap enumerate domain SYSVOL
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
smbmap -u Your_User -p Your_PASSWORD -d TargetDomain.LOCAL -H 172.16.5.5 -R SYSVOL --dir-only
```
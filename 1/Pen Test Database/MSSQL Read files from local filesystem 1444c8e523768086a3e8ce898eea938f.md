# MSSQL Read files from local filesystem.

OS: Windows
Description: MSSQL Read local Files
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: mssql (https://www.notion.so/mssql-1444c8e5237680f9abcfdf35bc047c00?pvs=21)

### MySQL Read Local Files

```jsx
select LOAD_FILE("/etc/passwd");
```
# crackmapexec spiderplus

OS: Windows
Description: 
Spider an SMB share and create a list of all files.
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21), smb (https://www.notion.so/smb-1434c8e5237680e7b5c3ffe1f7ead9e1?pvs=21)

```jsx
crackmapexec smb 172.16.5.5 -u Target_User-p Target_Password -M spider_plus --share 'Department Shares'
```
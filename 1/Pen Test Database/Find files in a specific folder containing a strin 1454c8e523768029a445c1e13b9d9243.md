# Find files in a specific folder containing  a string

OS: Windows
Description: Find files in a specific folder containing  a string
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
select-string -Path C:\Users\htb-student\Documents\*.txt -Pattern password
```
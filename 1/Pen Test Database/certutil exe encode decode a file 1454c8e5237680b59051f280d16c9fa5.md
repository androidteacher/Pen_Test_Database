# certutil.exe encode/decode a file

OS: Windows
Description: certutil encode/decode a file
Security Domains: Defense Evasion (https://www.notion.so/Defense-Evasion-1444c8e5237680b0b1e4e1911aa265ff?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
certutil -encode file1 encodedfile
```

```jsx
certutil -decode encodedfile file2
```
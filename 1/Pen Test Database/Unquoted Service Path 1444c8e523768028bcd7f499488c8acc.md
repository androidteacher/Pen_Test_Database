# Unquoted Service Path

OS: Windows
Description: Check for unquoted service path
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """
```

### Unquoted Service Path

- Example

```jsx
sc qc SystemExplorerHelpService
```

- Would show:

```jsx
C:\Program Files (x86)\System Explorer\service\SystemExplorerService64.exe
```

- We could use

```jsx
C:\Program.exe\
C:\Program Files (x86)\System.exe
```
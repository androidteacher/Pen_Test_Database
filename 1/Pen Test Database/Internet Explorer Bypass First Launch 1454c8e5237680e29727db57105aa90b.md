# Internet Explorer: Bypass First Launch

OS: Windows
Description: Bypass Internet Explorer First Launch
Security Domains: Execution (https://www.notion.so/Execution-1444c8e52376808b8c78d6d58e52f8a7?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Internet Explorer\Main" -Name "DisableFirstRunCustomize" -Value 2
```
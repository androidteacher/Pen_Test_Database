# Delete Remote Registry Key

OS: Windows
Description: Delete Remote Registry Value
Security Domains: Defense Evasion (https://www.notion.so/Defense-Evasion-1444c8e5237680b0b1e4e1911aa265ff?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
reg delete \\10.129.43.9\HKLM\SYSTEM\CurrentControlSet\Services\DNS\Parameters /v ServerLevelPluginDll
```
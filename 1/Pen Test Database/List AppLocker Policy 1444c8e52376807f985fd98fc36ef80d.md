# List AppLocker Policy

OS: Windows
Description: List AppLocker Policies
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21), Defense Evasion (https://www.notion.so/Defense-Evasion-1444c8e5237680b0b1e4e1911aa265ff?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections
```
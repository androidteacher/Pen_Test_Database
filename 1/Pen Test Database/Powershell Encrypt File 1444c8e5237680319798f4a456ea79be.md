# Powershell Encrypt File

OS: Windows
Description: Encrypt Data
Security Domains: Defense Evasion (https://www.notion.so/Defense-Evasion-1444c8e5237680b0b1e4e1911aa265ff?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### Powershell Encrypt File

- Download Invoke-AESEncryption here:
    - [https://www.powershellgallery.com/packages/DRTools/4.0.2.3/Content/Functions\Invoke-AESEncryption.ps1](https://www.powershellgallery.com/packages/DRTools/4.0.2.3/Content/Functions%5CInvoke-AESEncryption.ps1)

```jsx
Invoke-AESEncryption -Mode Encrypt -Key "p4ssw0rd" -Path .\scan-results.txt
```
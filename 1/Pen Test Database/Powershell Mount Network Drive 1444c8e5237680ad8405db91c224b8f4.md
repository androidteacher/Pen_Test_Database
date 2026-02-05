# Powershell Mount Network Drive

OS: Windows
Description: Mount Network Drive
Security Domains: Initial Access (https://www.notion.so/Initial-Access-1444c8e5237680db9b3afd69d2c38487?pvs=21), Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: smb (https://www.notion.so/smb-1434c8e5237680e7b5c3ffe1f7ead9e1?pvs=21), PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### Powershell mount network drive

```jsx
Interacting with Common Services
PS C:\> $username = 'plaintext'
PS C:\> $password = 'Password123'
PS C:\> $secpassword = ConvertTo-SecureString $password -AsPlainText -Force
PS C:\> $cred = New-Object System.Management.Automation.PSCredential $username, $secpassword
PS C:\> New-PSDrive -Name "N" -Root "\\192.168.220.129\Finance" -PSProvider "FileSystem" -Credential $cred
```
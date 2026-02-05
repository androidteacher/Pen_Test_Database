# Create PSCredential Object

OS: Active_Directory
Description: Create PSCredential Object
Security Domains: Resource Development (https://www.notion.so/Resource-Development-1444c8e523768023b086cae715467df4?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### Create PSCredential Object

```jsx
$SecPassword = ConvertTo-SecureString '<PASSWORD HERE>' -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential('INLANEFREIGHT\wley', $SecPassword) 
```
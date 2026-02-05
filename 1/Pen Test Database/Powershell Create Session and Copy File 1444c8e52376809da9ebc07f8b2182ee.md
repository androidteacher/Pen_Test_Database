# Powershell Create Session and Copy File

OS: Windows
Description: Powershell: Create session and transfer file
Security Domains: File Transfer (https://www.notion.so/File-Transfer-1444c8e52376809ba2ecfc98dc62c772?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### Create a Session

```jsx
# Create a new PSSession to a remote computer
$session = New-PSSession -ComputerName "RemoteComputerName" -Credential (Get-Credential)

# Verify the session variable contains the session information
$session

```

```jsx
Copy-Item -Path C:\samplefile.txt -ToSession $Session -Destination C:\Users\Administrator\Desktop
```
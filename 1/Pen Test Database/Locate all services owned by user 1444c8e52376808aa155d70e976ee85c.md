# Locate all services owned by user

OS: Windows
Description: Query all services to find user ACL entries
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### Locate all Services owned by ServerOperators

```jsx
# Define the output file path
$outputFilePath = "services.txt"

# Ensure the output file is empty or create it if it does not exist
if (Test-Path $outputFilePath) {
    Clear-Content $outputFilePath
} else {
    New-Item $outputFilePath -ItemType File
}

# Get all services running as SYSTEM
$systemServices = Get-WmiObject Win32_Service | Where-Object {$_.StartName -eq "LocalSystem"}

# Iterate over each service to check permissions
foreach ($service in $systemServices) {
    try {
        $serviceName = $service.Name
        
        # Get the security descriptor of the service
        $sd = Get-Acl "HKLM:\System\CurrentControlSet\Services\$serviceName"
        
        # Check if 'Server Operators' have any permissions
        $hasPermissions = $false
        foreach ($ace in $sd.Access) {
            if ($ace.IdentityReference -eq "BUILTIN\Server Operators") {
                $hasPermissions = $true
                break
            }
        }
        
        if ($hasPermissions) {
            # Output services where 'Server Operators' have any permissions to the file
            Add-Content $outputFilePath $serviceName
        }
    }
    catch {
        # Handle errors (e.g., permissions issues)
        Write-Warning "Could not check permissions for service: $serviceName"
    }
}

```
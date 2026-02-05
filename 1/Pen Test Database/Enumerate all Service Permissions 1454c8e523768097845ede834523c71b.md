# Enumerate all Service Permissions

OS: Windows
Description: Enumerate all Service Permissions and output to file
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
# Path to services.txt
$servicesFile = "services.txt"

# Path to PsService.exe (Update this path if PsService.exe is located in a different directory)
$psServicePath = "C:\Path\To\PsService.exe"

# Read each line from services.txt, each line contains a service name
$serviceNames = Get-Content $servicesFile

# Iterate over each service name and run PsService.exe security for it
foreach ($serviceName in $serviceNames) {
    # Construct the command to execute
    $command = "& `"$psServicePath`" security $serviceName"

    # Execute the command
    Write-Host "Executing: $command"
    Invoke-Expression $command

    # Optional: Capture the output to a file
    # $output = Invoke-Expression $command
    # $outputFile = "security_output_$serviceName.txt"
    # $output | Out-File $outputFile
    # Write-Host "Output saved to $outputFile"
}

```
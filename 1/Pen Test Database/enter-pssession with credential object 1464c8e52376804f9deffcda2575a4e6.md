# enter-pssession with credential object

OS: Active_Directory, Windows
Description: WinRM Service Access
Security Domains: Initial Access (https://www.notion.so/Initial-Access-1444c8e5237680db9b3afd69d2c38487?pvs=21), Lateral Movement (https://www.notion.so/Lateral-Movement-1444c8e5237680dea1fed00199ad754d?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

| `$password = ConvertTo-SecureString "Klmcargo2" -AsPlainText -Force` | Creates a variable (`$password`) set equal to the password (`Klmcargo2`) of a user from a Windows-based host. |
| --- | --- |
| `$cred = new-object System.Management.Automation.PSCredential ("INLANEFREIGHT\forend", $password)` | Creates a variable (`$cred`) set equal to the username (`forend`) and password (`$password`) of a target domain account from a Windows-based host. |
| `Enter-PSSession -ComputerName ACADEMY-EA-DB01 -Credential $cred` | Uses the PowerShell cmd-let `Enter-PSSession` to establish a PowerShell session with a target over the network (`-ComputerName ACADEMY-EA-DB01`) from a Windows-based host. Authenticates using credentials made in the 2 commands shown prior (`$cred` & `$password`). |
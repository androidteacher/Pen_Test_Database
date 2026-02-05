# Convert String to Base64 Example

OS: Windows
Description: Encode to Base64
Security Domains: Command Injection (https://www.notion.so/Command-Injection-1434c8e52376803c8c3edfbca59dcd49?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
[Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes('whoami'))
```
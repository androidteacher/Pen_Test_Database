# Linux: List keytab files and impersonate user (Kerberos)

OS: Linux
Description: Linux: List keytab files and impersonate user (Kerberos)
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21), Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21), Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

### List keytab information

```jsx
klist -k -t 
```

### Impersonating a user with keytab files

```jsx
**kinit carlos@TargetDomain.local -k -t /opt/specialfiles/carlos.keytab**

```

### smbclient -k flag

```jsx
smbclient //dc01/carlos -k -c ls
```
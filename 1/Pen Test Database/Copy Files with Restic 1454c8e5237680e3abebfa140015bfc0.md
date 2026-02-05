# Copy Files with Restic

OS: Windows
Description: Restic Backups
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21), Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: windows (https://www.notion.so/windows-1454c8e52376809bb701cef01e9f111a?pvs=21), PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### restic

- Initial repo

```jsx
 mkdir E:\restic2; restic.exe -r E:\restic2 init
```

- backup data

```jsx
$env:RESTIC_PASSWORD = 'Password'
restic.exe -r E:\restic2\ backup C:\SampleFolder
```

- backup data actively in use

```jsx
restic.exe -r E:\restic2\ backup C:\Windows\System32\config --use-fs-snapshot
```

- verify restic snapshots

```jsx
restic.exe -r E:\restic2\ snapshots
```

- based on ID obtained previously, restore to a folder for reading

```jsx
restic.exe -r E:\restic2\ restore 9971e881 --target C:\Restore
```
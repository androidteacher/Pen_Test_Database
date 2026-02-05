# Read/Interpret SDDL from the Event Log

OS: Active_Directory, Windows
Description: Read/Interpret SDDL from the Event Log
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21), PowerView (https://www.notion.so/PowerView-1454c8e523768011a934c27c986b7ef4?pvs=21)

### Reading an SDDL from the event log

```jsx
ConvertFrom-SddlString "SNIP"
<SEE BELOW>
```

- Filter on Discretionary ACL Portion

```jsx
ConvertFrom-SddlString "SNIP" | select -ExpandProperty DiscretionaryAcl
```

![Untitled](Read%20Interpret%20SDDL%20from%20the%20Event%20Log/Untitled.png)
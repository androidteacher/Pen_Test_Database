# wmi enumeration reference

OS: Windows
Description: wmi enumeration reference
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx

```

```jsx

```

### **Quick WMI checks: WMI enum**

| **Command** | **Description** |
| --- | --- |
| `wmic qfe get Caption,Description,HotFixID,InstalledOn` | Prints the patch level and description of the Hotfixes applied |
| `wmic computersystem get Name,Domain,Manufacturer,Model,Username,Roles /format:List` | Displays basic host information to include any attributes within the list |
| `wmic process list /format:list` | A listing of all processes on host |
| `wmic ntdomain list /format:list` | Displays information about the Domain and Domain Controllers |
| `wmic useraccount list /format:list` | Displays information about all local accounts and any domain accounts that have logged into the device |
| `wmic group list /format:list` | Information about all local groups |
| `wmic sysaccount list /format:list` | Dumps information about any system accounts that are being used as service accounts. |
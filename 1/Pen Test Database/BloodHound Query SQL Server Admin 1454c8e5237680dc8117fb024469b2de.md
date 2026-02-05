# BloodHound Query: SQL Server Admin

OS: Active_Directory, Windows
Description: BloodHound Query: SQL Server Admin
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21), bloodhound (https://www.notion.so/bloodhound-1474c8e52376807c8400efeed991bc37?pvs=21)

### SQL Server Admin

- bloodhound query

```jsx
MATCH p1=shortestPath((u1:User)-[r1:MemberOf*1..]->(g1:Group)) MATCH p2=(u1)-[:SQLAdmin*1..]->(c:Computer) RETURN p2
```
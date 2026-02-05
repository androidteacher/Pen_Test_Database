# BloodHound Query: WinRM Users

OS: Active_Directory, Windows
Description: BloodHound Query: WinRM Users
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21), bloodhound (https://www.notion.so/bloodhound-1474c8e52376807c8400efeed991bc37?pvs=21)

- Bloodhound raw query

```jsx
MATCH p1=shortestPath((u1:User)-[r1:MemberOf*1..]->(g1:Group)) MATCH p2=(u1)-[:CanPSRemote*1..]->(c:Computer) RETURN p2
```
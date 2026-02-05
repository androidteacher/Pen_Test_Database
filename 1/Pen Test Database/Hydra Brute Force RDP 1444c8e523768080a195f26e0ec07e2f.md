# Hydra Brute Force RDP

OS: Linux
Description: Brute Force RDP
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: rdp (https://www.notion.so/rdp-1444c8e52376801fbd7defc74098df00?pvs=21)

```jsx
hydra -L usernames.txt -p 'password123' <FQDN/IP> rdp
```
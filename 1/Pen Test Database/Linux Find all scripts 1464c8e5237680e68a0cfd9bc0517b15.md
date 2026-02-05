# Linux: Find all scripts

OS: Linux
Description: Linux: Find all scripts
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
find / -type f -name "*.sh" 2>/dev/null | grep -v "src\|snap\|share"
```
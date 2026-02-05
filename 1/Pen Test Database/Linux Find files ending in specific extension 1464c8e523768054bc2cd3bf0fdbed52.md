# Linux: Find files ending in specific extension

OS: Linux
Description: Linux find files ending in a specific extension
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
find /home/* -type f -name "*.txt" -o ! -name "*.*"
```
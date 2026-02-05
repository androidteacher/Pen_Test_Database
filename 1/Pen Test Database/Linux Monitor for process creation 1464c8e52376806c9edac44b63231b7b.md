# Linux: Monitor for process creation

OS: Linux
Description: Linux: Monitor for process creation
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

### Snoop on Linux Processes (psspy)

```jsx
https://github.com/DominicBreuker/pspy
```

- Check every 1000 ms

```jsx
./pspy64 -pf -i 1000
```
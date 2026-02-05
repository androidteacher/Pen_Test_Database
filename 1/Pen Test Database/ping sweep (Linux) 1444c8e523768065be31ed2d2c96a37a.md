# ping sweep (Linux)

OS: Linux
Description: Bash for loop to implement ping sweep.
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
for i in {1..254} ;do (ping -c 1 172.16.5.$i | grep "bytes from" &) ;done
```
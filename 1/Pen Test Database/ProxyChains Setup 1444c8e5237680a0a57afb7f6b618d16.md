# ProxyChains Setup

OS: Linux
Description: Proxy chains setup and usage
Security Domains: Lateral Movement (https://www.notion.so/Lateral-Movement-1444c8e5237680dea1fed00199ad754d?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

- Modify Proxychains

```jsx
tail -4 /etc/proxychains.conf
```

File should contain the destination of

```jsx
socks4 	127.0.0.1 9050
```

### Use Proxychains in conjunction with other commands

```jsx
proxychains nmap -v -sn 172.16.5.1-200
```

### Use Case:

- Set up a SOCKS proxy using SSH

```jsx
ssh -D 10.10.10.10 9050
```

- Configure proxychains to use this socks proxy

```jsx
socks5 	10.10.10.10 9050
```

- run telnet through proxychains to a protected subnet

```jsx
proxychains telnet 172.25.5.5 80
```
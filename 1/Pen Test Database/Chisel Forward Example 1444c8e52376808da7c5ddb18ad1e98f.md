# Chisel Forward Example

OS: Linux
Description: Chisel Client/Server pivot example
Security Domains: Lateral Movement (https://www.notion.so/Lateral-Movement-1444c8e5237680dea1fed00199ad754d?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

| `./chisel server -v -p 1234 --socks5` | Used to start a chisel server in verbose mode listening on port `1234` using SOCKS version 5. |
| --- | --- |
| `./chisel client -v 10.129.202.64:1234 socks` | Used to connect to a chisel server at the specified IP address & port using socks. |
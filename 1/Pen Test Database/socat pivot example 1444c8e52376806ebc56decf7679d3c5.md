# socat pivot example

OS: Linux
Description: Uses Socat to listen on port 8080 and then to fork when the connection is received. It will then connect(pivot) to the attack host on port 80.
Security Domains: Lateral Movement (https://www.notion.so/Lateral-Movement-1444c8e5237680dea1fed00199ad754d?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
socat TCP4-LISTEN:8080,fork TCP4:<IPaddressofVictim>:80
```
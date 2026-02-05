# openssl query domain

OS: Linux, Web
Description: openssl query domain
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
export TARGET="facebook.com"
export PORT="443"
openssl s_client -ign_eof -connect "${TARGET}:${PORT}" <<< $'HEAD / HTTP/1.0\r\n\r' > cert.pem
openssl x509 -noout -text -in cert.pem | grep 'DNS' | sed -e 's|DNS:|\n|g' -e 's|^\*.*||g' | tr -d ',' | sort -u
```
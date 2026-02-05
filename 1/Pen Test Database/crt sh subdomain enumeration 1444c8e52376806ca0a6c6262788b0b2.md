# crt.sh subdomain enumeration

OS: Linux
Description: Subdomain enumeration via crt.sh
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: dns (https://www.notion.so/dns-1444c8e52376808aa820e13096bf807f?pvs=21)

```jsx
curl -s https://crt.sh/\?q\=paypal.com\&output\=json | jq . | grep name | cut -d":" -f2 | grep -v "CN=" | cut -d'"' -f2 | awk '{gsub(/\\n/,"\n");}1;' | sort -u
```
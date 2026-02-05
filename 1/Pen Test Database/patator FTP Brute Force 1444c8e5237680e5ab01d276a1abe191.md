# patator FTP Brute Force

OS: Linux
Description: FTP Brute Force
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: ftp (https://www.notion.so/ftp-1434c8e5237680bcaf18c24e9f10cb87?pvs=21)
URL: https://github.com/lanjelot/patator

```jsx
patator ftp_login user=FILE1 password=FILE0 0=passwords.list 1=users.list host=10.129.5.99 port=2121 -x ignore:mesg='Login incorrect.'

```
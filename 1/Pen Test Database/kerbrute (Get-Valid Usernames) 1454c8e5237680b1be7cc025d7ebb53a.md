# kerbrute (Get-Valid Usernames)

OS: Active_Directory, Linux, Windows
Description: Setup and run kerbrute
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

### Kerbrute

```jsx
https://github.com/ropnop/kerbrute
```

```jsx
git clone https://github.com/ropnop/kerbrute.git
make all
cd dist/
./kerbrute_linux_amd64 
mv kerbrute_linux_amd64 /usr/local/bin/kerbrute
kerbrute userenum -d Target_Domain --dc 172.16.5.5 jsmith.txt -o valid_ad_users
```
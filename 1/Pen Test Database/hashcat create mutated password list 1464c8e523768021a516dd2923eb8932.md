# hashcat create mutated password list

OS: Linux
Description: Hashcat create mutated password list with rule
Security Domains: Resource Development (https://www.notion.so/Resource-Development-1444c8e523768023b086cae715467df4?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21), hashcat (https://www.notion.so/hashcat-1464c8e5237680c5b2dac6c57ec0e76f?pvs=21)

```jsx
hashcat --force password.list -r custom.rule --stdout > mut_password.list
```
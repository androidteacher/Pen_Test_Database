# list of Linux for loops to find senstive info:

OS: Linux
Description: List of useful for loops: Linux
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

| **Command** | **Description** |
| --- | --- |
| `for l in $(echo ".conf .config .cnf");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "lib|fonts|share|core" ;done` | Script that can be used to find .conf, .config and .cnf files on a Linux system. |
| `for i in $(find / -name *.cnf 2>/dev/null | grep -v "doc|lib");do echo -e "\nFile: " $i; grep "user|password|pass" $i 2>/dev/null | grep -v "\#";done` | Script that can be used to find credentials in specified file types. |
| `for l in $(echo ".sql .db .*db .db*");do echo -e "\nDB File extension: " $l; find / -name *$l 2>/dev/null | grep -v "doc|lib|headers|share|man";done` | Script that can be used to find common database files. |
| `find /home/* -type f -name "*.txt" -o ! -name "*.*"` | Uses Linux-based find command to search for text files. |
| `for l in $(echo ".py .pyc .pl .go .jar .c .sh");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "doc|lib|headers|share";done` | Script that can be used to search for common file types used with scripts. |
| `for ext in $(echo ".xls .xls* .xltx .csv .od* .doc .doc* .pdf .pot .pot* .pp*");do echo -e "\nFile extension: " $ext; find / -name *$ext 2>/dev/null | grep -v "lib|fonts|share|core" ;done` | Script used to look for common types of documents. |
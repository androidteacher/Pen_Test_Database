# Gau: Pull all unique subdomains and sort all endpoints found for those that are alive, run nuclei automated scan on unique, alive targets.

OS: Linux
Description: Gau: Pull all unique subdomains and sort all endpoints found for those that are alive, run nuclei automated scan on unique, alive targets.
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21), gau (https://www.notion.so/gau-1474c8e52376806eabd3f2c494a0ac00?pvs=21)

```php
subfinder -d domain.com | tee subs.txt
httpx -l subs.txt | alive.txt
cat alive.txt | gau --subs --blacklist png,jpg,gif,jpeg,swf,woff,gif,svg --o 01_output_gau.txt
cat 01_output_gau.txt | unfurl format %d | sort -u | tee -a gau_subdomains.txt
httpx -l gau_subdomains.txt | tee -a gau_alive.txt
for i in $(cat gau_alive.txt); do cat 01_output_gau.txt | grep $i | sort -u | tee -a endpoints_alive_final.txt;done
```

### Use qsreplace to eliminate duplicate parameters

```php
cat endpoints_alive_final.txt | qsreplace PARAM123 | sort -u | tee -a Unique_Parameters_final.txt
```

### Perform nuclei automated scan on all targets

```php
 nuclei -l Unique_Parameters_final.txt -as -o nuclei.log
```
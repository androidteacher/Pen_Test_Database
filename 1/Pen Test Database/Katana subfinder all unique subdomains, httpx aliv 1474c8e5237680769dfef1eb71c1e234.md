# Katana: subfinder all unique subdomains, httpx alive, katana crawl, unfurl domains, httpx alive, create list of all endpoints from alive subdomains

OS: Linux
Description: Katana: subfinder all unique subdomains, httpx alive, katana crawl, unfurl domains, httpx alive, create list of all endpoints from alive subdomains
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: katana (https://www.notion.so/katana-1474c8e52376802f9961cf562b9606f9?pvs=21)

```php
subfinder -d domain.com | tee -a subs.txt
httpx -l subs.txt | alive.txt
katana -list alive.txt | tee -a katana_list.txt
cat katana_list.txt | unfurl format %d | sort -u | tee -a unfurled_domains.txt
httpx -l unfurled_domains.txt | tee -a unfurled_alive.txt
for i in $(cat unfurled_alive.txt); do cat katana_list.txt | grep $i | sort -u | tee -a katana_final.txt; done

```

### Use qsreplace to eliminate duplicate parameters

```php
cat katana_final.txt | qsreplace PARAM123 | sort -u | tee -a Unique_Parameters_final.txt
```

### Perform nuclei automated scan on all targets

```php
 nuclei -l Unique_Parameters_final.txt -as -o nuclei.log

```
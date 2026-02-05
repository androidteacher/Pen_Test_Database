# Gau: Read from the list of target domains, find subdomains, HTTPX, gau, nuclei -as Note: —Walk away for 2 days. (This script works in order.)

OS: Linux
Description: Gau: Long term automated scan.
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: gau (https://www.notion.so/gau-1474c8e5237680c0a5e5f65a215b125e?pvs=21), PowerShell (https://www.notion.so/PowerShell-1434c8e52376805dba60efbabdb026bf?pvs=21), nuclei (https://www.notion.so/nuclei-1474c8e5237680ea945ecb752fccd88c?pvs=21)
URL: https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/refs/heads/main/data/wildcards.txt

```php
#!/bin/bash

# Create directories for outputs
mkdir -p endpoints gau_output unique final_results

# Wordlist file
WORDLIST="wordlist_example.txt"

# Read each line (subdomain) from the wordlist
while IFS= read -r subdomain; do
    echo "Processing $subdomain..."

    # Subfinder: Find subdomains
    subfinder -d "$subdomain" | tee subs.txt

    # Httpx: Determine which subdomains are alive
    httpx -l subs.txt | tee alive.txt

    # Gau: Enumerate endpoints and known URLs
    gau --subs --blacklist png,jpg,gif,jpeg,swf,woff,gif,svg --o "gau_output/${subdomain}_01_output_gau.txt" < alive.txt

    # Extract subdomains using Unfurl
    unfurl format %d < "gau_output/${subdomain}_01_output_gau.txt" | sort -u | tee "endpoints/${subdomain}_gau_subdomains.txt"

    # Httpx: Determine which endpoints from gau are alive
    httpx -l "endpoints/${subdomain}_gau_subdomains.txt" | tee "endpoints/${subdomain}_gau_alive.txt"

    # Match alive endpoints with gau output
    > "endpoints/${subdomain}_endpoints_alive_final.txt"
    while IFS= read -r endpoint; do
        grep "$endpoint" "gau_output/${subdomain}_01_output_gau.txt" | sort -u >> "endpoints/${subdomain}_endpoints_alive_fin>
    done < "endpoints/${subdomain}_gau_alive.txt"

    # Replace query parameters with a fixed value and filter unique URLs
    qsreplace PARAM123 < "endpoints/${subdomain}_endpoints_alive_final.txt" | sort -u | tee "unique/${subdomain}_Unique_Param>

    # Run Nuclei with autodetection and output results to a subdomain-specific log file
    nuclei -l "unique/${subdomain}_Unique_Parameters_final.txt" -as -o "final_results/${subdomain}-scanned.nuclei.log"

    echo "Scan completed for $subdomain. Output: final_results/${subdomain}-scanned.nuclei.log"
done < "$WORDLIST"

echo "Processing completed for all subdomains in the wordlist."

```

### Example wordlist_example.txt:

```php
arlo.com
arloxcld.com
central.arubanetworks.com
asana.biz
app.asana.com
atlastunnel.com
cic-bug-bounty.auth0app.com
tube8.com
trafficjunky.com
adultforce.com
backblazeb2.com
bigcommerce.net
bitdefender.net
bitdefender.com
bugcrowd.com
canva.cn
canva.com
canva.tech
cashstaging.app
```
# subdomain enumeration: sonar.omnisint.io

OS: Linux, Web
Description: subdomain enumeration
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: dns (https://www.notion.so/dns-1444c8e52376808aa820e13096bf807f?pvs=21), Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

| `curl -s https://sonar.omnisint.io/subdomains/{domain} | jq -r '.[]' | sort -u` | All subdomains for a given domain. |
| --- | --- |
| `curl -s https://sonar.omnisint.io/tlds/{domain} | jq -r '.[]' | sort -u` | All TLDs found for a given domain. |
| `curl -s https://sonar.omnisint.io/all/{domain} | jq -r '.[]' | sort -u` | All results across all TLDs for a given domain. |
| `curl -s https://sonar.omnisint.io/reverse/{ip} | jq -r '.[]' | sort -u` | Reverse DNS lookup on IP address. |
| `curl -s https://sonar.omnisint.io/reverse/{ip}/{mask} | jq -r '.[]' | sort -u` | Reverse DNS lookup of a CIDR range. |
# TheHarvestor Usage

OS: Linux, Web
Description: theHarverster OSINT
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

### TheHarverster:

- sources.txt

```jsx
baidu
bufferoverun
crtsh
hackertarget
otx
projectdiscovery
rapiddns
sublist3r
threatcrowd
trello
urlscan
vhost
virustotal
zoomeye
```

```jsx
export TARGET="google.com"
cat sources.txt | while read source; do theHarvester -d "${TARGET}" -b $source -f "${source}_${TARGET}";done
```

- extract subdomains

```jsx
cat *.json | jq -r '.hosts[]' 2>/dev/null | cut -d':' -f 1 | sort -u > "${TARGET}_theHarvester.txt"
```
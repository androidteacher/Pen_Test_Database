# Gau: create domain list and run nuclei to detect potential sub-domain takeover

OS: Linux
Description: Gau: create domain list and run nuclei to detect potential sub-domain takeover
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21), nuclei (https://www.notion.so/nuclei-1474c8e5237680ea945ecb752fccd88c?pvs=21), gau (https://www.notion.so/gau-1474c8e52376806eabd3f2c494a0ac00?pvs=21)

```jsx
httpx -l subs.txt > alive.txt
```

```jsx
cat alive.txt | gau --subs --blacklist png,jpg,gif,jpeg,swf,woff,gif,svg --o 01_output_gau.txt
```

```jsx

nuclei -l 01_output_gau.txt -t detect-all-takeovers.yml

```

OR

```jsx
for i in $(cat alive.txt);
do
httpx -silent -mc 200,301,302,403 | nuclei $i -t detect-all-takeovers.tml -rl 30  | tee output/NUCLEI.$1
```
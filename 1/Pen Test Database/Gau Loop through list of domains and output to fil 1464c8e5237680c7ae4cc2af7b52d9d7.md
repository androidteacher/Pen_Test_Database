# Gau: Loop through list of domains and output to file

OS: Linux
Description: gau for loop
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21), gau (https://www.notion.so/gau-1474c8e52376806eabd3f2c494a0ac00?pvs=21)

```jsx
httpx -l subs.txt > alive.txt
```

```jsx
cat alive.txt | gau --subs --blacklist png,jpg,gif,jpeg,swf,woff,gif,svg --o 01_output_gau.txt
```
# Install GF and GF-Patterns and replace parameters

OS: Linux
Description: install GF and GF-Patterns
Security Domains: Resource Development (https://www.notion.so/Resource-Development-1444c8e523768023b086cae715467df4?pvs=21)

```jsx
go install -v github.com/tomnomnom/gf@latest
```

```jsx
cd ~
mkdir patterns
cd patterns
git clone https://github.com/1ndianl33t/Gf-Patterns
cd Gf-Patterns
```

### Find potential parameters that are potentially susceptible to open redirect.

```jsx
cat starbucks_ca.txt | gf redirect > redirect_list.txt
```
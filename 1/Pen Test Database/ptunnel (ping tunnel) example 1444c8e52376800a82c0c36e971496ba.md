# ptunnel (ping tunnel) example

Description: pivot to internal network with ptunnel
Security Domains: Lateral Movement (https://www.notion.so/Lateral-Movement-1444c8e5237680dea1fed00199ad754d?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
git clone https://github.com/utoni/ptunnel-ng.git

sudo ./autogen.sh 
```

- Copy to pivot box

```jsx
scp -r ptunnel-ng ubuntu@10.129.202.64:~/
```

- Start on pivot box

```jsx
sudo ./ptunnel-ng -r10.129.202.64 -R22
```

- Create a tunnel on the attack box

```jsx
sudo ./ptunnel-ng -p10.129.202.64 -l2222 -r10.129.202.64 -R22
```

- Connect

```jsx
ssh -p2222 -lubuntu 127.0.0.1
```
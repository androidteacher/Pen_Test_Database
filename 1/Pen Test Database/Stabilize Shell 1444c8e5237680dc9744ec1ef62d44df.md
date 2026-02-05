# Stabilize Shell

OS: Linux
Description: Stabilize an already existing Reverse Shell
Security Domains: Execution (https://www.notion.so/Execution-1444c8e52376808b8c78d6d58e52f8a7?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

# Stabilize a Reverse Shell

### At your reverse shell prompt, type:

```jsx
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

### You’ll see that the prompt changes at this point, but we aren’t done yet.

![Untitled](Stabilize%20Shell/Untitled.png)

### Background the shell with CTRL-Z

- By backgrounding a process with CTRL-Z, we are suspending it in the background. We can return to it at the exact same point of execution by typing the **fg** command.

```jsx
CTRL-Z
```

![Untitled](Stabilize%20Shell/Untitled%201.png)

### Once we have backgrounded our reverse shell, we want to activate ‘raw’ mode which will send data after each keypress as opposed to each time we hit enter. (This will allow the shell session to recognize things like the up-arrow and TAB.)

- The  **; fg** will return us to the foreground and we’ll back at the remote shell.
    - If you aren’t sure what the semi-colon is doing in the command below, you should definitely ask ChatGPT!

```jsx
stty raw -echo; fg
```

![Untitled](Stabilize%20Shell/Untitled%202.png)

### Finally, we want to set our terminal emulator to ‘xterm’ with the following command.

```jsx
export TERM=xterm
```

![Untitled](Stabilize%20Shell/Untitled%203.png)
# lxc cheatsheet

OS: Linux
Description: lxc cheat sheet
Security Domains: Resource Development (https://www.notion.so/Resource-Development-1444c8e523768023b086cae715467df4?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

| `lxd init` | Start the LXD initialization process |
| --- | --- |
| `lxc image import alpine.tar.gz alpine.tar.gz.root --alias alpine` | Import a local image |
| `lxc init alpine r00t -c security.privileged=true` | Start a privileged LXD container |
| `lxc config device add r00t mydev disk source=/ path=/mnt/root recursive=true` | Mount the host file system in a container |
| `lxc start r00t` | Start the container |
# tmux cheat sheet

OS: Linux
Description: tmux cheat sheet
Security Domains: Resource Development (https://www.notion.so/Resource-Development-1444c8e523768023b086cae715467df4?pvs=21)
Target_Technology: Bash (https://www.notion.so/Bash-1434c8e5237680b5aa14d2174d201e9a?pvs=21)

| CTRL-B D | Detach |
| --- | --- |
| tmux ls | List sessions |
| tmux a -t <session Identified) | Attach |
| tmux new -s NAME | Create |
| ctrl-b % | Split H |
| ctrl-b “ | Split V |
| ctrl-b q | show pane # |
| ctrl-b q # | jump to pane |
| ctrl-b <hold-ctrl> arrows | resize things |
| ctrl-b c | new window |
| ctrl-b n | move sequentially through windows |
| ctrl-b , | rename window |
| ctrl-b w | bring up sessions and windows list |
| ctrl-b x | kill selected pane |
| ctrl-b & | kill selected window |
| ctrl-b [ | start copy mode |
| CTRL space | start selection |
| enter or CTRL-W | copy selection out |
| ctrl-b ] | paste |
| ctrl-b z | zoom in on pane |
| ctrl-b ! | convert pane to window |
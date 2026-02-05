# PowerView Module/Commands List

OS: Active_Directory, Windows
Description: PowerView Modules List
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)

| `Export-PowerViewCSV` | PowerView script used to append results to a `CSV` file. Performed from a Windows-based host. |
| --- | --- |
| `ConvertTo-SID` | PowerView script used to convert a `User` or `Group` name to it's `SID`. Performed from a Windows-based host. |
| `Get-DomainSPNTicket` | PowerView script used to request the kerberos ticket for a specified service principal name (`SPN`). Performed from a Windows-based host. |
| `Get-Domain` | PowerView script used tol return the AD object for the current (or specified) domain. Performed from a Windows-based host. |
| `Get-DomainController` | PowerView script used to return a list of the target domain controllers for the specified target domain. Performed from a Windows-based host. |
| `Get-DomainUser` | PowerView script used to return all users or specific user objects in AD. Performed from a Windows-based host. |
| `Get-DomainComputer` | PowerView script used to return all computers or specific computer objects in AD. Performed from a Windows-based host. |
| `Get-DomainGroup` | PowerView script used to eturn all groups or specific group objects in AD. Performed from a Windows-based host. |
| `Get-DomainOU` | PowerView script used to search for all or specific OU objects in AD. Performed from a Windows-based host. |
| `Find-InterestingDomainAcl` | PowerView script used to find object `ACLs` in the domain with modification rights set to non-built in objects. Performed from a Windows-based host. |
| `Get-DomainGroupMember` | PowerView script used to return the members of a specific domain group. Performed from a Windows-based host. |
| `Get-DomainFileServer` | PowerView script used to return a list of servers likely functioning as file servers. Performed from a Windows-based host. |
| `Get-DomainDFSShare` | PowerView script used to return a list of all distributed file systems for the current (or specified) domain. Performed from a Windows-based host. |
| `Get-DomainGPO` | PowerView script used to return all GPOs or specific GPO objects in AD. Performed from a Windows-based host. |
| `Get-DomainPolicy` | PowerView script used to return the default domain policy or the domain controller policy for the current domain. Performed from a Windows-based host. |
| `Get-NetLocalGroup` | PowerView script used to enumerate local groups on a local or remote machine. Performed from a Windows-based host. |
| `Get-NetLocalGroupMember` | PowerView script enumerate members of a specific local group. Performed from a Windows-based host. |
| `Get-NetShare` | PowerView script used to return a list of open shares on a local (or a remote) machine. Performed from a Windows-based host. |
| `Get-NetSession` | PowerView script used to return session information for the local (or a remote) machine. Performed from a Windows-based host. |
| `Test-AdminAccess` | PowerView script used to test if the current user has administrative access to the local (or a remote) machine. Performed from a Windows-based host. |
| `Find-DomainUserLocation` | PowerView script used to find machines where specific users are logged into. Performed from a Windows-based host. |
| `Find-DomainShare` | PowerView script used to find reachable shares on domain machines. Performed from a Windows-based host. |
| `Find-InterestingDomainShareFile` | PowerView script that searches for files matching specific criteria on readable shares in the domain. Performed from a Windows-based host. |
| `Find-LocalAdminAccess` | PowerView script used to find machines on the local domain where the current user has local administrator access Performed from a Windows-based host. |
| `Get-DomainTrust` | PowerView script that returns domain trusts for the current domain or a specified domain. Performed from a Windows-based host. |
| `Get-ForestTrust` | PowerView script that returns all forest trusts for the current forest or a specified forest. Performed from a Windows-based host. |
| `Get-DomainForeignUser` | PowerView script that enumerates users who are in groups outside of the user's domain. Performed from a Windows-based host. |
| `Get-DomainForeignGroupMember` | PowerView script that enumerates groups with users outside of the group's domain and returns each foreign member. Performed from a Windows-based host. |
| `Get-DomainTrustMapping` | PowerView script that enumerates all trusts for current domain and any others seen. Performed from a Windows-based host. |
| `Get-DomainGroupMember -Identity "Domain Admins" -Recurse` | PowerView script used to list all the members of a target group (`"Domain Admins"`) through the use of the recurse option (`-Recurse`). Performed from a Windows-based host. |
| `Get-DomainUser -SPN -Properties samaccountname,ServicePrincipalName` | PowerView script used to find users on the target Windows domain that have the `Service Principal Name` set. Performed from a Windows-based host. |
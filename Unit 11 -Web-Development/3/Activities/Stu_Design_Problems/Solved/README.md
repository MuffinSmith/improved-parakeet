# Design Problems

In this exercise, you'll consider the security implications of different server architectures.

## Questions

In the case of a single host running both an HTTP and DB server, an attacker can compromise the entire system by compromising the single host.

Consider the Web Farm (without database cluster).
- Which servers might an attacker target to steal data?
  > **Solution**: An attacker must compromise at least one of the HTTP servers.
- Which servers might an attacker target to DoS the application?
  > **Solution**: An attacker could target any of the devices in the architecture—the load balancer, HTTP servers, or database.

Consider the Web Farm (with database cluster).
- Explain one way a database cluster might be more secure than using a single database.
  > **Solution**: A database administrator can store different data in different databases, So, if an attacker compromises one database server, the data in the other one may still be safe.
- How does the CIA of a Web Farm with database cluster compare to that of a Web Farm without one?
  > **Solution**: The availability of database clusters is always higher. Confidentiality may be improved, depending on how developers distribute data across the databases. Integrity is equivalent in both cases.

Consider the Web Farm with Dedicated Application Servers.
- Which servers would an attacker need to compromise to steal sensitive data?
  > **Solution**: An attacker would need to compromise the Application Servers, which sit behind _two_ firewalls.
- Is the Web Farm with Dedicated Application Servers more or less secure than the Web Farm with Load Balanced Application Servers?
  > **Solution**: They're both equally secure. The only difference between the two architectures is the load balancer in front of the App Servers, which adds no real security benefits.

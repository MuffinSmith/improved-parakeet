# Design Problems

In this exercise, you'll consider the security implications of different server architectures.

## Questions

In the case of a single host running both an HTTP and DB server, an attacker can compromise the entire system by compromising the single host.

Consider the Web Farm (without database cluster).
- Which servers might an attacker target to steal data?
- Which servers might an attacker target to DoS the application?

Consider the Web Farm (with database cluster).
- Explain one way a database cluster might be more secure than using a single database.
  - **Hint**: You can store different data in different places.
- How does the CIA of a Web Farm with database cluster compare to that of a Web Farm without one?

Consider the Web Farm with Dedicated Application Servers.
- Which servers would an attacker need to compromise to steal sensitive data?
- Is the Web Farm with Dedicated Application Servers more or less secure than the Web Farm with Load Balanced Application Servers?

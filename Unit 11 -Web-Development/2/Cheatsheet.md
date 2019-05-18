# Day 2 Cheat Sheet — Exploring Servers

## Key Terms

- **Caching**: a process in which browsers and/or servers save responses to previous requests for later reuse
  > **Example**: to serve requets faster, they are cache for future requests.
  
- **Private Caches**: are meant to serve a single user.
  > **Example**: Your local browser cache is an example of a private cache, since only you can use it.
    
- **Public Caches**: which are typically servers that sit between you and the destination server you’re requesting resources from.
    
- **Cache-Control header**: instruct clients and intermediary servers as to whether they should cache the response it appears in; and if so, how.
  > **Example**: lets servers specify which resources to cache.
    
- **Patching**: a set of changes designed to improve or fix a computer program
  > **Example**: computer systems are patched regular to address vulnerabilitues and reduce risk
    
- **Web Cache Poisoning**: an attack in which a hacker tricks a public proxy server into caching malicious data.
  > **Example**: certain departments are usually targeted with phishing emails
    
- **Authorization**: giving someone or something (process, appliaction, program) persmission to have access to something.
  > **Example**: how do you remember if the current user is logged in?
    
- **Authentication**: process of determining whether someone or something is, in fact, who or what it declares itself to be.
  > **Example**: how do you know that the current user is who they say they are?
    
- **User preferences**: specific settings customized by the user
  > **Example**: how do you remember which time zone the user wants to use?
    
- **Cookies**: pieces of key/value data that clients can send to servers to provide this information
  > **Example**: When browsing websites, cookies are created about your activity
  
- **Sessions**: is data used by a server to remember details about a user.
  > **Example**: session ID's are generated when logging into a membership area on a website.
    
- **Stateful Information**: anything that changes over time
  > **Example**: login status, preferences, etc.
      
- **Sessions ID**: computers that have a specific role or purpose for clients/users
  > **Example**: web servers, database servers, email servers, etc.
      
- **Impersonation**: Stealing and sending a user's cookies and/or session ID, so the web application thinks you're someone else

- **Forgery**: Creating fake cookies and/or session IDs that the application understands and interprets "correctly", but which lead to unintended behavior
  > **Example**: you create a fake session cookie that gives your user account administrator privileges, etc.
      
- **Validation**: preventing users from submitting invalid data
  > **Example**: input validation is used often when submitting forms to ensure valid characters and such are appropriate
      
- **Client-side validation**: preventing the user from sending certain data through a form 
  > **Example**: Gruyere preventing you from trying to register with long usernames
      
- **Server-side validation**:  preventing a server from using invalid data
  > **Example**: if Gruyere simply could not create accounts with long usernames.
      
- **Session Hijacking**: the "fundamental" impersonation attack on session server sessions
  > **Example**: A legitimate user logs into a banking application, and receives a cookie like: SESSID=100, an attacker sends request from his own computer with the cookie: SESSID=100, then the server responds to the attacker as if he were Jane, because he used a cookie containing her session ID.
                              
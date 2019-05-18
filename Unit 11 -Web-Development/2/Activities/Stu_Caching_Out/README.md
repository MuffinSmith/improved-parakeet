# Caching out

## Instructions

### Shared vs Private Caches
- Consider an article page on a site like `https://www.reuters.com`,which serves mostly articles and images. Contrast this with the home page of a site like `https://www.youtube.com`. 
  - Which page is more likely to be served from the browser cache? Why?

- Consider the case of users accessing YouTube on a college campus.
  - How would a private cache speed up a user's experience of the site? Which videos would load faster?
  - How would a shared cache speed up a user's experience of the site? Which videos would load faster?
  - Which kind of cache do you think is more useful for reducing site load times?

### Cache Control
Refer to the documentation at: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control#Syntax>

- What does the `Cache-Control` header do?

- What kinds of information do `Cache-Control` request headers contain?
  - **Hint**: Focus on the first three directives.

- What kinds of information do `Cache-Control` response headers contain?
  - **Hint**: Focus on the first two directives.

- What does this indicate about which features of a response matter most for efficient caching? 

## Expansion

Caching might seem unexciting, but it's crucial for fast user experiences, and has considerable security implications.

One example of a recent attack on web caches is the aptly named Web Cache Deception attack. 

Read about it here: <https://blogs.akamai.com/2017/03/on-web-cache-deception-attacks.html>

- Read the **Attack** section.
  - What do attackers attempt to trigger when executing this attack?
  - Who must initiate the first request—the attacker or the target?
  - What should mitigation efforts focus on?

---

**Notes**: In a Web Cache Deception attack, an attacker tricks a web server into caching private data that should _not_ be stored on a public cache. Then, the attacker can read the private data by reading the public cache!

This demonstrates one of many vulnerabilities that arise from storing data in multiple locations on the network.

# Caching out

## Instructions

### Shared vs Private Caches
- Consider an article page on a site like `https://www.reuters.com`,which serves mostly articles and images. Contrast this with the home page of a site like `https://www.youtube.com`. 
  - Which page is more likely to be served from the browser cache? Why?
    > **Solution**: A page from Reuters is more likely to be served from the browser cache, as it's more static than a page from a site like YouTube.

- Consider the case of users accessing YouTube on a college campus.
  - How would a private cache speed up a user's experience of the site? Which videos would load faster?
    > **Solution**: A private cache would result in faster load times for videos the user rewatches frequently.
  - How would a shared cache speed up a user's experience of the site? Which videos would load faster?
    > **Solution**: A shared cache would result in faster load times for the most popular videos university-wide.
  - Which kind of cache do you think is more useful for reducing site load times?
    > **Solution**: In this scenario, a shared cache has a greater effect on each individual's average load times than a private cache would, except for users who only watch the same videos repeatedly.

### Cache Control
Refer to the documentation at: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control#Syntax>

- What does the `Cache-Control` header do?
    > **Solution**
    >   - The `Cache-Control` request header allows a client to request cache-related behavior from the origin server and/or intermediary proxies. For example, a request header of `Cache-Control: must-revalidate` asks the caches to revalidate the resource in the request line before loading it from the cache.
    >   - The `Cache-Control` response header allows a server to instruct a client as to whether to cache a resource; for how long; when to revalidate and/or force reload it; etc.

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

# Web Cache Poisoning

## Instructions

Caching might seem unexciting, but it's crucial for fast user experiences, and has considerable security implications.

**Cache Poisoning** is an important attack through which an attacker tricks a cache into caching a malicious file, _instead_ of the file the cache should serve.

In this exercise, you'll read about cache poisoning attacks, and how they're used. Refer to this write-up: <https://portswigger.net/blog/practical-web-cache-poisoning>

Use the questions below to guide your reading.

## Questions

- Read the introduction and **Caching 101** sections.

- Read the **Cache Keys** section, and answer the following questions:
  - What must a cahce do when it receives a request for a resource? Why is this tricky?
    > **Solution**: It must decide whether it has this resource in the cache, or if it should forward the request to the application server.
  - Caches use _____ _____ to address this problem.
    > **Solution**: Cache Keys. These are pieces of data from a request used to "fingerprint" it, which the cache uses to determine if it's seen the response to a given request before.

- Read the **Cache Poisoning Section**, and answer the questions below.
  - What is the objective of a cache poisoning attack?
    > **Solution**: "The objective of a web cache poisoning attack is to send a request that causes a harmful response that gets saved in the cache and served to other users." 
    
- The idea behind caching is very simple. Statically store “answers” (responses) to “questions” (requests) that are frequently requested—bypassing the need to re-compute heavy requests. A caching system needs to have at least two key functionalities in place:

  - How long to cache an item (i.e. File, HTTP Request, etc.) for
  - Determining whether or not a request hits the cache (therefore quick response) or misses it (therefore needs to ask the application)
    
![](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Instructional/1-Lesson-Plans/Unit-Web-Development/2/Images/proxy_poison.png)
    
  - What is the easiest way to poison a cache?
    > **Solution**: The easiest way to poison a cache is to attack unkeyed inputs, and HTTP headers in particular.

- You're encouraged to read the remaining sections yourself, but they _are not_ required for this exercise.

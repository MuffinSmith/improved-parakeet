# SQL Injection Spraying

## Instructions

### SQL Injection Hunting

- Navigate to `http://192.168.99.100/security.php`, and set your security level to **Low**. Turn on Burp's Interceptor.

- Navigate to `http://192.168.99.100/vulnerabilities/sqli`. Submit a request for ID 1, and send the intercepted request to Repeater.

- Attempt to find injection vulnerabilities manually. Proceed by answering the questions below:
  - Can you break the query syntax by injecting a single or double quote?
  - When you discover which quote breaks the syntax, submit something like: `id=1" UNION SELECT 1,2,3,4;`. 
    - Play with how many numbers you use after `SELECT`. 
    - Does `1,2,3,4` produce an error? What about `1,2,3`? 
    - Based on your results, how many columns does the underlying database query return?
  - After your `UNION SELECT` query works, add: `-- -&Submit=Submit` to the end of your query. It will look something like:`id=1" UNION SELECT 1,2,3,4;-- -&Submit=Submit`.
    - The above query is _wrong_, but looks like the one that works.
    - What do you suppose `-- -&Submit=Submit` means? **Hint**: Look at the buttons on the web form.

### SQL Spraying

- Instead of manually identifying a SQL injection vulnerability, use Intruder to spray the payloads in `sqli_payloads.txt`.

- Were you able to find the successful payload with this method?

## Questions

- Identify three disadvantages to spraying SQLi payloads instead of looking for vulnerabilities manually.

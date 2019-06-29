# First Steps with Webhook
Use Firefox to navigate to: <https://webhook.site>.

Enable Foxy Proxy, and intercept a request to your unique Webhook URL. Be sure to disable the interceptor after you capture the request.

Then, follow the instructions below.

## Instructions
- Send the intercepted request to Repeater, and press **Go**. Compare the request in Repeater to the Webhook log to familiarize yourself with reading captured requests.

- In Repeater, add the following Header: `Cookie: PHPSESSID=FakeSessionID`. Then, press **Go**. Find the cookie in the Webhook log.

- Next, navigate to: <https://gist.github.com/>

- Create an image tag that looks like the one below.

  ```html
  <img src="<Your Webhook URL>?example=parameter" >
  ```

- Save your Gist, then click the **Raw** link.

- Load the link to your gist with the RFI vulnerability at: <http://ptl-08a17b2b-81673f5e.libcurl.so/?page=intro.php>

- Return to your Webhook log, and find the most recent request. Identify the query parameter that was sent.

# Cookies and Sessions

## Instructions

### Inspecting Cookies

- Log into DVWA, and inspect your cookies in Omnibug. List the names of the cookies you see, and what piece of functionality you suppose each governs.

- Navigate to `http://192.168.99.100/vulnerabilities/weak_id`. Note where the page says that you're using that app on security level **low**.

- Open Burp Suite, and turn on the Interceptor.

- Reload the page at `http://192.168.99.100/vulnerabilities/weak_id`. Refer to the intercepted request in Burp Suite, and press `Ctrl + R` to send it to Repeater.

- Click the **Repeater** tab at the top of the Burp Suite UI. Change the value of the `security` header so that the app sets the level to "impossible".

- Inspect the response in the right-hand pane of Repeater (click the **render** button to see the page as it appears in the browser). Did your hack work?

### Protecting Cookies

- Return to `http://192.168.99.100/vulnerabilities/weak_id`. Verify that your security level is `low`.

- Right-click anywhere and press **Inspect Element**. Click the **Console** tab.

- Recall that users can read cookies with JavaScript. In the console, run: `document.cookie`.
  - Why might this feature of JavaScript be a security liability?

- Click the **Storage** tab in the pane that pops up, and find the site **Cookies**.

- Find the `security` cookie. Look at the `httpOnly` tab. Set its value to `true`. 

- Return to the **Console**, and try to print `document.cookie`. What effect does `httpOnly` have?

- Read this section on `HttpOnly` from OWASP before proceeding: <https://www.owasp.org/index.php/HttpOnly#What_is_HttpOnly.3F>

### Weak Session IDs

- Return to `http://192.168.99.100/vulnerabilities/weak_id`. Verify that your security level is `low`.

- Right-click anywhere and press **Inspect Element**. Click the **Storage** tab in the pane that pops up, and find the site **Cookies**.
  - Inspect the value of the `PHPSESSID` cookie.

- Back on DVWA, click **Generate**, then look at the intercepted request in Burp Suite.
  - What does the app say this button supposed to do?
  - What do you notice about the new token?
  - What is the value of `dvwaSession`?
  - Press **Generate** again. What is the value of `dvwaSession` now?

## Questions

- What kinds of functionality do webapps use cookies to implement?

- What kinds of attacks does the HttpOnly attribute protect against? How does it protect against them?

- Suppose an application uses the weak session ID algorithm you met above to generate an ID for each new visitor to the site. Then, the first user has `dvwaSession=1`; the second, `dvwaSession=2`; etc.
  - Describe an attack against this session ID that would allow a hacker to authenticate as `administrator`, assuming the site has 1,000 unique daily users, on average.
  - Describe at least two ways to prevent the attack you just suggested.

## Extension

- In the left navigation bar, click **DVWA Security**, and set the security level to **Medium**. Return to the **Weak Session ID** page, and intercept the requests that result from pressing **Generate** several times. 
  - Define the algorithm used to generate these `dvwaSession` values.
  - Is this algorithm susceptible to the attack you described before? Why or why not?

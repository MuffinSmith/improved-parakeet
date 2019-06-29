# Setting Up

In this exercise, you will set up DVWA for the day's exercises. Then, you'll verify that your Foxy Proxy and Burp Suite installations behave as expected.

## Instructions

- Launch DVWA by opening a terminal and running: `start_dvwa`.
- Open FIrefox, and navigate to: `http://localhost`.
- Login with the credentials below.
  - **Username**: `admin`
  - **Passwodr**: `password`
  - **Create/Reset** the database, then log in again with the same credentials.
- Launch Burp Suite, and start the proxy.
- Turn on Foxy Proxy.
- Navigate to **DVWA Security**. Verify that Burp Suite intercepts your request (you don't have to do anything with it yet—just make sure the interceptor is working).
- if so, copy the request into slack to share what you captured!
# Weak Session IDs
In this exercise, you will use Burp suite to study DVWA's weak session ID algorithm.

Launch DVWA by running: `start_dvwa`

Then, use Firefox to navigate to `http://localhost`.

Click **Create / Reset Database**, then log in with the same credentials as above.

Navigate to **DVWA Security**, and make sure your securty level is set to low.

**Good luck!**

## Instructions
- Navigate to the **Weak Session ID** vulnerabilty.

- Right-click anywhere in the page, and select **Inspect Element**. Click the **Storage** tab in the top navbar of the developer's panel, then click **Cookies** in the left sidebar.

- Click **Generate**. Look for the `dvwaSession` cookie.

- Click **Generate** again, and look at your new session ID. 
  - When you click **Generate** a third time, what will your session ID be?

- Navigate to **DVWA Security**, and set the security level to medium

- Generate a few session IDs. Which part of your session ID doesn't change?

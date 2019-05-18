# Manipulating Cookies

Start an instance of Google Gruyere: <https://google-gruyere.appspot.com/start>

Click **Agree & Start**, then follow the instructions below.

## Instructions

- Inspect your cookies.
  - Right-click anywhere, and select **Inspect**.
  - In the developer tools that pop up, click the arrow in the top-right (in the row where **Console** and **Network** appear), and select **Application**.
  - Select **Cookies** under **Storage** in the left pane.

- Click **Sign up**, and register for an account.

- **Sign in** and inspect your cookies. 
  - Which cookies has Gruyere set? What are their values?
  - Which is used to give you access to your account?

- Review the challenge instructions at: <https://google-gruyere.appspot.com/part3#3__cookie_manipulation>

- Look at **Hint 1**.
  - Gruyere's cookie format is: `hash|username|admin|author`
  - What does your cookie look like?
  - What's different?

- Return to your Gruyere instance, and **Sign out**.

- Click **Sign up**. Before proceeding, come up with a username that will have the `admin` value set.
  - **Hint**: What does your cookie look like if you register as `jane`? What about `jane]`?

- When you've discovered the weakness, slack out the username you registered with that gained administrative privileges.

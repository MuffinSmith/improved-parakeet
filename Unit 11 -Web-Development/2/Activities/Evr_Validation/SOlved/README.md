# Validation and User Input

Gruyere imposes a length limit on your usernames when you sign up. So, you can't register with something like:

> **Username**: `really_long_name|admin|author`

Even though the app attempts to prevent you from using long usernames, _you can bypass the length limit_. This means you actually _can_ register with `really_long_name|admin|author`...Just not through the web form.
 
The insight is that the _form_ won't let you submit a request with a long name, but the _server_ will process a request with a long name if it gets one.

Recall that the browser isn't the only web client there is—you can use, e.g., cURL to send requests without using the web form, instead.

This is one way to bypass client-side validations. Below, you'll find one other, and think critically about server-side validation.

---

Preventing the user from sending certain data through a form is called **client-side validation**—e.g., Gruyere preventing you from trying to register with long usernames.
- Why is client-side validation important?
  > **Solution**: It prevents normal users from submitting invalid data, which improves the user experience. However, it's easily bypassed, and does _not_ significantly improve security.

cURL is one way to bypass Gruyere's client-side validation. Navigate to the **Sign up** page; open the Developer Tools with `Ctrl + Shift + I`; then press `Ctrl + Shift + C`, and click on the field where you enter your username.
- Look at the HTML attributes that pop up in the **Elements** pane. Which one should you remove?
  > **Solution**: Double-click and delete `maxlength=16`. Done.

Preventing a server from _using_ certain data is called **server-side validation**. An example of this would be if Gruyere simply could not create accounts with long usernames.
- Why is server-side validation important?
  > **Solution**: Server-side validation hedges against the fact that client-side validation is vulnerable to outright bypass.

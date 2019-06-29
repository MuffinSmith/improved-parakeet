# XSS Review

## Questions

### Breaking Syntax

Consider the HTML below.

  ```html
  <img src="http://placeholder.it/200x200x" style="border: 1px solid blue;" />
  ```

Suppose the user profile page allows users to type a color to use for the border color. For instance, a user could enter `red` in a form, which would change the above HTML to:

  ```html
  <img src="http://placeholder.it/200x200x" style="border: 1px solid red;" />
  ```

Alternatively, you could set it to something invalid:

  ```html
  <img src="http://placeholder.it/200x200x" style="border: 1px solid NOT A COLOR!;" />
  ```

Use the ability to update the border color to inject an XSS payload that causes an alert box to pop up when the user mouses over the image.
- Which HTML event attribute should you use? Refer to: <https://www.w3schools.com/tags/ref_eventattributes.asp>

### Mitigation

Explain two different strategies for patching the above vulnerability.

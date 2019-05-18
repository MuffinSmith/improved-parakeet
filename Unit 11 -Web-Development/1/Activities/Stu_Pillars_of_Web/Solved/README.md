# Client-Side Assets

## Instructions

### Inspecting HTML
- Open [index.html](index.html) in a text editor.
  - List all the links that the browser will download when loading the page.
    > **Solution**: The following links will fire requests:
    >  - `https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css`
    >  - `https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css`
  - Identify the links that require CORS requests.
    > **Solution**: Both of the above requests will require CORS requests, since they are pulled from different domains.

- Open [index.html](index.html) in the browser.

- Enter a name in the form, and hit **Submit**. Note which part of the page changes.

- Look at the HTML in your text editor, or use `view-source` to see it in the browser. Find the text that changed when you submitted the name.
  - Which tag contains the name?
    > **Solution**: The name is contained in: `<span id="name-target">Larry</span>
  - Which attribute does the tag have?
    > **Solution**: The span tag has the attribute `id`.

- Look at the HTML for the input where you entered your name—it's contained in the `input` tag.
  - Which attribute does this share with the tag you identified in the step above?
    > **Solution**: The input tag has the attribute `id`, as well.

### Inspecting CSS
Next, you'll make some changes to a CSS file to see how it affects the appearance of the web page.

- Open `styles.css`. 

- Look at the line at the top. 
  - Explain what this statement does.
    > **Solution**: The `@import` statement performs an HTTP request for a font file, hosted by the server at the specified URL.
  - Explain why this functionality might introduce a security vulnerability.
    > **Solution**: Anywhere a web page or application performs a network request is a possible source of an injection attack.

- Uncomment the line containing the `font-family` property by removing the `/*...*/` around the CSS rule. Return to the browser, and reload the page.
  - This shows the result of downloading and applying a custom font via a CSS rule.

- Finally, change the value of the `color` property to, e.g., `tomato`, and reload the web page.

### Tinkering with JavaScript
Finally, you'll see how JavaScript can be used to update an HTML page after page load.

- Submit another name in the form, e.g.: `Jane`.

- Next, submit the name, but wrapped in HTML, e.g.: `<p>Jane</p>`. Also try:
  - `<h2>Jane</h2>`
  - `<h2 style="color: blue;">Jane</h2>`

- Right-click on the name, and select **Inspect Element**.

- Explain what happens when you:
  - Submit the form with a normal name, e.g.: `Jane`
    > **Solution**: In this case, the text from the form is dumped into the span tag that contained the original name.
  - Submit the form with HTML name, e.g.: `Jane`
    > **Solution**
    >  - In this case, the text from the form is dumped into the span tag that contained the original name...Exactly the same as in the previous case!
    >  - The difference is that, when you submit raw HTML, the browser _renders it as HTML_—it does _not_ display characters like `<`, `>`, etc., literally. Rather, it interprets them as special characters, and _runs the submission as code_. This is potentially a huge vulnerability, as it allows us to inject HTML, CSS, and/or JS!
  
- Finally, explain one way in which this functionality could be leveraged to exploit users.

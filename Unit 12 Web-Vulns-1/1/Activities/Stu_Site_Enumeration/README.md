# Site Enumeration

## Instructions

### Enumerating with Burp 

- Browse to `http://192.168.99.100/index.php`.

- Click the **Target** tab in Burp Suite, and find `http://192.168.99.100` in the **Site map** column on the left.

- Return to the browser, and click around the site a bit. Return to Burp Suite and inspect the site map.
  - **Note**: Do **not** use the Proxy. In other words, make sure that **Intercept is off** in the **Proxy** tab.

- Spider the site, and inspect the resulting site map. 
  - Do you notice any pages on the site that the spider didn't find?
  - Did you notice any pages that you missed but the spider _did_ find?

- Inspect the site map. Use the **URL** column to identify the URLs for the following:
  - Pages that might be vulnerable to injection attacks.
    - **Hint**: Which pages accept query parameters?
  - Pages that might be vulnerable to file upload attacks.
    - **Hint**: Which pages send POST requests?

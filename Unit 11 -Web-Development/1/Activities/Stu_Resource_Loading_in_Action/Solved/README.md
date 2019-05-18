# Resource Loading in Action

## Instructions

- Open Chrome, and open the Developer Tools with `Ctrl + Shift + I`.

- Navigate to `https://amazon.com`.

- Give the page a moment to load. When it's usable, look at the bottom of the Network inspector to see how many requests were fired.
  > **Solution**: I observed something around 383 requests.
  - What happens to this number when you scroll down on the page?
  - Where do you think the new requests are coming from?
    > **Solution**: The number increases, presumably due to AJAX via JavaScript.

- Inspect the resources in the list of requests. Find one requested from the domain `amazon.com`, and click on it.

- In the details pane on the right, click the **Headers** tab to see the request/response headers.
  - Which CORS headers should you look for in this request?
    > **Solution**: None, since this is a request to the same domain.

- Next, find a request for a resource from a different domain, and click on it.
  - Which CORS headers should you look for in this request?
    > **Solution**: All of them are possible, as this is a cross-origin request.

- If you found CORS headers in either response above, record which headers you found; which values they had; and what they're for.
  > **Solution**: In the response for a request for `https://d23tl967axkois.cloudfront.net/broadcast/B07L414W8Z.json`, I noted the following CORS headers:
  >   - `Access-Control-Allow-Credentials: true` instructs the browser to allow JavaScript to access cookies, authorization headers, or TLS client certificates.
  >   - `Access-Control-Allow-Methods: GET` indicates that the server only acknowledges cross-origin GET requests.
  >   - `Access-Control-Allow-Origin: https://amazon.com` indicates that cross-origin requests will only be fulfilled if they come from `https://amazon.com`. Requests from other domains will be denied.

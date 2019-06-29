# Breaking Quotes

## Instructions

### Gruyere

Open your Gruyere instance by opening: <https://google-gruyere.appspot.com/start>

- Click on **Home**. Find your username on the page, and note the font color.

- Click on **Profile**. Change the **Color** to `red`. Note how the font color changes.

- Right-click your name, then select **Inspect Element**. 
  - Where did the color you entered on your profile get echoed onto the page?

- Use your answer to the above to get an `onmouseover="alert(1)"` attribute into the page.
  - **Hint**: You'll have to save this payload through the **Color** field on your **Profile**.

## Bonus

After getting the above payload to fire, see if you can
- Use Burp Suite to intercept the request containing your payload
- Use Repeater to test two additional payloads
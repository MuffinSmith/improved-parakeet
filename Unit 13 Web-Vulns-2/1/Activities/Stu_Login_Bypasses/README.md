# Login Bypasses

## Instructions

### Classic Login Bypasses
Navigate to: <http://ptl-81d264b3-87f9c741.libcurl.so/login.php>

- Try to log in as `admin` with an arbitrary password.

- Try to log in as:
  - `admin'`.
  - `admin"`.
  - Based on the error output, which type of quote do you think the SQL statement uses?

- Add an `or` statement to your injection. 
  - If the server uses double quotes, your query should now look like: `admin" or <Condition>`, where `<Condition>` is your always-true condition, such as `'2'='2'`.

- If your injection works—congratulations! If not—suppose the SQL statement on the server looks like the below, where the username you submit to the form gets substituted in `$USERNAME`.
  - What does the statement look like if you substitute your payload for `$USERNAME`?
  - You might notice an extra quote. How could you modify your payload to remove it?

  ```sql
  SELECT * FROM users WHERE username='$USERNAME' and password='$PASSWORD'
  ```

## Extension

Recall that the OR clause results in the database retrieving _all_ rows. Of course, you'd expect a valid username/password combination to return just one. A well-designed web application would refuse to log in users whose username/password submission returns more than 1 result, since this would suggest an injection attack.

(Un)fortunately, this protection can be bypassed by injecting a LIMIT statement. Read about it at: <https://www.techonthenet.com/sql/select_limit.php>

Then, load the vulnerable form at: <http://ptl-726b6879-cc829763.libcurl.so/login.php>

Update your injection payload to include a LIMIT statement to bypass this form.

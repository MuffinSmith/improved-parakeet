# CREATE and INSERT

## Instructions

Navigate to: <https://www.db-fiddle.com/>

Then, follow the steps below.

---

- Create a table, called `exploits`, with the following columns:
  - `id`, of type `int`
  - `name`, of type `varchar(255)``
  - `severity`, of type `varchar(128)`

- Insert the following data into the table:
  - 1, 'Heartbleed', 'High'
  - 2, 'Use-After-Free', 'High'
  - 3, 'usermap_script', 'Medium'

- In the right pane, type: `SELECT * FROM exploits`.

## Extension

After completing the above, update your code as follows:
- Add two lines to the top of the left pane: 

  ```sql
  CREATE DATABASE warehouse;
  USE DATABASE warehouse;
  ```

- Change the line in the pane to: `SELECT * FROM warehouse.exploits`.

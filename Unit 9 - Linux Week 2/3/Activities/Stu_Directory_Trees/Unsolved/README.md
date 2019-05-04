# Directory Trees
## Instructions
- Create a script, called `create_dirs.sh`.

- Create a new directory, called `Cybersecurity`. Then, change into it.

- Use a for loop with `seq` to create the directories `Unit_1`; `Unit_2`; `Unit_3`; etc.

- Update your for loop to create the directories `Unit_1/1`; `Unit_1/2`; `Unit_1/3`; `Unit_2/1`; etc. Use brace expansion.
  - **Hint**: The command `mkdir Unit_1/{1,2}` creates the directories `Unit_1/1` and `Unit_1/2`.
  - **Hint**: Run `mkdir --help`, and read about the `-p` flag. You'll need it.

- Your script should create a directory tree like the below.

  ```bash
  Cybersecurity/
    Unit_1/
      1/
      2/
      3/
    Unit_2/
      1/
      2/
      /3
    # etc.
  ```

## Extension
- After getting your for loop to work, use brace expansion and `mkdir -p` to create the entire directory tree with a single command. You do _not_ need a for loop if you use brace expansions cleverly.
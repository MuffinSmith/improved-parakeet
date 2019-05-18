# Editing with nano

## Instructions

- Open a terminal, and move to `~/Documents`.

- Use nano to create a file called `notes.sh`.
  - Use the `-u` flag so you can undo/redo.

- Enter the following script:

  ```bash
  echo "Hello!"
  echo "Today is: $(date)"
  echo "This script is running as: $(whoami)"
  echo "Remember: '$(fortune | cowsay -f tux)'"
  echo "Goodbye!"
  ```

- Practice undo/redo.
  - Press `Alt + U` to undo.
  - Press `Alt + E` to redo.

- nano has rudimentary cut/paste functionality.
  - Move to the middle of a line, and press `Ctrl + K` to cut the rest of the line.
  - Press `Ctrl + U` to paste the rest of the line.

- You can search for text with `Ctrl + W`.
  - Press `Ctrl + W` and search for `echo`.
  - Press ` Alt + W` to go to the next search result.
  - Press `Alt + Q` to go to the previous search result.

- Save and exit when you're done exploring.
  - Press `Ctrl + X`; `Y`; then `Enter`.

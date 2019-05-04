# Cat Whisperer
## Instructions
Start by returning to the same Virtual Machine.

- Run the command `cat < /etc/passwd`.
  - What do you see?
  - How is this different from `cat /etc/passwd`?
  - Rewrite this command using the file descriptor for `stdin`.

  > **Solutions**
  >   - This prints the contents of `/etc/passwd` to the screen.
  >   - It's not—`cat < /etc/passwd` means, "Send the file `/etc/passwd` to `cat` as standard input." But, `cat /etc/passwd` does the same thing by default. The only difference is that including the `<` makes things more explicit.

- Next, run: `cat << EOF`
  - After entering this command, you will get a prompt because the `cat` program is now waiting for your input.
  - Enter a few lines of text, hitting the return key each time.
  - After a few lines of text, type `EOF` and hit return. What happens?
  - Explain what you think `EOF` means.

  > **Solution**: You'll notice that `cat` prints everything you type _after_ `<< EOF`, and _until_ the second `EOF`. The text between these delimiters is called a **heredoc**. The `<<` means: "use this heredoc as standard input".

### Bonus
- Run: `cat << EOF > my_file.txt`
  - How is this different from just `cat << EOF`?
  - Describe in detail what will happen when you complete this command.
  > **Solutions**
  >   - This command means: `Use the heredoc delimited by `EOF` as standard input to `cat`. When I'm done writing the heredoc, save anything that `cat` prints out to `my_file.txt`."
  >   - This is different from `cat << EOF` because it saves standard output to `my_file.txt` _instead_ of printing it to the console.

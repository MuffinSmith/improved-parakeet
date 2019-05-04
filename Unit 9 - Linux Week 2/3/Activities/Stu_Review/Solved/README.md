# Review
## Instructions
### Command Expansion
The `which <command>` command prints the absolute path to `<command>`. 

For example, `which ls` reports that the command `ls` is in the file `/usr/bin/ls`.

  ```bash
  $ which ls
  /usr/bin/ls
  ```
The `file <Target>` command tells you what kind of file `<Target>` is. For example, `file Notes.txt` tells you that `Notes.txt` is a text file.

- Use `file` and a command expansion to find out what kind of file `cat` is.
- What does `LS_PATH=$(which ls)` do?
  - **Note**: Feel free to run this in your Terminal to find out! Try running `echo $LS_PATH` after setting the variable.

  > **Solutions**
  >   - `file $(which cat)`
  >   - `LS_PATH=$(which ls)` creates a variable called `LS_PATH`, whose value is the absolute path to `ls`, `/usr/bin/ls`.

### Redirection
Consider the command: `cat nonexistent_file 2> /dev/null`
- What will print to the Terminal? Why?
  > **Solution**: This prints _nothing_. `cat nonexistent_file` generates an error, but `2> /dev/null` suppresses error messages by redirecting standard error to `/dev/null` (the "garbage can").

Consider the command: `cat nonexistent_file > /dev/null`
- What will print to the Terminal? Why?
  > **Solution**: This prints an error message. `cat nonexistent_file` generates an error, but `> /dev/null` _only redirects standard output_. So, standard error still gets printed to the console.

Consider the command: `cat /etc/passwd > /dev/null`. Assume `/etc/passwd` exists!
- What will print to the Terminal? Why?
  > **Solution**: This prints _nothing_. `cat /etc/passwd` will print to standard out, but `> /dev/null` redirects standard output to `/dev/null`, so it doesn't print.

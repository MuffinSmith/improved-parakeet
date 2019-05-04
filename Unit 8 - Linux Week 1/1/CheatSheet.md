# Day 1 Cheat Sheet — Intro to Linux

## Key Commands

### Essential Command Line
Below are examples of the most important basic Linux CLI tools.

#### Creating Files and Directories
To create a new, empty file, run:

  ```bash
  touch <filename>
  ```

To create a new, empty directory, run:

  ```bash
  mkdir <dirname>
  ```

To make a new tree of directories, run:

  ```bash
  mkdir -p lots/of/new/directories
  ```

#### Listing Files
To list files in a given directory, run:

  ```bash
  # List all files in ~/Documents, with human-readable file sizes
  ls -shal ~/Documents
  ```

<details>
  <summary>Expand for Explanations of Flags</summary>
  <ul>
    <li><code>-sh</code> lists file sizes in human-readable format
    <li><code>-a</code> lists all files, including hidden ones
    <li><code>-l</code> lists additional information, such as file owner; modified datetime; and size.
  </ul>
</details>

#### Copying and Moving Files
To copy a file from one location to another, use `cp`:

  ```bash
  # Copies ~/Documents/secrets.txt to ~/Documents/private/secrets.txt
  cp ~/Documents/secrets.txt ~/Documents/private
  ```

To move a file from one location to another, use `mv`. This command is also used to rename files.

  ```bash
  # Moves ~/Documents/secrets.txt to ~/Documents/private/secrets.txt
  mv ~/Documents/secrets.txt ~/Documents/private

  # Renames `old.txt` to `new.txt`
  mv old.txt new.txt
  ```

#### Removing Files and Directories
To remove a file, use `rm`. To remove an empty directory, use `rmdir`.

  ```bash
  # Removes old.txt
  rm old.txt

  # Removes EmptyFolder
  rmdir EmptyFolder
  ```

To remove a directory and all of its contents, use `rm -r`. This will prompt you whenever it tries to remove non-empty directories.

  ```bash
  # Removes ~/Documents
  rm -r ~/Documents
  ```

To remove a directory and all of its contents _without_ safety prompts, use `rm -rf`. **Be careful with this command**—it's irrevocable.

  ```bash
  # Removes ~/Documents, does not prompt user
  rm -rf ~/Documents
  ```

#### Creating and Extracting Archives
To create a tarball, run: `tar cvf <Archive Name> <File List>`

  ```bash
  # Creates archive.tar from ~/Documents
  tar cvf archive.tar ~/Documents

  # Creates archive.tar from `file.one` and `file.two`
  tar cvf archive.tar file.one file.two
  ```

To extract a tarball, run: `tar xvf <Archive Name>`

  ```bash
  # Unpack `archive.tar`
  tar xvf archive.tar
  ```

#### Listing Processes
To list processes started by the current user, run `ps`.

To list all processes, run `ps aux`.

To kill a process, run `kill <PID>`.

To kill all processes with a given name, such as `python`, run: `killall <Process Name>`.

  ```bash
  # Kills all `apache2` servers
  killall apache2
  ```

#### Installing Packages
To update PPAs, use `apt update`.

  ```bash
  # Note: Run with `sudo` when a normal user
  sudo apt update
  ```

To install new packages, use `apt install <packages>`.

 
  ```bash
  # Note: Run with `sudo` when a normal user
  sudo apt install vim gedit
  ```

To remove a package, use `apt remove <package>`. You should also run `apt autoremove` right after to clean up properly.

  ```bash
  # Note: Run with `sudo` when a normal user
  sudo apt remove vim gedit
  sudo apt autoremove
  ```

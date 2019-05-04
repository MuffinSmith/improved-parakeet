## GP: Installing Packages

- In this next activity, students will combine their knowledge of nano and package management to install `cowsay` and `fortune`.

* Given root access on a Ubuntu 18.04 Linux VM, students must be able to..

* Use apt to install fortune and cowsay
* Add a line to ~/.bashrc that prints a cowsay message with fortune | cowsay -f tux
* Start a new terminal to see the effect of adding this script to ~/.bashrc

- Instructions:
  - In this activity you will be installing the applications `Fortune` and `Cowsay`.
    - Fortune is a application that gives you a random quote every time you open the terminal up.
    - Cowsay is an application that creates an ASCII character appear to tell you your quote.
  - You will need to use the command that you have learned from the installing packages section in order to complete this in class assignment.
    - HINT: `apt-get install <package-name>`

**SOLUTION:** Explain to students that to install a list of quotes for Tux to give us every time we open the terminal app, we will first need to install an app called "Fortune". This is done by using the command `apt-get install fortune`.
 - Next, explain to the students that we're going to need to use a tool that will give Tux the penguin shape in ascii characters. This is done by using the command `apt-get install cowsay`

- To test this command, run ` fortune | cowsay -f tux`
  - Once you have `Fortune` and `Cowsay` and you have tested the command to make sure it works, you will need to make changes to the `~/.bashrc` file so the command runs each time you open your terminal.
    - Add the following line `fortune | cowsay -f tux` to the very bottom of the `~/.bashrc` file.
    - HINT: Use `nano` to edit the `~/.bashrc` file.

**SOLUTION:** Use the command `nano etc/bash.bashrc` and append the line `fortune | cowsay -f tux` to the bottom of the file.
- Open a new Terminal and verify that you can see Tux giving you a random quote.

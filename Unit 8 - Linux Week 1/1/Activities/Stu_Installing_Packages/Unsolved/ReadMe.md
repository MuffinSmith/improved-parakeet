## GP: Installing Packages

- In this next activity, students will combine their knowledge of nano and package management to install `cowsay` and `fortune`.

- Slack out the instructions in [Stu_Installing_Packages/README.md](Activities/Stu_Installing_Packages/ReadMe.md).

- Instructions:
  - In this activity you will be installing the applications `Fortune` and `Cowsay`.
    - Fortune is a application that gives you a random quote every time you open the terminal up.
    - Cowsay is an application that creates an ASCII character appear to tell you your quote.
  - You will need to use the command that you have learned from the installing packages section in order to complete this in class assignment.
    - HINT: `apt-get install <package-name>`

- To test this command, run ` fortune | cowsay -f tux`
  - Once you have `Fortune` and `Cowsay` and you have tested the command to make sure it works, you will need to make changes to the `~/.bashrc` file so the command runs each time you open your terminal.
    - Add the following line `fortune | cowsay -f tux` to the very bottom of the `~/.bashrc` file.
    - HINT: Use `nano` to edit the `~/.bashrc` file.

- Open a new Terminal and verify that you can see Tux giving you a random quote. Take a screenshot, and show it to your neighbor.

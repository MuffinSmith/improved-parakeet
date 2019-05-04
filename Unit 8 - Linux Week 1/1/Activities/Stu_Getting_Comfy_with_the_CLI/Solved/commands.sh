### Review
# Get started by opening up a Terminal.

# Move into your home directory, and then into your Documents folder.
cd ~/Documents

# Create the following directories:
mkdir Cybersecurity Class_Notes Class_Resources

# On second thought, you realize you don't need a `Cybersecurity` folder, since you have a `Class_Notes` directory. Remove it.
rmdir Cybersecurity

# Move into `Class_Notes`, and create a file called `Linux_Notes`.
cd Class_Notes
touch Linux_Notes

# Create a folder called `12_Intro_to_Windows_and_Linux` in `Class_Notes`, and move `Linux_Notes` into this folder.
mkdir 12_Intro_to_Windows_and_Linux
mv Linux_Notes 12_Intro_to_Windows_and_Linux

# Use `man rm`, and search for the `-i` flag. What does it do?
man rm
/-i

# Use `rm -i` to try to remove `Linux_Notes`, but choose _not_ to remove the file.
rm -i Linux_Notes

### Using Manpages 
# Change back to your home directory, and list all the files.
cd ~
ls

# Use `man ls`, and search for "all". Figure out which flag lets you list all files.
man ls
/-all

# List all files in your home directory. Write down the names of all the new files you see.
ls -a

# Look at the first few lines of each of the new files. 
head .bashrc
head .bash_logout
head .profile
head .ICEauthority
  
# Use the manpages to find out how to use `ls` to "sort by modification time".
man ls
/modification time

# Use the manpages to find out how to use `ls` in "long listing format".
man ls
/long listing format

# Use the above two options together to list every file in your home directory, sorted according to the time they were last modified.
ls -alt

# Use the manpages to find out how to use `ls` to sort alphabetically.
man ls
/alphabetical

# List every file in your home directory in alphabetical order, in long listing format.
ls -alX

# Move into the directory containing the tarball, and use `man tar` to figure out how to "list" the files in an archive.
cd Records

# Use `tar` to list the files in the archive.
tar tvf grocery_starter.tar

# Use `tar` to extract the files in the archive.
tar xvf grocery_starter.tar

### Cutting Up Files
# Use `cat` to look at the file you extracted. What does it contain?
cat groceries.txt

# Set the variable continueWriting to "y" to start things off
continueWriting = "y"
# Establish a connection to "Notes.txt" and set the mode to "write"
notesFile = open("Notes.txt","a")

# Check if the user would like to write some more text to the page
while continueWriting == "y":

    # Ask the user to enter some text and save it to a variable
    text = input("Please enter text to be saved into the file: ")
    # Use notesFile.write() to push the text in the above variable to the external file
    notesFile.write(text)

    # Add a newline character after the entered text
    notesFile.write("\n")
    # Ask the user if they would like to write another line
    continueWriting = input("Would you like to write more text into the page? (y)es/(n)o: ")

notesFile.close()
# Set the variable continueWriting to "y" to start things off
continueWriting = "y"

# Establish a connection to "Notes.txt" and set the mode to "write"
notesFile = open("Notes.txt", "w")

# Check if the user would like to write some more text to the page
while(continueWriting == "y"):

    print("\n-------------\n")    

    # Ask the user to enter some text and save it to a variable
    toWrite = input("Please enter some text to write...\n")

    # Use notesFile.write() to push the text in toWrite to the external file
    notesFile.write(toWrite)

    # Add a newline character after the entered text
    notesFile.write("\n")

    print("\n-------------\n")

    # Ask the user if they would like to write another line
    continueWriting = input("Please enter (y) if you would like to add another note...\n")

notesFile.close()
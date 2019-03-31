# Create a function that will ask what the user wants to do
def getChoice():

    # Collect the user's choice from the terminal
    userChoice = input("What would you like to do?\n[1]Read\n[2]Write\n[3]Quit\nSelection: ")
    print("---------------------")

    # Return the user's choice back to the main application
    return userChoice

# Create a function that will read the external file and print out the data it contains
def readFile():

    # Open up the external file in read mode
    watchlistFile = open("Watchlist.csv", "r")

    # Read in the text from the external file
    watchlistText = watchlistFile.read()

    # Split the file on each newline
    watchlistRows = watchlistText.split("\n")

    # Remove the last row which is empty from the list
    # This empty row was a result of our split on newline character
    watchlistRows.pop()

    # Loop through each row in the list of watchlistRows
    for row in watchlistRows:

        # Split the contents of the row on each comma
        rowData = row.split(",")

        # Print out each piece of data to the terminal
        print("Name: " + rowData[0])
        print("Birth Year: " + rowData[1])
        print("Reason to Watch: " + rowData[2])
        print("Threat Level: " + rowData[3])
        print("---------------------")
    
    # Close the external file
    watchlistFile.close()

# Create a function that will write a new row of data into the external file
def writeFile():

    # Open up the external file in append mode
    watchlistFile = open("Watchlist.csv", "a")

    # Collect information from the user
    name = input("What is the individual's name?\n")
    birthYear = input("What year was the individual born?\n")
    reason = input("For what reason should we watch the individual?\n")
    threat = input("What level a threat is the individual?\n")
    print("---------------------")

    # Create a formatted string using the collected information
    stringToWrite = name + "," + birthYear + "," + reason + "," + threat + "\n"

    # Write the data to the external file
    watchlistFile.write(stringToWrite)
    watchlistFile.close()

# Collect the user's initial choice
userChoice = int(getChoice())

# Run a while loop so long as the user's choice is "1" or "2"
while (userChoice == 1 or userChoice == 2):

    # Check to see if the user selected the read option
    if(userChoice == 1):
        # Run the readFile() function
        readFile()
    
    # Check to see if the user selected the write option
    if(userChoice == 2):
        # Run the writeFile() function
        writeFile()
    
    # Collect the user's choice once more.
    userChoice = int(getChoice())

# Print out "THANK YOU FOR USING THE WATCHLIST"
print("THANK YOU FOR USING THE WATCHLIST")
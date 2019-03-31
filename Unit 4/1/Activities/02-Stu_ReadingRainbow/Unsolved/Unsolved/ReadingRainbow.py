# Ask the user for a color and save it to a variable
var1 = input("What color would you like to look up?: ")

# Check that the color entered is one of the colors with an associated file
if var1 in ["blue","green","orange","red","violet","yellow"]:
# Create a connection to the file that the user entered
# Since the files are all in the "Colors" folder the path should be "Colors/<Input>.txt"
    colorFile = open("Colors/" + var1 + ".txt")
# Read in the text contained within the colorFile
    fileText = colorFile.read()
    print(fileText)
# Close the connection to the colorFile
    colorFile.close()
# If there is no file associated with the color entered then print out an apology to the screen
else:
    print("No file associated with that file (:   ")
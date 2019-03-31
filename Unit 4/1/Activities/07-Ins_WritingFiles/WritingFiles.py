# The open() function is also used for writing, though it defaults to "r"ead
# so we have to use the "w" mode as the second argument ("w"rite, instead of "r"ead)
diary_file = open("MyPersonalDiary.txt", "w")


# The .write() function is then used to push the text into the external file
diary_file.write("My chicken ate all of the cat food.")

# Since no spacing or newlines are added between .write() functions, they have to be programmed into the application manually
diary_file.write("\nTuna was my favorite flavor but I swear i do not eat cat food.")


diary_file.close()
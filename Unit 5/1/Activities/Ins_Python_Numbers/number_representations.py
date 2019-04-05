# Collect a number from the user
letter = input("Please provide a letter to convert. ")

# NOTE: The \t indicates a tab stop--it makes printing prettier
# Print Letter 
print("Letter:\t ", letter)

# Print ASCII
ascii_value = ord(letter)
print("ASCII:\t ", ascii_value)

# Print Hex
print("Hex:\t ", hex(ascii_value))

# Print Octal
print("Octal:\t ", oct(ascii_value))

# Print Binary
print("Binary:\t ", bin(ascii_value))

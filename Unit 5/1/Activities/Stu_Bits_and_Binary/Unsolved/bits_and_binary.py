# Get a string to encode from the user
string = input("Please enter a string to encode. ")

# TODO:Convert to ASCII encoded
# Create a list called `ascii_encoded`
ascii_encoded = list()
  # For every letter in `string`
  # add its ASCII value to`ascii_encoded`
  for letter in string:
    ascii_encoded.append(ord(letter))

# TODO: Convert ASCII to binary
# Create a list called `binary`
  # For every code point in `ascii_encoded`
  # add its binary value to `binary`

# TODO: Convert ASCII to hex
# Create a list called `hexadecimal`
  # For every code point in `ascii_encoded`
  # add its hex value to `hexadecimal`

# Print every code point in `ascii_encoded`
# NOTE: Use `print(<value to print>, end=" ")`
# to keep everything on the same line

# Print a separator
print("\n" + "=-" * 12)

# Print every byte in `hexadecimal`

# Print a separator
print("\n" + "=-" * 12)

# Print every bit in `binary`

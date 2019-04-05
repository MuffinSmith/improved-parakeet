# Hash Magic

In this activity, you will use hash signatures in a Python script to:
- Identify an original document from amongst a group of fakes
- Create a antivirus scanner that will scan a directory for a given piece of malware

This activity requires the new tools you just learned in lecture. Examples of these tools in use are included below for your convenience, in the section called **Reference**.

## Instructions

### Find the Needle in the Haystack

Open the starter file in [haystack.py](Unsolved/haystack.py), and fill in the code for the comments starting with `# TODO`.

To test your solution, run the solution you write in `Unsolved/haystack.py` script with the path: `../Resources`. You should identify `Zimmerman3.txt` as the original file.

### AntiVirus Scanner

Open the starter file in [av.py](Unsolved/av.py), and fill in the code for the comments starting with `# TODO`.

To test your solution, run the solution you write in `Unsolved/av.py` script with the path: `C:/Program Files/Git/usr/bin` (Windows), or `/usr/bin` (Mac). Your script should find `ls` in the target directory.

## Reference

### Reading Raw Bytes

To read a file as "raw bytes" (e.g., raw 1s and 0s), pass `"rb"` as the mode to `open` files with.

```python
filepath = "./my/binary/file"
with open(filepath, "rb") as file:
    contents = file.read()
```

Working with raw bytes makes it easier to work with hashes.

### Hashing Files

To get a file's hash signature, we need to use Python's `hashlib` module, best understood by example.

```python
import hashlib

# Text to hash
# The `b` prefix makes this raw data instead of a normal string--not an important detail for now!
text = b"This is my sample text!"

# Hashing the data
sha256 = hashlib.sha256()
sha256.update(text)
hashed = sha256.hexdigest()
```

**Heads-Up**: The three lines are the bottom are required _every_ time you want to create a hash signature—you cannot reuse the `sha256` object you create initially. Doing so is a common mistake.

This means that, if you need to hash files in a loop, you should have these all three of these lines _inside_ of the loop!

### Checking if a File is a File

Python will complain if you try to read a directory as a file...Fair enough.

To check that a filepath represents a file and not a directory, use `os.path.isfile`.

```python
import os

path_to_file = "./MyFavoriteThings.txt"
path_to_directory = "./Pictures"

if os.path.isfile(path_to_file):
    print("This will print!")

if os.path.isfile(path_to_directory):
    print("This will not print!")
```

You'll need to use `os.path.isfile` in your solution for [av.py](Unsolved/av.py).

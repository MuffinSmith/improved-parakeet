# Cracking Hashcat

## Getting Setup 

* **Mac** users need to have homebrew installed. 
  * Go to https://brew.sh/  
  * Run the command found there, `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
  * Next in your terminal run `brew install hashcat`
  
* **Windows** users should download the zipped *hashcat binaries* from: https://hashcat.net/hashcat/
  - Download *9 Zip* from the Windows Store
  - Unzip the the hashcat binaries downloaded in step 1
  - Open a terminal to move into the directory hashcat was unzipped to, then run `hashcat` to run it

  
## Instructions 

- In this exercise, you have been given the three following files:
  - `1.txt`
  - `2.txt`
  - `3.txt`

- Your objective is to identify which hash each is, then identify the correct Hashcat flags to discover the password. 
- Once you have found the correct algorithm rename the file to the algorithm name. 

## Hints

Use the following hints to determine the hash type:
- `1.txt`: Bitcoin uses this hashing algorithm.
- `2.txt`: Windows uses this to hash its passwords.
- `3.txt`: Github uses this hash for committing items.

## Reference

The following site is a _fantastic_ resource for Hashcat's command-line flags. Refer to this once you've determined which hash algorithm corresponds to each password file.

Link: <https://hashcat.net/wiki/doku.php?id=example_hashes>

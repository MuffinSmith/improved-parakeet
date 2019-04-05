# AES in CBC Mode

## Instructions

### CBC Encryption Diagram

Draw and label a diagram of AES being used to encrypt in CBC mode.

Then, draw and label a diagram of AES being used to decrypt in CBC mode.

Remember the following components:
- IV
- Key
- Plaintext Blocks
- XOR Operation
- Ciphertext Blocks

## Extension

- Do you need to keep your IV secret? Why or why not?

- The example message you used to create your diagram had exactly 16 characters, which is perfectly divisible by our hypothetical block size of 4 bits. How do you suppose you'd deal with the case of a message that's, say, 15 characters long, like `attack at dawn!`?

- Read the **PKCS5 Padding** heading: <https://cryptosys.net/pki/manpki/pki_paddingschemes.html>

- Apply PKCS5 padding to the following messages, assuming a block length of 16 characters. Represent your padding in hexadecimal format, e.g.: 1 = `\x01`, 2 = \x02`, 10 = `\xa`, 16 = `\xf`, etc.
  - `attack at dawn!`
  - `attack at dawn`
  - `short`

- Why is padding necessary?

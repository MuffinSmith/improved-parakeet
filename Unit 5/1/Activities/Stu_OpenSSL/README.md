# Encrypting Data with OpenSSL

In this activity, you'll use the command-line tool OpenSSL to encrypt data with the AES symmetric cipher.

## Instructions

Before you start, create a new directory called `~/.openssl`. You'll save your keys, passphrases, etc., into this directory.

### Generating Key and IV

- Before you start, choose a password to use to protect your key. Save it in a file called `~/.openssl/pass`.

- Next, generate a key and IV with the following command:

  ```bash
  openssl enc -nosalt -aes-256-cbc -k <your password here> -P > ~/.openssl/key_and_iv
  ```

- Be sure to replace `<your password here>` with the password in `~/.openssl/pass`, of course.

- Inspect the contents of `~/.openssl/key_and_iv`. You should see something like the following:

  ```bash
  key=5D41402ABC4B2A76B9719D911017C59228B46ED3C111E85102909B1CFB50EA0F
  iv =DE37085F7EDA3711FA2D9FE7E0FC29BE
  ```

### Encryption

- Now that we have a key and IV, we can encrypt files on the command line.

- Create a file called `SecretMessage.txt`, and store a message inside of it.

- Encrypt the file with the following command:

  ```bash
  openssl enc -nosalt -aes-256-cbc -in SecretMessage.txt -out SecretMessage.txt.enc -base64 -K <key> -iv <iv>
  ```

- Copy and paste the key and IV in `~/.openssl/key_and_iv` into the placeholders for `<key>` and `<iv>`, respectively.

- Inspect the contents of `SecretMessage.txt.enc`. It should look like gibberish.

### Decryption

- To decrypt the file, issue the following command:

  ```bash
  openssl enc -nosalt -aes-256-cbc -d -in SecretMessage.txt.enc -base64 -K <key> -iv <iv>
  ```

- Copy and paste the key and IV in `~/.openssl/key_and_iv` into the placeholders for `<key>` and `<iv>`, respectively.

- This should print the original message to the command line.

## Extension

- After successfully encrypting/decrypting a file, send your seat partner an encrypted message; your key; and your IV. Verify that they're able to decrypt the message.

- For ease of use, open your `~/.bash_profile` in a text editor, and add the following lines:

  ```bash
  # Copy and paste the key and IV from ~/.openssl/key_and_iv here
  export OPENSSL_KEY="<your key value here>"
  export OPENSSL_IV="<your IV value here>"
  ```

- This lets you use `-K $OPENSSL_KEY -iv $OPENSSL_IV` instead of having to copy/paste out of `~/.openssl/key_and_iv`.

- **Warning**: This is _not_ a secure practice in general, as it exposes your (secret!) key to the Terminal. This is fine for our purposes in class, but isn't recommended in production systems.

## Questions

- In order for your partner to decrypt your message, you need to send them your symmetric key. How did you do this?

- Was the channel you used to transfer your symmetric key secure?

- Can you think of a way to _safely_ trade symmetric keys, where "safely" means "there's no chance any eavesdropper could have stolen it"?

- What is "base64"? What do you suppose the `-base64` flag does?

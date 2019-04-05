
## Commands

### GPG

#### Generating Keypairs

To generate a keypair:

```
gpg --gen-key
```

This raises a prompt to select the type of keypair to create.

#### Generating a Revocation Certificate

A **revocation certificate** is a document that warns the public _not_ to use a certain public key, in the event the private key is lost or compromised. This prevents people from using the invalidated public key to encrypt new data.

To generate a revocation certificate:

```
# Creates a revocation certificate in the file `revoke.asc`
gpg --output revoke.asc --gen-revoke <key name>
```

#### Inspect the Public Keyring

To list all the public keys GPG recognizes:

```
gpg --list-keys
```

#### Exporting and Importing Keys

To export a public key:

```
# Export the key associated with alice@example.org in alice.gpg
gpg --output alice.gpg --export alice@example.org
```

The file `alice.gpg` contains binary data, which includes unprintable characters. This means you can't inspect the contents of `alice.gpg` on the command line.

As a workaround, you can export keys with **ASCII armor**, which allows them to be printed to the screen.

To export a key with ASCII armor:

```
# Export the key associated with alice@example.org in alice.gpg
gpg --armor --output alice.gpg --export alice@example.org
```

To import a public key stored in a `gpg` file:

```
gpg --import bob.gpg
```

#### Encrypting and Decrypting

To encrypt a document:

```
gpg --output encrypted_document.gpg --encrypt --recipient alice@example.org unencrypted_document
```

To decrypt a document:

```
gpg --output unencrypted_document --decrypt encrypted_document.gpg
```

Finally, to encrypt using a symmetric-key algorithm:

```
gpg --output encrypted.gpg --symmetric unencrypted_file
```

This is primarily useful for encrypting documents only you plan to decrypt later.

#### Signing Document

To generate an encrypted document with an attached signature:

```
gpg --output document.sig --sign document
```

## Resources

- Overview of TLS/SSL: <https://www.ssl.com/article/ssl-tls-handshake-overview/>

- Summary of TLS Handshake: <https://www.ibm.com/support/knowledgecenter/en/SSFKSJ_7.1.0/com.ibm.mq.doc/sy10660_.htm>

- Summary of ECB Oracle Attacks: <https://news.ycombinator.com/item?id=7959519>

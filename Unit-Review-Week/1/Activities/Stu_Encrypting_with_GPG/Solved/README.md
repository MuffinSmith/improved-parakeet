# Encrypting with GPG

## Solutions

> **Solution**
> ```bash
> # Inspect the public keys GPG recognizes.
> $ gpg --list-keys
> # Use GPG to generate a new keypair.
> $ gpg --gen-key
> # Export your new keypair with ASCII armor. Exchange it with your seat partner via Slack
> $ gpg --armor --output instructor.gpg --export instructor@example.org
> # Import your partner's key
> $ gpg --import partner.gpg
> # Encrypt a document with your partner's key
> $ gpg --output encrypted.gpg --encrypt --recipient partner@example.org unencrypted_document
> # Read the encrypted document
> $ cat document.enc
> # Decrypt the document
> $ gpg --output document.decrypted --decrypt encrypted.gpg
> ```

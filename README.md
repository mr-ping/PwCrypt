# PwCrypt
You can use this tool to encrypt and validate the password

### Installation:

    git clone https://github.com/mr-ping/PwCrypt.git

### Usage:

1. Import a class named PwCrypt

        from pwcrypt import PwCrypt

2. Define a text based password

        text_password = 'MyPassword'

3. Create the instance of PwCrypt
   
        pw = PwCrypt()

4. Generate the hashed password

        hashed_password = pw.hash_password(text_password)

5. Then we can validate whether my password is crrect with the hashed  
one which just we got.

        pw.validate_password(text_password, hashed_password)

### More help:
    
    from pwcrypt import PwCrypt
    help(PwCrypt)

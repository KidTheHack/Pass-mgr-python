# Password manager in python


# Introduction.
This is my password manager written in Python. It’s a very minimalist 
project that uses only the **cryptography** library, specifically the 
**Fernet** class for the encryption functions essential to its operation,
and **InvalidToken** to handle exceptions caused by invalid keys.
Below you’ll find a quick usage guide. 
If you're interested, on my [website](https://kid-hack.com "My website")
(in Italian) you can find a more detailed explanation of how the 
project is structured.
I hope you find it useful! Feel free to contact me for anything either 
here on GitHub or through the contacts listed on my [website](https://kid-hack.com "My website").

# Implemented Features.
* Creation of new keys and password files.
* Loading of existing keys and password files.
* Decryption of stored services.
* Password file management:
    * Listing all stored services.
    * Adding new services.
    * Deleting services.



# Usage.
First, you need to install cryptography via pip, generate or load a key, create or load
a password file, and after that you can use all the other features.

## Options:
1. Generate new keys for encrypting password files.  
2. Load existing keys.  
3. Create new encrypted password files.  
4. Load existing password files.  
5. Add new services to the loaded password file.  
6. Generate a list of all services in the file.  
7. Retrieve the username and saved password for a service.  
8. Delete a service.

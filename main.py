from cryptography.fernet import Fernet
import os

"""
- This script allows users to encrypt and decrypt files using the Fernet symmetric encryption algorithm.
- The encrypted files format remains the same but their contents turns into an unreadable file.
- you get an Encryption Key to be used when you want to decrypt the code.
- When decrypted using the provided encryption key, the files are restored to their original form.
"""
def generate_key():
    # Generating a random encryption key
    return Fernet.generate_key() 

def encrypt_file(key, file_path, output_file):
    # encrypts the users file with the key and saves the result.
    with open(file_path, 'rb') as file:
        data = file.read()

    f = Fernet(key) # uses the key to create a fernet object & encrypt. 
    encrypted_data = f.encrypt(data)

    with open(output_file, 'wb') as file: # Saves the encrypted data to the output file (the saved result).
        file.write(encrypted_data)

def decrypt_file(key, file_path, output_file):
    # decrypts the users file with the key and saves the result.
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)

    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

# encrypt or decrypt?
user_choice = input("Do you want to encrypt or decrypt? Enter 'encrypt' or 'decrypt': ")

if user_choice == "encrypt":
    # get the file, add a suffix of '_encrypt' and use the existing file ext. as the encrypted file ext. 
    file_path = input("Enter the path to the file you want to encrypt: ")
    filename, file_extension = os.path.splitext(file_path)
    encrypted_file = filename + "_encrypt" + file_extension

    # Generate encryption key
    encryption_key = generate_key()

    # encrypt the file and print out the encryption key to be used when decrypting. 
    encrypt_file(encryption_key, file_path, encrypted_file)
    print("File encrypted successfully.")
    print("Encryption Key: ", encryption_key.decode())

elif user_choice == "decrypt":
    # get the encrypted file, and also get the encryption key to decrypt the file. 
    file_path = input("Enter the path to the file you want to decrypt: ")
    encryption_key = input("Enter the encryption key: ").encode()

    # prepare the file name and ext. and replace the '_encrypt' suffix in the encrypted file to '_decrypt'
    filename, file_extension = os.path.splitext(file_path)
    decrypted_file = filename.replace("_encrypt", "_decrypt") + file_extension

    attempt = 0
    max_attempt = 3
    decrypted_successfully = False

    # attempt using the encryption key 3 times, "if only user enters the wrong key"
    while attempt < max_attempt:
        # if user enters the correct encryption key, then decrypt successfully. 
        try:
            decrypt_file(encryption_key, file_path, decrypted_file)
            print("File decrypted successfully.")
            decrypted_successfully = True
            break
        # if decryption key is wrong, then try again until user exceeds max. attempts...
        except:
            attempt += 1
            print("Wrong encryption key. Please try again.")
            encryption_key = input("Enter the encryption key: ").encode()
    # if user exceed the max. attempt then exit the script...
    if not decrypted_successfully:
        print("You have exceeded your max attempt. Exiting the script...")
# if use enter anything other than encrypt or decrypt print an error
else:
    print("Invalid Option. Please enter 'encrypt' or 'decrypt'.")
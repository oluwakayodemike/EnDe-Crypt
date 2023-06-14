# EnDe-Crypt 🔒

This script enables users to encrypt and decrypt files using the Fernet symmetric encryption algorithm. The encrypted files maintain their original format while their content is transformed into an unreadable state. Decryption can be performed by providing the correct encryption key, restoring the files to their original form.

# Running EnDe-Crypt ⚙️

After installing Python and the Crytography library You can run EnDe-Crypt locally on your terminal.

- clone the repository:
```bash
git clone https://github.com/oluwakayodemike/EnDe-Crypt/
```
- run the script:
```bash
python main.py
```

## Usage 

1. Run the script and choose whether to encrypt or decrypt a file.
2. If encrypting:
   - Enter the path to the file you want to encrypt.
   - The script will generate an encryption key and save the encrypted file with the "_encrypt" suffix added to the original file name.
   - Make sure to securely store the encryption key as it will be required for decryption.
3. If decrypting:
   - Enter the path to the file you want to decrypt.
   - Provide the encryption key used during encryption.
   - The script will decrypt the file and save the decrypted version with the "_decrypt" suffix added to the original file name.

## Dependencies 👫

Make sure you have all these installed on your local machine.

- Python3: needed to run the script
```bash
sudo apt update
sudo apt install python3
```
- cryptography library: Required to perform the encryption and decryption operations. Install it using `pip install cryptography`.

## Functions 🤖

### `generate_key()`

Generates a random encryption key using the Fernet algorithm.

### `encrypt_file(key, file_path, output_file)`

Encrypts the input file using the provided encryption key and saves the encrypted data to the output file.

- `key`: The encryption key as bytes.
- `file_path`: The path to the file to be encrypted.
- `output_file`: The path to save the encrypted file.

### `decrypt_file(key, file_path, output_file)`

Decrypts the input file using the provided encryption key and saves the decrypted data to the output file.

- `key`: The encryption key as bytes.
- `file_path`: The path to the file to be decrypted.
- `output_file`: The path to save the decrypted file.

## Using the Console. 💻
### Encrypting 🔐:
```
oluwakayodemike@ubuntu:~/Code/EnDe-Crypt$ python main.py
Do you want to encrypt or decrypt? Enter 'encrypt' or 'decrypt': encrypt
Enter the path to the file you want to encrypt: ~/Code/EnDe-Crypt/me.jpg
File encrypted successfully.
Encryption Key:  cqCSHQWUx6egzCRhQmKRp-xpQfwhTjXFfSDq7EYP1OQ=
```

### Decrypting 🔓:
```
oluwakayodemike@ubuntu:~/Code/EnDe-Crypt$ python main.py
Do you want to encrypt or decrypt? Enter 'encrypt' or 'decrypt': decrypt                                              
Enter the path to the file you want to decrypt: ~/Code/EnDe-Crypt/me_encrypt.jpg
Enter the encryption key: cqCSHQWUx6egzCRhQmKRp-xpQfwhTjXFfSDq7EYP1OQ=
File decrypted successfully.
```
**Note:** 
- Ensure you securely store the encryption key generated during encryption, as it is required for decryption.
- The encrypted file will be with a suffix of '_encrypt' while the decrypt with '_decrypt'

## Author 👨🏽‍💻

Oluwakayode Michael

## License 🪪

This project is licensed under the [MIT License](LICENSE).

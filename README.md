# Hill Cipher Project

This project implements a Hill Cipher, a polygraphic substitution cipher based on linear algebra. The Hill Cipher encrypts and decrypts text using a square 2x2 matrix key.

## Features

- **Encryption**: Enciphers plaintext using a valid key matrix.
- **Decryption**: Deciphers ciphertext using a valid key matrix.
- **Support for ASCII Characters**: Represents non-printing ASCII characters by their hexadecimal values.

## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/sameddallaa/hill-cipher.git
   ```

2. Navigate to the project directory:

   ```bash
   cd hill-cipher
   ```

3. Install any necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the main script to encrypt or decrypt text:

   ```bash
   python main.py
   ```

5. Follow the prompts to input plaintext or ciphertext and the key matrix.

## Example

Here's an example of encrypting and decrypting text using the Hill Cipher:

### Encryption

```plaintext
Enter plaintext: Hello, world!
Enter key matrix (2x2):
                                        7 7
                                        1 2
Encrypted text: »''0x12''è''D''=''Ç''!''0xe'"'"'S''°''4''0x96''S
```

### Note

The non-printing ASCII characters are represented by their hex codes, for instance, the end of medium ASCII character, which denotes the end of a string, is represented by the code 0x19

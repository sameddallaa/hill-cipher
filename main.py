from math import gcd, floor
from numpy import linalg, array
from hill_cipher import encrypt, decrypt


while True:
    try:
        key = []
        for element in range(4):
            key.append(int(input(f"Please enter the value of key[{element // 2}, {element % 2}]: \n")))
        
        det = round(linalg.det(array(key).reshape(2,2))) % 256
        if gcd(det, 256) != 1:
            raise ValueError
        break
    except ValueError:
        print("Key is not inversible. Please try again.")
        
print(f'Key: {array(key).reshape(2,2)}')
print(f'Select one of the following operations: \nEncryption: Type 1\nDecryption: Type 2\n')

while True:
    try:
        choice = int(input("Please enter your choice: \n"))
        if choice == 1 or choice == 2:
            break
        else:
            raise ValueError
    except ValueError:
        print("Invalid choice. Please try again.")

if choice == 1:
    plaintext = input("Please provide the text to be encrypted")
    ciphertext = encrypt(plaintext, key)
    print(f'The corresponding ciphertext: {ciphertext}\n')
else:
    ciphertext = input("Please provide the text to be decrypted")
    plaintext = decrypt(ciphertext, key)
    print(f'The corresponding plaintext: {plaintext}\n')
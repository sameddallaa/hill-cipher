from numpy import array
from hill_cipher import encrypt, decrypt

key = [9, 1, 3, 2]

with open('output.txt', 'w') as output:
    output.write(decrypt('input.txt', key))
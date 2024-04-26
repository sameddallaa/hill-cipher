from math import gcd
from numpy import array, dot, linalg
from utils import split_into_list_of_fours, char_to_int_map, reassemble_into_list_of_twos, int_to_char_map, inverse_mod_256, comatrix, consecutive_combinations, matrix_inverse_mod_256
def encrypt(plain, key):
    
    key_arr = array(key).reshape(2, 2)
    
    det = round(linalg.det(key_arr)) % 256
    
    if gcd(det, 256) != 1:
        raise ValueError('Key is not invertible')
    

    file_content_list = split_into_list_of_fours(plain)
    file_content_list_int = []
    
    for fragment in file_content_list:
        for char in fragment:
            file_content_list_int.append(char_to_int_map[char])
            
    file_content_list_int = reassemble_into_list_of_twos(file_content_list_int)
    
    cipher_text = []
    
    for content in file_content_list_int:
        plain_text_fragment = array(content).reshape(2, 1)
        cipher_text_fragment = dot(key_arr, plain_text_fragment)
        cipher_text_fragment = cipher_text_fragment.tolist()
        cipher_text.extend(cipher_text_fragment)
    cipher_text = [[c % 256 for c in fragment] for fragment in cipher_text]
    cipher_text_flattened = [item for sublist in cipher_text for item in sublist]
    output = []
    for c in cipher_text_flattened:
        output.append(int_to_char_map[c] if c != 39 else "'")
    return "".join(repr(item) for item in output)
        
        
def decrypt(cipher, key):
    
    key_arr = array(key).reshape(2, 2)
    
    det = round(linalg.det(key_arr)) % 256
    if gcd(det, 256) != 1:
        raise ValueError('Key is not invertible')
    
    cipher = cipher.replace('"\'"', "'single_quotes'")
    cipher = cipher.split("''")
    cipher = ["'" if x == "'single_quotes'" else x for x in cipher]
    file_content_list = split_into_list_of_fours(cipher)
    file_content_list_int = []
    
    for fragment in file_content_list:
        for char in fragment:
            try:
                file_content_list_int.append(char_to_int_map[char])
            except KeyError:
                file_content_list_int.append(char_to_int_map[char])
    file_content_list_int = reassemble_into_list_of_twos(file_content_list_int)
    
    plain_text = []
    
    key_inv = matrix_inverse_mod_256(key)
    
    for content in file_content_list_int:
        cipher_text_fragment = array(content).reshape(2, 1)
        plain_text_fragment = dot(key_inv, cipher_text_fragment)
        plain_text_fragment = plain_text_fragment.tolist()
        plain_text.extend(plain_text_fragment)
    plain_text = [[c % 256 for c in fragment] for fragment in plain_text]
    
    plain_text_flattened = [item for sublist in plain_text for item in sublist]
    output = []
    for p in plain_text_flattened:
        output.append(int_to_char_map[p])

    return "".join(repr(item)[1:-1] for item in output)

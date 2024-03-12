from math import sqrt, gcd
from numpy import array, dot, linalg
from utils import split_into_list, char_to_int_map, reassemble_into_list, int_to_char_map, inverse_mod_26, comatrix, consecutive_combinations
def encrypt(file_name, key):
    
    key_dimension = int(sqrt(len(key)))
    key_arr = array(key).reshape(key_dimension, key_dimension)
    
    det = linalg.det(key_arr) % 26
    
    det = int(det)
    
    if gcd(det, 26) != 1:
        raise ValueError('Key is not invertible')
    
    with open(file_name, 'r') as file:
        file_content = file.read()
        
        file_content_list = split_into_list(file_content, len(key))
        file_content_list_int = []
        
        for fragment in file_content_list:
            for char in fragment:
                file_content_list_int.append(char_to_int_map[char])
                
        file_content_list_int = reassemble_into_list(file_content_list_int, key_dimension)
        
        cipher_text = []
        
        for content in file_content_list_int:
            plain_text_fragment = array(content).reshape(key_dimension, 1)
            cipher_text_fragment = dot(key_arr, plain_text_fragment)
            cipher_text_fragment = cipher_text_fragment.tolist()
            cipher_text.extend(cipher_text_fragment)
            cipher_text = [[c % 26 for c in fragment] for fragment in cipher_text]
            
            cipher_text_flattened = [item for sublist in cipher_text for item in sublist]
            cipher_text_flattened = [int_to_char_map[code] for code in cipher_text_flattened]
            
    return "".join(cipher_text_flattened)
        
        
def decrypt(file_name, key):
    
    key_dimension = int(sqrt(len(key)))
    key_arr = array(key).reshape(key_dimension, key_dimension)
    
    det = linalg.det(key_arr) % 26
    det = int(det)
    if gcd(det, 26) != 1:
        raise ValueError('Key is not invertible')
    
    with open(file_name, 'r') as file:
        file_content = file.read()
        
        file_content_list = split_into_list(file_content, len(key))
        file_content_list_int = []
        
        for fragment in file_content_list:
            for char in fragment:
                file_content_list_int.append(char_to_int_map[char])
                
        file_content_list_int = reassemble_into_list(file_content_list_int, key_dimension)
        
        plain_text = []
        
        key_inv = inverse_mod_26(det) * comatrix(key)
        
        for content in file_content_list_int:
            cipher_text_fragment = array(content).reshape(key_dimension, 1)
            plain_text_fragment = dot(key_inv, cipher_text_fragment)
            plain_text_fragment = plain_text_fragment.tolist()
            plain_text.extend(plain_text_fragment)
            plain_text = [[c % 26 for c in fragment] for fragment in plain_text]
            
            plain_text_flattened = [item for sublist in plain_text for item in sublist]
            plain_text_flattened = [int_to_char_map[code] for code in plain_text_flattened]
            
    return "".join(plain_text_flattened)
import re
import numpy


int_to_char_map = {}
for i in range(256):
    if (i >= 32 and i <= 126) or (i >= 161):
        int_to_char_map[i] = chr(i)  
    else:
        int_to_char_map[i] = hex(i)

int_to_char_map[39] = 'single_quotes'

char_to_int_map = {b: a for (a, b) in int_to_char_map.items()}
def split_into_list_of_fours(string):
    return [string[i:i+4] for i in range(0, len(string), 4)]

def reassemble_into_list_of_twos(sequence):
    if len(sequence) % 2 != 0:
        while True:
            sequence.append(25)
            if len(sequence) % 2 == 0:
                break
    return [list(sequence[i:i+2]) for i in range(0, len(sequence), 2)]

def inverse_mod_256(integer):
    integer = integer % 256
    current = 1
    while True:
        if (integer*current) % 256 == 1:
            return current
        else:
            current += 1
            if current == 256:
                raise ValueError('Matrix is not invertible')
            
def comatrix(matrix):
    a = matrix[0]
    b = matrix[1]
    c = matrix[2]
    d = matrix[3]
    
    comatrix = numpy.array([[d, -b],[-c, a]])
    
    return comatrix

def matrix_inverse_mod_256(matrix):
    matrix_array = numpy.array(matrix).reshape(2, 2)
    det = round(numpy.linalg.det(matrix_array))
    
    return inverse_mod_256(det) * comatrix(matrix)

def consecutive_combinations(lst):
    if len(lst) <= 4:
        return lst
    output = []
    
    for i in range(0, len(lst), 4):
        output.append(lst[i:i+4])
        
    return output

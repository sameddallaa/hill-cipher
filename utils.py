import numpy

int_to_char_map = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z'
}


char_to_int_map = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25
}

def split_into_list(string, size):
    return [string[i:i+size] for i in range(0, len(string), size)]

def reassemble_into_list(sequence, size):
    if len(sequence) % size != 0:
        while True:
            sequence.append(25)
            if len(sequence) % size == 0:
                break
    return [list(sequence[i:i+size]) for i in range(0, len(sequence), size)]

def inverse_mod_26(integer):
    integer = integer % 26
    current = 1
    while True:
        if integer*current % 26 == 1:
            return current
        else:
            current += 1
            if current == 26:
                raise ValueError('Matrix is not invertible')
            
def comatrix(matrix):
    a = matrix[0]
    b = matrix[1]
    c = matrix[2]
    d = matrix[3]
    
    comatrix = numpy.array([[d, -b],[-c, a]])
    
    return comatrix

def consecutive_combinations(lst, n):
    return [lst[i:i+n] for i in range(len(lst) - n + 1)]

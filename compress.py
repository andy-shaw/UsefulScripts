import math
import string

infile = 'bitstream_input.txt'
encoding = {}
deliminator = '00'

#pre-calculated frequency of letters based on a separate dictionary with digits at the end
sorted_letters =   [' ', 'E', 'S', 'I', 'A', 'R', 'N', 
                    'T', 'O', 'L', 'C', 'D', 'U', 'P', '\n',
                    'M', 'G', 'H', 'B', 'Y', 'F', 'V',
                    'K', 'W', 'Z', 'X', 'Q', 'J', '0',
                    '1', '2', '3', '4', '5', '6', '7',
                    '8', '9', '%']

def create_encoding():
    #encoding is the same every time, I was simply lazy in writing out the binary by hand
    i = 1
    for c in sorted_letters:
        t = str(bin(i))[2:]

        #remove 001 from being in any of the encodings
        while deliminator + '1' in t:
            i += 1
            t = str(bin(i))[2:]
        encoding[c] = t
        i += 1

def compress(text):
    '''compress text, returns binary as string'''
    result = ''
    for letter in text:
        result += deliminator + encoding[letter]

    return result

def decompress(text):
    '''decompress provided text, returns string'''
    result = ''
    words = get_words(text)
    for word in words:
        for key, val in encoding.items():
            #remove deliminator
            if val == word[2:]:
                result += key

    return result

def get_words(text):
    current = 0
    next = 3
    words = []

    while next < len(text):
        #end of message checked first
        if text[next:next+3] == '001':
            #char has been found
            words.append(text[current:next])
            current = next
        next += 1
    #add last word
    words.append(text[current:])

    return words
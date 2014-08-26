'''
Andy Shaw
7/5/2014

This module provides a dictionary to interact with.
'''

default_name = 'dictionary.txt'
path = r'C:\\Python27\\Lib\\'

import string
from string import lower

def fetch(length=None):
    '''return a list with the words of the requested length'''
    f = open(path+default_name, 'r')
    words = []

    if not length: 
        if raw_input('The dict is large, do you wish to load? (y/n)').lower() == 'y':
            word = f.readline().strip()
            while word:
                words.append(word)
                word = f.readline().strip()
            return words

        else:
            return []

    if length:
        word = f.readline().strip()
        while word:
            if len(word) == length:
                words.append(word)
            word = f.readline().strip()
    return words

def fetch_indexed():
    '''return a dict of all the words for quick indexing'''
    f = open(path+default_name, 'r')
    words = {}
    for s in string.lowercase:
        words[s] = []

    if raw_input('The dict is large, do you wish to load? (y/n)').lower() == 'y':
        word = f.readline().strip()
        while word:
            #append words that start with certain letter to that letter in the dictionary
            words[word[0]].append(word)
            word = f.readline().strip()
        return words

    else:
        return {}
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 17:45:40 2023

@author: Pakhomav
"""

import random

def shuffle_unicode_char(char):
    offset = random.randint(1, 5000)
    shuffled_char = chr((ord(char) + offset) % 1114112)
    return shuffled_char

def shuffle_text(text):
    shuffled_text = [shuffle_unicode_char(char) for char in text]
    return ''.join(shuffled_text)

if __name__ == "__main__":
    filename = input("Please enter the file name to scramble: ")
    with open(filename, 'r', encoding='utf-8') as file:
        original_text = file.read()
    shuffled_text = shuffle_text(original_text)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(shuffled_text)
    print("Document has been scrambled.")

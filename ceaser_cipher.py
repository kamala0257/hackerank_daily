#!/bin/python3

import math
import os
import random
import re
import sys


def caesarCipher(s, k):
    encrypted = []
    # k can be larger than 26, so take the modulo
    k = k % 26
    
    for char in s:
        if 'a' <= char <= 'z':
            # Shift lowercase letters
            shifted = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            encrypted.append(shifted)
        elif 'A' <= char <= 'Z':
            # Shift uppercase letters
            shifted = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            encrypted.append(shifted)
        else:
            # Leave non-alphabetic characters unchanged
            encrypted.append(char)
            
    return "".join(encrypted)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

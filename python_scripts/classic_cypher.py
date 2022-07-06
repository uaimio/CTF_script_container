#!/usr/bin/env python3

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

def generateKey():
    start = random.randint(1,25)
    key = "".join([alphabet[start:], alphabet[0:start]])
    return key

def generateStdKey():
    return ["".join([alphabet[start:], alphabet[0:start]]) for start in range(1, 25)]

def encrypt(plain, key):
    ciphertext = ""
    for k in range(len(plain)):
        character = plain[k]
        #print(f'character={character}')
 
        if ord(character) <= 90 and ord(character) >= 65: # to find lowercase in the key
            i = alphabet.index(chr(ord(character)+32))
            #print(f'i={i}')
            characterEncrypted = chr(ord(key[i])-32)
            key = "".join([key[len(key)-1:],key[0:len(key)-1]])
            ciphertext = "".join([ciphertext,characterEncrypted])
        elif ord(character) <= 122 and ord(character) >= 97:
            i = alphabet.index(character)
            characterEncrypted = key[i]
            key = "".join([key[len(key)-1:],key[0:len(key)-1]])
            print(f'KEY={key}')
            ciphertext = "".join([ciphertext,characterEncrypted])
        else:
            ciphertext = "".join([ciphertext,character])
        
    return ciphertext

def decrypt(ciph, key):
    plaintext = ''

    for k in range(len(ciph)):
        character = ciph[k]
        if ord(character) <= 122 and ord(character) >= 97:
            i = key.index(character)
            characterDecrypted = alphabet[i]
            key = "".join([key[len(key)-1:],key[0:len(key)-1]])
            #print(f'KEY={key}')
            plaintext = "".join([plaintext,characterDecrypted])
        else:
            plaintext = "".join([plaintext,character])

    return plaintext

def handle():
    plaintextFLAG = "flag{uaimio}"
    cyphFLAG = "xcqv{gvyavn_zvztv_etvtddlnxcgy}xcqv{gvyavn_zvztv_etvtddlnxcgy}xcqv{gvyavn_zvztv_etvtddlnxcgy}xcqv{gvyavn_zvztv_etvtddlnxcgy}xcqv{gvyavn_zvztv_etvtddlnxcgy}xcqv{gvyavn_zvztv_etvtddlnxcgy}xcqv{gvyavn_zvztv_etvtddlnxcgy}xcqv{gvyavn_zvztv_etvtddlnxcgy}xcqv{gvyavn_zvztv_etvtddlnxcgy}"
    #key = generateKey()
    for key in generateStdKey():
        print(f'POSSIBILE DECR={decrypt(cyphFLAG, key)}')

    #ciphertext = encrypt(plaintextFLAG, "bcdefghijklmnopqrstuvwxyza")
    #print(ciphertext)
    
    return



if __name__ == "__main__":
    handle()

import hashlib
import string
import random

def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def getAWord(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def findSHA():
    while True:
        word = getAWord()
        hashed = encrypt_string(word)
        if(hashed.find('b00da') == True):
            print(word)
            print(encrypt_string(word))
            break
findSHA()

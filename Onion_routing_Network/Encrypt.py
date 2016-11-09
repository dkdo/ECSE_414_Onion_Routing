import random
import string


#ALLCHARACTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()/-_+=`<,>.?:;[]|'
ALLCHARACTERS = string.printable
keyRange = len(ALLCHARACTERS)

def encrypt (data, key):
    key = int (key)
    encryptedMessage = data
    translatedMessage = ''
    for char in encryptedMessage:
        if char in ALLCHARACTERS:
            charPosition = ALLCHARACTERS.find(
                char)  # gets the position of the character in the ALLCHARACTERS to shift it
            charPosition = charPosition + key
            # deals with the wrap around if the charPosition is bigger than the length of ALLCHARACTERS
            if charPosition >= keyRange:
                charPosition = charPosition - keyRange
            translatedMessage = translatedMessage + ALLCHARACTERS[charPosition]
        else:
            translatedMessage = translatedMessage + char
    encryptedMessage = translatedMessage
    return encryptedMessage

def decrypt (data, key):
    key = int(key)
    decryptedMessage = data
    translatedMessage = ''
    for char in decryptedMessage:
        if char in ALLCHARACTERS:
            charPosition = ALLCHARACTERS.find(
                char)  # gets the position of the character in the ALLCHARACTERS to shift it
            charPosition = charPosition - key

            # deals with the wrap around if the charPosition is smaller than 0
            if charPosition < 0:
                charPosition = charPosition + keyRange
            translatedMessage = translatedMessage + ALLCHARACTERS[charPosition]
        else:
            translatedMessage = translatedMessage + char
    decryptedMessage = translatedMessage
    return decryptedMessage


def generateKeys(numberOfNodes):
    listOfKeys = []
    for i in range(0, numberOfNodes):
        key = random.randint(0, keyRange - 1)
        listOfKeys.append(key)
    print "KEYS", listOfKeys
    return listOfKeys



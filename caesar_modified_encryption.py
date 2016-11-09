import random
import string

ALLCHARACTERS = string.printable
# ALLCHARACTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`<,>.?/:;{}[]|'

keyRange = len(ALLCHARACTERS)

def generateKeys(numberOfNodes):
	listOfKeys = []
	for i in range(0, numberOfNodes):
		key = random.randint(0, keyRange - 1)
		listOfKeys.append(key)
	return listOfKeys

# this method is really slow (runs in O(n^2))
def encryption(message, listOfKeys):
	encryptedMessage = message
	for key in listOfKeys:
		translatedMessage = ''
		for char in encryptedMessage:
			if char in ALLCHARACTERS:
				charPosition = ALLCHARACTERS.find(char) # gets the position of the character in the ALLCHARACTERS to shift it
				charPosition = charPosition + key
				# deals with the wrap around if the charPosition is bigger than the length of ALLCHARACTERS
				if charPosition >= keyRange:
					charPosition = charPosition - keyRange
				translatedMessage = translatedMessage + ALLCHARACTERS[charPosition]
			else:
				translatedMessage = translatedMessage + char
		encryptedMessage = translatedMessage
		print "current Encrypted Message is: ", encryptedMessage
	return encryptedMessage

def decryption(messageToDecrypt, listOfKeys):
	decryptedMessage = messageToDecrypt
	decryptKeys = listOfKeys[::-1]
	for key in decryptKeys:
		translatedMessage = ''
		for char in decryptedMessage:
			if char in ALLCHARACTERS:
				charPosition = ALLCHARACTERS.find(char) # gets the position of the character in the ALLCHARACTERS to shift it
				charPosition = charPosition - key

				# deals with the wrap around if the charPosition is smaller than 0
				if charPosition < 0:
					charPosition = charPosition + keyRange
				translatedMessage = translatedMessage + ALLCHARACTERS[charPosition]
			else:
				translatedMessage = translatedMessage + char
		decryptedMessage = translatedMessage
		print "current Decrypted Message is: ", decryptedMessage
	return decryptedMessage

def main(message, nodes):
	listOfKeys = generateKeys(nodes)
	print "key:", listOfKeys
	encryptedMessage = encryption(message, listOfKeys)
	decryptedMessage = decryption(encryptedMessage, listOfKeys)
	print "decrypted message is:", decryptedMessage
	print "initial message and decrypted message equal:", message==decryptedMessage

# modify the parameters here in order to test. The first parameter is the message we want to encrypt and the second is the # of nodes.
if __name__ == "__main__":
	main('Whatever WHATEVER your MESSAGE is YOU CAN DECRYPT IT USING THISS THING!!! CAN you HNDLE @#!@#@!', 500)
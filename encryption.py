import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import sys
import time


def generateKeys(numberOfNodes):
	listOfPrivateKeys = []
	random_generator = Random.new().read
	for i in range(0, numberOfNodes):
		privateKey = RSA.generate(1024, random_generator) #generates private key (key obj)
		listOfPrivateKeys.append(privateKey) #add key to the list
	return listOfPrivateKeys

def encryption(message, listOfKeys):
	encryptedMessage = message
	index = 1
	for key in listOfKeys:
		publicKey = key.publickey() #public key export ("creates" the public key based on the key obj)
		encrypt = publicKey.encrypt(encryptedMessage, 32) #encrypts the initial message, returns a tuple (i don't know why)
		encryptedMessage = encrypt[0]
		print "size of message is:", len(encryptedMessage)
		index += 1
	return encryptedMessage

def decryption(messageToBeDecrypted, listOfPrivateKeys):
	decryptedMessage = messageToBeDecrypted
	privateKeys = listOfPrivateKeys[::-1]
	index = len(privateKeys) - 1
	for key in privateKeys:
		decrypt = key.decrypt(decryptedMessage)
		decryptedMessage = decrypt
		index -= 1
	return decryptedMessage

def main(message, nodes):
	listOfKeys = generateKeys(nodes)
	encryptedMessage = encryption(message, listOfKeys)
	decryptedMessage = decryption(encryptedMessage, listOfKeys)

	print "decrypted message is:", decryptedMessage
	print "initial message and decrypted message equal:", message==decryptedMessage

#modify the parameters here in order to test. The first parameter is the message we want to encrypt and the second is the # of nodes.
if __name__ == "__main__":
    main("TESTING", 8)
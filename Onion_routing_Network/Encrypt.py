from Crypto.Cipher import AES
import base64
import os
import json

#TODO
def encrypt (data, key):
    # the block size for the cipher object; must be 16 per FIPS-197
    BLOCK_SIZE = 16

    # the character used for padding--with a block cipher such as AES, the value
    # you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
    # used to ensure that your value is always a multiple of BLOCK_SIZE
    PADDING = '{'

    # one-liner to sufficiently pad the text to be encrypted
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING


    # one-liners to encrypt/encode and decrypt/decode a string
    # encrypt with AES, encode with base64
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))

    encoded = EncodeAES(key, data)  # encrypts the initial message
    encryptedMessage = encoded

    return encryptedMessage

#TODO
def decrypt (data, key):
    # the block size for the cipher object; must be 16 per FIPS-197
    BLOCK_SIZE = 16

    # the character used for padding--with a block cipher such as AES, the value
    # you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
    # used to ensure that your value is always a multiple of BLOCK_SIZE
    PADDING = '{'

    # one-liner to sufficiently pad the text to be encrypted
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

    # one-liners to encrypt/encode and decrypt/decode a string
    # encrypt with AES, encode with base64
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

    decode = DecodeAES(key, data)
    decryptedMessage = decode
    return decryptedMessage


def generateKeys(numberOfNodes):
    listOfKeys = []
    # the block size for the cipher object; must be 16 per FIPS-197
    BLOCK_SIZE = 16
    for i in range(0, numberOfNodes):
        secret = os.urandom(BLOCK_SIZE)
        cipher = AES.new(secret)
        listOfKeys.append(cipher)
    return listOfKeys
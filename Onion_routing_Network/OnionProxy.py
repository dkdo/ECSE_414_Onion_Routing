import SocketServer
import OnionRoutingNetwork
import thread
import time
import socket
from Encrypt import encrypt, decrypt, generateKeys
import json


buffer = 4096
host = 'localhost'
port = 9999
keyList = ["500"]
count = -1


def validRequest(request):
    return True

def sendToEntryFunnel( data):
    print "Sending to entry funnel", data["IP"]
    entryFunnelAddress = ('localhost', data["IP"])
    entrySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    entrySocket.connect(entryFunnelAddress)
    entrySocket.send(json.dumps(data["data"]))

    time.sleep(50.0 / 1000.0);  # sometime thread just delete before sending . Slowing the program down
    response = entrySocket.recv(buffer)
    return response

def peelOnion(request, onion):
    for key in request["Path"]:
        onion = decrypt(onion, key)
    return onion

def assembleOnion(request):
    onion = encrypt(request["Message"], keyList[0])
    i = 1
    # create onion
    for IP in (request["Path"][1:][::-1]):
        # Create onion layer
        onion = encrypt({"IP": IP, "data": onion}, keyList[i])
        i += 1
    onion = {"IP": request["Path"][0], "data": onion}
    return onion

def OnionProxyHandler(clientSocket,client_address):
    global keyList
    data = clientSocket.recv(buffer)
    print "Received request from the Proxy Server\n"
    message = json.loads(data)
    process = validRequest(message)

    if message  == "requestForKey":
        response = keyList[count]
        print "Send key", response, "to", client_address
        clientSocket.send(str(response))

    elif process:
        keyList = generateKeys(len(message["Path"]) + 1)
        onion = assembleOnion(message)
        response = sendToEntryFunnel(onion)
        response = peelOnion(message, response)
        clientSocket.send(json.dumps(response))

    else:
        error = "The format of the message is not correct, please resend!\n"
        clientSocket.send(error)

    return


if __name__=='__main__':
    address = (host,port)
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(address)
    serverSocket.listen(100)

    while 1:
        clientSocket, client_address = serverSocket.accept()
        print "connected to", client_address
        count += 1
        thread.start_new_thread(OnionProxyHandler, (clientSocket,client_address))

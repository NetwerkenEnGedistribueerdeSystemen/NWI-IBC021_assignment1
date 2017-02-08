from socket import *
serverPort = 20000
# build TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
# bind it to port
serverSocket.bind(('', serverPort))
# listen (clients will start queuing up)
serverSocket.listen(1)

print('The echo server is ready to receive')
while 1:
    # the is waiting for clients to connect/ processes them one at a time
    connectionSocket, addr = serverSocket.accept()
    print('Processing client ', addr)
    try :
        sentence = connectionSocket.recv(1024)
        # while the other side hasn't closed the socket, do echo
        while sentence:
            echoedSentence = sentence
            connectionSocket.send(echoedSentence)
            sentence = connectionSocket.recv(1024)
    except error:
        pass
    print('Client closed ', addr)
    # close socket
    connectionSocket.close()

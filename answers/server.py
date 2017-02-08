import os.path
from socket import *

serverPort = 20000
# build TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
# bind it to port
serverSocket.bind(('', serverPort))
# listen (clients will start queuing up)
serverSocket.listen(1)


# author: Hendrik Werner s4549775


def send_file(path):
    if os.path.isfile(path):
        connection.send(b"file_content\n")
    else:
        connection.send(b"file_not_found\n")

def command_loop(connection):
    while True:
        received = connection.recv(1024).decode().strip()
        if received == "bye":
            connection.send(b"bye\n")
            return
        elif received.split()[0] == "get":
            send_file(received.split()[1])
        else:
            connection.send(b"cannot_understand\n")


def greeting(connection):
    while True:
        received = connection.recv(256).decode().strip()

        if received == "hello":
            connection.send(b"hello\n")
            return
        else:
            connection.send(b"cannot_understand\n")


def process_client(connection):
    try:
        greeting(connection)
        command_loop(connection)
    except error:
        print(error)


if __name__ == "__main__":
    print("Start the server.")
    while True:
        connection, address = serverSocket.accept()
        print("Process client", address)
        process_client(connection)
        print("Close connection", address)
        connection.close()

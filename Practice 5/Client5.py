import socket

# SERVER IP, PORT
IP = "192.168.1.131"
PORT = 8000



while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # The client is blocking the server....  NOT A GOOD DESIGN!!!
    msg = input("> ")

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()
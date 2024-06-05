import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
    "Test comment"
    
    server_socket = socket.create_server(("localhost", 6379))
    client, addr =    server_socket.accept() # wait for client
    client.send(b"+PONG\r\n")


if __name__ == "__main__":
    main()

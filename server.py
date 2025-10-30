import socket

def main():
    ip = "127.0.0.1"
    port = 5566
    buffer_size = 1024

    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to IP and port
        server_socket.bind((ip, port))
        print("[+]TCP server socket created.")
        print(f"[+]Bind to the port number: {port}")

        # Start listening for connections
        server_socket.listen(5)
        print("Listening...")

        while True:
            # Accept incoming client connection
            client_socket, client_address = server_socket.accept()
            print("[+]Client connected.")

            # Receive message from the client
            message = client_socket.recv(buffer_size).decode()
            print(f"Client: {message}")

            # Send response to the client
            response = "HI, THIS IS SERVER. HAVE A NICE DAY!!!"
            print(f"Server: {response}")
            client_socket.send(response.encode())

            # Close the client connection
            client_socket.close()
            print("[+]Client disconnected.\n")

    except Exception as e:
        print(f"[-]Error: {e}")

    finally:
        # Close the server socket (although in this case the server runs indefinitely)
        server_socket.close()

if __name__ == "__main__":
    main()

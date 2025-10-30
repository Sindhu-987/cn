import socket

def main():
    ip = "127.0.0.1"
    port = 5566
    buffer_size = 1024

    # Create the socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((ip, port))
        print("[+]Connected to the server.")

        # Send data to the server
        message = "HELLO, THIS IS CLIENT."
        print(f"Client: {message}")
        client_socket.send(message.encode())

        # Receive response from the server
        response = client_socket.recv(buffer_size).decode()
        print(f"Server: {response}")

    except Exception as e:
        print(f"[-]Error: {e}")

    finally:
        # Close the socket
        client_socket.close()
        print("[+]Disconnected from the server.")

if __name__ == "__main__":
    main()


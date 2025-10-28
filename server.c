#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8080

int main() {
    int server_fd, new_socket;
    char buffer[1024] = {0};
    char *msg = "Hello from server";
    struct sockaddr_in address;
    socklen_t addrlen = sizeof(address);

    // Create socket
    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd < 0) {
        perror("Socket creation failed");
        exit(1);
    }

    // Configure address
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // Bind socket to port
    if (bind(server_fd, (struct sockaddr*)&address, sizeof(address)) < 0) {
        perror("Bind failed");
        exit(1);
    }

    // Listen for client
    listen(server_fd, 1);

    // Accept connection
    new_socket = accept(server_fd, (struct sockaddr*)&address, &addrlen);
    if (new_socket < 0) {
        perror("Accept failed");
        exit(1);
    }

    // Read client message
    read(new_socket, buffer, sizeof(buffer));
    printf("Client: %s\n", buffer);

    // Send response
    send(new_socket, msg, strlen(msg), 0);
    printf("Server: %s\n", msg);

    close(new_socket);
    close(server_fd);
    return 0;
}

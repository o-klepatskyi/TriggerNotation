import socket
import datetime
import os

# Define the server listening address and port
server_host = "0.0.0.0"  # Listen on all available network interfaces
server_port = 12345  # Specify the same port number as used in the sender
log_file_path = os.path.join(os.getcwd(), "log.txt")

def receive_file():
    try:
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # Bind the socket to the specified address and port
            server_socket.bind((server_host, server_port))

            # Listen for incoming connections
            server_socket.listen()

            print("Waiting for incoming connections...")
            
            # Accept a connection from a client
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")

            # Open a local file for appending in binary mode

            with open(log_file_path, "ab") as file:
                # Write a log line with the current date and time
                log_line = f"\nReceived data at {datetime.datetime.now()}\n"
                file.write(log_line.encode())

                # Receive and write the file data in chunks
                while True:
                    data = client_socket.recv(1024)  # Receive 1 KB at a time
                    if not data:
                        break
                    file.write(data)

            print("File received and saved as 'received_file.txt'.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        receive_file()

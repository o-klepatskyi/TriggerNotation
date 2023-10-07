import socket
import os
import time

# Define the local file path and remote server details
local_file_path = os.path.join(os.getcwd(), "file.txt")
remote_host = "127.0.0.1"
remote_port = 12345  # Specify the desired port number
threshold_bytes = 16  # Specify the desired threshold in bytes

def send_file_to_remote(initial_size):
    
    # Create a TCP socket
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            # Connect to the remote server
            client_socket.connect((remote_host, remote_port))

            # Open the local file for reading in binary mode
            with open(local_file_path, "rb") as file:
                # Move the file pointer to the initial size
                file.seek(initial_size)

                # Read and send the file in chunks
                while True:
                    data = file.read(1024)  # Read 1 KB at a time
                    if not data:
                        break
                    client_socket.send(data)

            print(f"File sent to remote server with initial size: {initial_size} bytes.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Get the initial size of the file
    while not os.path.exists(local_file_path):
        print(f"Waiting for {local_file_path} to be created...")
        time.sleep(1)

    print(f"{local_file_path} has been created.")

    # Get the initial size of the file
    initial_size = os.path.getsize(local_file_path)

    while True:
        # Wait for 1 second
        time.sleep(1)

        # Get the current size of the file
        current_size = os.path.getsize(local_file_path)
        print(f"Current size of the file: {current_size} bytes")

        # Check if the difference in size is greater than 1 KB
        if abs(current_size - initial_size) > threshold_bytes:
            print(abs(current_size - initial_size))
            # Send the new information from the file via TCP
            send_file_to_remote(initial_size)

            # Update the initial size to the current size
            initial_size = current_size
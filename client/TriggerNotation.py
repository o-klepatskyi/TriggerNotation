import tkinter as tk
import tkinter.messagebox as messagebox

# Store the correct username and password as plaintext
correct_username = "user123"
correct_password = "pass123"

def show_message(message):
    messagebox.showinfo("Message", message)

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
window.geometry("300x170")

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

# Start the main event loop
window.mainloop()

import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    try:
        password_length = int(entry_length.get())
        if password_length < 6:
            messagebox.showwarning("Weak Password", "Password length should be at least 6 characters for better security.")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Setting up the UI window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Labels and entries
label_title = tk.Label(root, text="Random Password Generator", font=("Arial", 16))
label_title.pack(pady=10)

label_length = tk.Label(root, text="Enter Password Length:", font=("Arial", 12))
label_length.pack(pady=10)

entry_length = tk.Entry(root, font=("Arial", 12))
entry_length.pack(pady=5)

label_password = tk.Label(root, text="Generated Password:", font=("Arial", 12))
label_password.pack(pady=10)

entry_password = tk.Entry(root, font=("Arial", 12), width=30)
entry_password.pack(pady=5)

# Buttons
button_generate = tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password)
button_generate.pack(pady=10)

button_copy = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), command=copy_to_clipboard)
button_copy.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

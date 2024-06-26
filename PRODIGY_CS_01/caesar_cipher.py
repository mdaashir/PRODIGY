import tkinter as tk
from tkinter import messagebox
import pyperclip

def caesar_cipher(text, shift, direction):
    # Encrypt or decrypt text using Caesar Cipher.
    result = ""
    shift = shift % 26  # Ensure the shift is within the range of 0-25

    if direction == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Perform the shift
            offset = (ord(char) - start + shift) % 26
            result += chr(start + offset)
        else:
            # Non-alphabetic characters are not modified
            result += char

    return result

def log_history(text, shift, direction, result):
    # Log the encryption or decryption operation to history.txt.
    with open("history.txt", "a") as file:
        file.write(f"{direction.capitalize()} | Shift: {shift} | Input: {text} | Output: {result}\n")

def encrypt():
    # Handle the encryption process and update the GUI.
    text = text_entry.get()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return

    result = caesar_cipher(text, shift, "encrypt")
    log_history(text, shift, "encrypt", result)
    display_result("Encrypted Result: ", result)

    # Reset the input text and shift value
    text_entry.delete(0, tk.END)
    shift_entry.delete(0, tk.END)

def decrypt():
    # Handle the decryption process and update the GUI.
    text = text_entry.get()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return

    result = caesar_cipher(text, shift, "decrypt")
    log_history(text, shift, "decrypt", result)
    display_result("Decrypted Result: ", result)

    # Reset the input text and shift value
    text_entry.delete(0, tk.END)
    shift_entry.delete(0, tk.END)

def show_help():
    # Display the help information in a message box.
    help_text = """
    Caesar Cipher Tool

    This tool allows you to encrypt and decrypt text using the Caesar Cipher algorithm.

    Instructions:
    - Enter the text to process.
    - Enter the shift value (an integer).
    - Click Encrypt or Decrypt to perform the operation.

    The Caesar Cipher shifts each letter by the specified number of positions.
    Example: Encrypt "HELLO" with a shift of 3 -> "KHOOR".
             Decrypt "KHOOR" with a shift of 3 -> "HELLO".
    """
    messagebox.showinfo("Help", help_text)

def display_result(prefix, result):
    # Display the result with a prefix in the result label
    result_label.config(text=prefix, fg="#FFFFFF", font=("Arial", 12, "bold"))
    result_display.config(text=result, fg="#FFFFFF", font=("Arial", 12))
    # Show the copy button
    copy_button.grid()
    # Resize the window to fit the result text
    root.update_idletasks()  # Update the window to calculate the new size
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    root.geometry(f"{window_width}x{window_height}")

def copy_result():
    # Copy the result text to the clipboard
    result = result_display.cget("text")
    pyperclip.copy(result)
    messagebox.showinfo("Copied", "Text copied to clipboard.")
    copy_button.grid_remove() # Hide the copy button after copying

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("400x200")
root.configure(bg="#212121")  # Dark background
root.resizable(False, False)  # Make the window fixed

# Create and place the widgets
tk.Label(root, text="Enter Text:", bg="#212121", fg="#FFFFFF", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
text_entry = tk.Entry(root, width=20, bg="#424242", fg="#FFFFFF", font=("Arial", 12))  # Dark entry box
text_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Shift Value:", bg="#212121", fg="#FFFFFF", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
shift_entry = tk.Entry(root, width=10, bg="#424242", fg="#FFFFFF", font=("Arial", 12))  # Dark entry box
shift_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt, bg="#388E3C", fg="#FFFFFF", font=("Arial", 12, "bold"), padx=10)  # Dark green
encrypt_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt, bg="#1976D2", fg="#FFFFFF", font=("Arial", 12, "bold"), padx=10)  # Dark blue
decrypt_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

help_button = tk.Button(root, text="Help", command=show_help, bg="#FFA000", fg="#212121", font=("Arial", 12, "bold"), padx=10)  # Dark orange
help_button.grid(row=2, column=2, padx=10, pady=10, sticky="e")

copy_button = tk.Button(root, text="Copy", command=copy_result, bg="#616161", fg="#FFFFFF", font=("Arial", 12, "bold"), padx=10)  # Gray button
copy_button.grid(row=2, column=2, padx=10, pady=10, sticky="e")
copy_button.grid_remove()  # Hide the copy button initially

result_frame = tk.Frame(root, bg="#424242", bd=1, relief=tk.SOLID)  # Dark gray frame
result_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")

result_label = tk.Label(result_frame, text="", bg="#424242", fg="#FFFFFF", font=("Arial", 12, "bold"))  # Dark entry box
result_label.pack(padx=10, pady=5)

result_display = tk.Label(result_frame, text="", bg="#424242", fg="#FFFFFF", font=("Arial", 12), justify="left", anchor="nw", wraplength=200)
result_display.pack(padx=10, pady=5)

# Start the main event loop
root.mainloop()
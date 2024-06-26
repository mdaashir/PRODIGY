import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import os
import subprocess

output_image_path = ""  # Define output_image_path as a global variable

def encrypt_image(input_image_path, output_image_path, key):
    try:
        # Open the image
        image = Image.open(input_image_path)
        image_array = np.array(image)
        
        # Encrypt the image by adding the key to each pixel value
        encrypted_array = (image_array + (key % 256)) % 256
        
        # Create and save the encrypted image
        encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
        encrypted_image.save(output_image_path)
        
        # Log the action
        log_action("Encryption", input_image_path, output_image_path, key)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during encryption: {e}")
        return False

def decrypt_image(input_image_path, output_image_path, key):
    try:
        # Open the encrypted image
        image = Image.open(input_image_path)
        image_array = np.array(image)
        
        # Decrypt the image by subtracting the key from each pixel value
        decrypted_array = (image_array - (key % 256)) % 256
        
        # Create and save the decrypted image
        decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
        decrypted_image.save(output_image_path)
        
        # Log the action
        log_action("Decryption", input_image_path, output_image_path, key)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during decryption: {e}")
        return False

def generate_output_path(input_path, suffix):
    base, ext = os.path.splitext(input_path)
    return f"{base}_{suffix}{ext}"

def log_action(action, input_path, output_path, key):
    log_entry = f"{action} | Input: {input_path} | Output: {output_path} | Key: {key}\n"
    with open("history.txt", "a") as log_file:
        log_file.write(log_entry)

def encrypt():
    global output_image_path  # Declare the global variable

    input_image_path = input_entry.get()
    key = key_entry.get()
    if not key.isdigit():
        messagebox.showerror("Error", "Key must be a positive integer.")
        return
    key = int(key)

    output_image_path = generate_output_path(input_image_path, "encrypted")

    # Reset the input text and key value
    input_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)

    if encrypt_image(input_image_path, output_image_path, key):
        messagebox.showinfo("Success", f"Image encrypted and saved to {output_image_path}")
        view_button.grid()

def decrypt():
    global output_image_path  # Declare the global variable
    
    input_image_path = input_entry.get()
    key = key_entry.get()
    if not key.isdigit():
        messagebox.showerror("Error", "Key must be a positive integer.")
        return
    key = int(key)

    output_image_path = generate_output_path(input_image_path, "decrypted")

    # Reset the input text and key value
    input_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    
    if decrypt_image(input_image_path, output_image_path, key):
        messagebox.showinfo("Success", f"Image decrypted and saved to {output_image_path}")
        view_button.grid()

def browse_image():
    file_path = filedialog.askopenfilename()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def show_help():
    help_text = """
    Image Encryption/Decryption Tool

    This tool allows you to encrypt and decrypt images using a key.

    Instructions:
    1. Click Browse to select an image.
    2. Enter the encryption/decryption key (a positive integer).
    3. Click Encrypt to encrypt the image or Decrypt to decrypt it.

    Note:
    - Encrypted images will be saved with '_encrypted' suffix.
    - Decrypted images will be saved with '_decrypted' suffix.
    """
    messagebox.showinfo("Help", help_text)

def view_output():
    global output_image_path  # Declare the global variable

    try:
        subprocess.Popen(["xdg-open", output_image_path])  # Linux
    except:
        try:
            subprocess.Popen(["open", output_image_path])  # macOS
        except:
            subprocess.Popen(["start", output_image_path], shell=True)  # Windows
            

# Create the main window
root = tk.Tk()
root.title("Image Encryption/Decryption Tool")
root.resizable(False, False)  # Make the window fixed

# Create and place widgets
input_label = tk.Label(root, text="Input Image:", font=("Arial", 12))
input_label.grid(row=0, column=0, padx=5, pady=5)

input_entry = tk.Entry(root, width=40, font=("Arial", 12))
input_entry.grid(row=0, column=1, padx=5, pady=5)

browse_button = tk.Button(root, text="Browse", command=browse_image, font=("Arial", 12), bg="#2196F3", fg="#FFFFFF")
browse_button.grid(row=0, column=2, padx=5, pady=5)

key_label = tk.Label(root, text="Key:", font=("Arial", 12))
key_label.grid(row=1, column=0, padx=5, pady=5)

key_entry = tk.Entry(root, width=10, font=("Arial", 12))
key_entry.grid(row=1, column=1, padx=5, pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt, font=("Arial", 12), bg="#4CAF50", fg="#FFFFFF")
encrypt_button.grid(row=2, column=0, padx=5, pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt, font=("Arial", 12), bg="#FF5722", fg="#FFFFFF")
decrypt_button.grid(row=2, column=1, padx=5, pady=5)

help_button = tk.Button(root, text="Help", command=show_help, font=("Arial", 12), bg="#607D8B", fg="#FFFFFF")
help_button.grid(row=2, column=2, padx=5, pady=5)

view_button = tk.Button(root, text="View", command=view_output, font=("Arial", 12), bg="#673AB7", fg="#FFFFFF")
view_button.grid(row=1, column=2, padx=5, pady=5)
view_button.grid_remove()  # Hide the view button initially

# Start the main event loop
root.mainloop()

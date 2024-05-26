from PIL import Image
import numpy as np
import os

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
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

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
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

def generate_output_path(input_path, suffix):
    base, ext = os.path.splitext(input_path)
    return f"{base}_{suffix}{ext}"

def main():
    while True:
        print("Menu:")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            try:
                input_image_path = input("Enter the path of the image to encrypt: ")
                key = int(input("Enter the key for encryption (integer): "))
                output_image_path = generate_output_path(input_image_path, "encrypted")
                encrypt_image(input_image_path, output_image_path, key)
                print(f"Image encrypted and saved to {output_image_path}")
            except ValueError:
                print("Invalid key. Please enter an integer value.")
            except FileNotFoundError:
                print("The input file path is incorrect. Please check the file path.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                
        elif choice == '2':
            try:
                input_image_path = input("Enter the path of the image to decrypt: ")
                key = int(input("Enter the key for decryption (integer): "))
                output_image_path = generate_output_path(input_image_path, "decrypted")
                decrypt_image(input_image_path, output_image_path, key)
                print(f"Image decrypted and saved to {output_image_path}")
            except ValueError:
                print("Invalid key. Please enter an integer value.")
            except FileNotFoundError:
                print("The input file path is incorrect. Please check the file path.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == '__main__':
    main()

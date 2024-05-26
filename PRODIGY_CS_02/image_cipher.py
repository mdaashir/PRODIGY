from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    image = Image.open(input_image_path)
    image_array = np.array(image)
    
    # Encrypt the image by adding the key to each pixel value
    encrypted_array = (image_array + key) % 256
    
    # Create and save the encrypted image
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_image_path)

def main():
    # Define input and output paths
    input_image_path = 'birds.png'
    encrypted_image_path = 'encrypted_image.png'

    
    # Define a key for encryption/decryption
    key = 321
    
    # Encrypt the image
    encrypt_image(input_image_path, encrypted_image_path, key)
    print(f'Image encrypted and saved to {encrypted_image_path}')
    
if __name__ == '__main__':
    main()

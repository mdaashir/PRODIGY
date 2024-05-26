def caesar_cipher(text, shift, direction):
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

def display_help():
    help_text = """
    Caesar Cipher Program Help Menu

    This program allows you to encrypt and decrypt text using the Caesar Cipher algorithm.

    Options:
    1. Encrypt - Encrypts the provided text using the specified shift value.
    2. Decrypt - Decrypts the provided text using the specified shift value.
    3. Help    - Displays this help menu.
    4. Exit    - Exits the program.

    Instructions:
    - When prompted, choose an option by entering the corresponding number.
    - Enter the text you want to encrypt or decrypt.
    - Enter the shift value (an integer) to use for the Caesar Cipher.
    """
    print(help_text)

def main():
    while True:
        print("Caesar Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Help")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '4':
            break
        elif choice == '3':
            display_help()
            continue
        elif choice not in ['1', '2']:
            print("Invalid choice, please try again.\n")
            continue

        text = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value, please enter an integer.\n")
            continue

        if choice == '1':
            direction = "encrypt"
        elif choice == '2':
            direction = "decrypt"
        else:
            print("Invalid choice, please try again.")
            continue

        result = caesar_cipher(text, shift, direction)
        print(f"Result: {result}\n")

if __name__ == "__main__":
    main()
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

def main():
    while True:
        print("Caesar Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '3':
            break

        text = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))

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
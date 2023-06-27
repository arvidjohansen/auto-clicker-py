import keyboard

TRIGGER_KEY = 'right shift'
EMULATED_KEY = 'enter'
DEBUG = True

def on_trigger_key_release(event):
    if DEBUG:
        print(event.name)
    if event.name == TRIGGER_KEY:
        print(f'Pressing ' + EMULATED_KEY)
        keyboard.press(EMULATED_KEY)
        print(f'Releasing ' + EMULATED_KEY)
        keyboard.release(EMULATED_KEY)

keyboard.on_release(on_trigger_key_release)
keyboard.wait()


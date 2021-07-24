import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)
pin_list = [board.GP3, board.GP6, board.GP20, board.GP4, board.GP7, board.GP19, board.GP5, board.GP8, board.GP18]
btnList = []

def initialize_buttons():
    for i in pin_list:
        index = pin_list.index(i)
        print("Initializing pin ",i," with button",index + 1)
        btn = digitalio.DigitalInOut(i)
        btn.direction = digitalio.Direction.INPUT
        btn.pull = digitalio.Pull.DOWN
        btnList.append(btn)

def launch_app(searchtext):
    keyboard.press(Keycode.COMMAND, Keycode.SPACE)
    keyboard.release_all()
    layout.write(searchtext)
    time.sleep(0.3)
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()
    
def command_one():
    keyboard.press(Keycode.COMMAND, Keycode.ONE)
    keyboard.release_all()
    
def command_two():
    keyboard.press(Keycode.COMMAND, Keycode.TWO)
    keyboard.release_all()

initialize_buttons()


while True:
    for i in btnList:
        if i.value:
            btn = btnList.index(i) + 1
            print("Button ", btn , " pressed")
            
            if btn == 1:
                launch_app("outlook")
                
            if btn == 2:
                launch_app("teams")
                
            if btn == 3:
                command_one()
                
            if btn == 4:
                command_two()                
    time.sleep(0.1)


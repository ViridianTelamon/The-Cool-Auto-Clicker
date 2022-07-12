"""    
    Copyright (C) 2022 ViridianTelamon (Viridian)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


print("The Cool Auto Clicker")
print("\nBy:  ViridianTelamon.")
time.sleep(0.2)
start_stop_key_input = input("\nEnter A Start And Stop Key (Make Sure The Letter Is Lowercase):  ")
time.sleep(2)
exit_key_input = input("\nEnter An Exit Key (Make Sure The Letter Is Lowercase):  ")
time.sleep(0.2)
delay_input = float(input("\nEnter A Number For The Delay Between The Certain Mouse Button Clicks (It Can Be A Decimal If You Want Too):  "))
time.sleep(0.2)
mouse_input = input("\nEnter Either Left Or Right For The Mouse Button That You Want To Be Chosen:  ")
time.sleep(0.2)
print("\nSetup Is Complete!  Press The Start Or Stop Or Exit Button That You Chose To You The Autoclicker!")

mouse_input = mouse_input.lower()

if mouse_input=="left":
    mouse_input = Button.left
elif mouse_input=="right":
    mouse_input = Button.right

delay = delay_input
button = mouse_input
start_stop_key = KeyCode(char=start_stop_key_input)
exit_key = KeyCode(char=exit_key_input)


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()

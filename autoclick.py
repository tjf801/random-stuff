import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 1
button = Button.right
start_stop_key = KeyCode(char='v')
exit_key = KeyCode(char='b')

class ClickMouse(threading.Thread):
	def __init__(self, delay, button):
		super().__init__()
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
			if self.running:
				mouse.press(self.button)
				mouse.release(self.button)
				time.sleep(self.delay)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
	if key == start_stop_key:
		if click_thread.running:
			click_thread.stop_clicking()
			print("Stopped")
			mouse.release(button)
		else:
			click_thread.start_clicking()
			print("Started")
	elif key == exit_key:
		click_thread.exit()
		listener.stop()

with Listener(on_press=on_press) as listener:
	listener.join()

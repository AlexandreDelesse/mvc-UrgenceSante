import RPi.GPIO as GPIO
import threading, time

class Buzzer:
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	BUZZER = 23
	GPIO.setup(BUZZER, GPIO.OUT)

	def __init__(self):
		self.buzzer_thread = threading.Thread(target=self.buzzer_pattern)

	def buzzer_pattern(self):
		print("buzzer start")
		GPIO.output(self.BUZZER, True)
		time.sleep(0.5)
		GPIO.output(self.BUZZER, False)
		time.sleep(0.5)
		GPIO.output(self.BUZZER, True)
		time.sleep(0.5)
		GPIO.output(self.BUZZER, False)
		print("buzzer stop")

	def start_buzzer(self):
		self.buzzer_thread.start()
		

	

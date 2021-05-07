import RPi.GPIO as GPIO
import threading, time

class Buzzer:
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	BUZZER = 23
	GPIO.setup(BUZZER, GPIO.OUT)

	def __init__(self):
		pass		

	def buzzerPattern(self):
		print("buzzer start")
		GPIO.output(self.BUZZER, True)
		time.sleep(1)
		GPIO.output(self.BUZZER, False)		
		print("buzzer stop")

	def startBuzzer(self):
		self.buzzerPattern()

	def stopBuzzer(self):
		GPIO.cleanup()

	def __del__(self):
		GPIO.cleanup()
		

	

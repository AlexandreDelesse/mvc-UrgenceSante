from model import Model
from view import View
from buzzer import Buzzer
from persistance import Persistance
import threading

class Controller:
	
	MAX_TEMPERATURE = 21
	MIN_TEMPERATURE = 19
	ALARME_ON = "activée"
	ALARME_OFF = "desactivée"
	alarme = True

	def __init__(self):
		self.model = Model()
		self.view = View(self)
		self.persistance = Persistance()
		self.bt_thread = threading.Thread(target=self.display_bluetooth_value)
		self.view.alarme_var.set(self.ALARME_ON)
		self.buzzer = Buzzer()
		

	def main(self):
		self.bt_thread.start()
		self.view.main()

	def display_bluetooth_value(self):
		while(1):
			result = self.model.get_bluetooth_value()
			self.view.value_var.set(str(result) + " °C")
			self.persistance.write_in_file(result)


	def on_off_alarme(self):
		if (self.alarme == True):
			self.alarme = False
			self.view.alarme_var.set(self.ALARME_OFF)
			print("alarme OFF")
		else:
			self.alarme = True
			self.view.alarme_var.set(self.ALARME_ON)
			print("alarme ON")

if __name__== '__main__':
	app = Controller()
	app.main()

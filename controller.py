from beacon import Beacon
from view import View
from buzzer import Buzzer
from persistance import Persistance
import threading, time

class Controller:
	
	MAX_TEMPERATURE = 21
	MIN_TEMPERATURE = 19
	ALARME_ON = "activée"
	ALARME_OFF = "desactivée"
	alarme = True

	def __init__(self):
		self.beacon = Beacon()
		self.view = View(self)
		self.persistance = Persistance()
		self.bt_thread = threading.Thread(target=self.refreshDataInView)
		self.view.alarme_var.set(self.ALARME_ON)
		self.buzzer = Buzzer()
		

	def main(self):
		self.bt_thread.start()
		self.view.main()

	def refreshDataInView(self):
		while(1):
			self.beacon.refreshTemperature()
			temperature = self.beacon.getTemperature()
			temperatureTime = self.beacon.getTemperatureTime()
			beaconName = self.beacon.getBeaconName()

			self.view.value_var.set(str(temperature) + " °C")
			self.persistance.write_in_file(beaconName, temperatureTime, temperature)

			time.sleep(5)


	def on_off_alarme(self):
		if (self.beacon.isAlarmeActivated == True):
			self.beacon.isAlarmeActivated = False
			self.view.alarme_var.set(self.ALARME_OFF)
			print("alarme OFF")
		else:
			self.beacon.isAlarmeActivated = True
			self.view.alarme_var.set(self.ALARME_ON)
			print("alarme ON")

if __name__== '__main__':
	app = Controller()
	app.main()





	

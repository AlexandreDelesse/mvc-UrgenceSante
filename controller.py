from beacon import Beacon
from view import View
from buzzer import Buzzer
import threading, time

class Controller:
	stopAllThread = False
	def __init__(self):
		self.beacon = Beacon()
		self.view = View(self)
		self.bluetoothThread = threading.Thread(target=self.refreshDataInView)
		self.alarmeThread = threading.Thread(target = self.manageAlarme)
		self.buzzer = Buzzer()
		

	def main(self):
		self.initViewFromBeacon()
		self.bluetoothThread.start()
		self.alarmeThread.start()
		self.view.main()
		self.stopAllThread = True


	def initViewFromBeacon(self):
		self.view.temperatureVar.set(self.beacon.temperature)
		self.view.alarmeVar.set(self.beacon.alarmeStatus)

	def refreshDataInView(self):
		while(self.stopAllThread == False):
			self.beacon.refreshTemperature()
			temperature = self.beacon.getTemperature()
			self.view.temperatureVar.set(str(temperature) + " °C")
			
			time.sleep(5)


	def on_off_alarme(self):
		self.beacon.switchAlarmeStatus()
		self.view.alarmeVar.set(self.beacon.alarmeStatus)
	
	def manageAlarme(self):
		while(self.stopAllThread == False):
			if(self.beacon.alarmeStatus == "ON" and self.beacon.isAlarmeActivated == True):
				self.buzzer.startBuzzer()
			time.sleep(1.5)	


if __name__== '__main__':
	app = Controller()
	app.main()	
	print("merci au revoir")





	

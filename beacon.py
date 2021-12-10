from bluepy.btle import Scanner
from TagTemperature import TagTemperature
from datetime import datetime
from persistance import Persistance


class Beacon:

	SEARCH_TIME = 5.0

	def __init__(self):
		self.macAddress = "e7:4f:89:d8:1e:75"
		self.beaconName = "CT801"
		self.temperature = None
		self.temperatureTime = ""
		self.temperatureLimitMax = 21
		self.temperatureLimitMin = 19
		self.alarmeStatus = "ON"
		self.isAlarmeActivated = False

		self.persistance = Persistance()

	def getMacAddress(self):
		return self.macAdress

	def getBeaconName(self):
		return self.beaconName

	def getTemperature(self):
		return self.temperature

	def getAlarmeStatus(self):
		return self.alarmeStatus

	def getTemperatureTime(self):
		return self.temperatureTime

	def refreshTemperature(self):
		scanner = Scanner()
		devices = scanner.scan(self.SEARCH_TIME)
		for device in devices:
			if(device.addr == self.macAddress):
				date = datetime.now()
				self.temperatureTime = date
				self.temperature = TagTemperature(device.rawData).formattedDataSensor
				print(f"temperature: {self.temperature}, time: {self.temperatureTime}")
				self.persistance.writeInFile(self.beaconName, self.temperatureTime, self.temperature)
				if (self.temperature > self.temperatureLimitMax or self.temperature < self.temperatureLimitMin):
					print("alarme on")
					self.isAlarmeActivated = True
				else:
					print("alarme off")
					self.isAlarmeActivated = False
	
	def switchAlarmeStatus(self):
		if (self.alarmeStatus == "ON"):
			self.alarmeStatus = "OFF"
			print("alarme desactivée")
		else:
			self.alarmeStatus = "ON"
			print("alarme activée")


	

	

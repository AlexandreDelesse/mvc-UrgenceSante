from bluepy.btle import Scanner
from TagTemperature import TagTemperature
import threading


class Bluetooth:

	SEARCH_TIME = 5.0
	
	def __init__(self):
		self.temperature = "none"
		self.mac_address = "e7:4f:89:d8:1e:75"
	
	def scan_bluetooth(self):
		scanner = Scanner()
		devices = scanner.scan(self.SEARCH_TIME)
		for device in devices:
			if(device.addr == self.mac_address):
				print("trouvé :)")
				self.temperature = TagTemperature(device.rawData).formattedDataSensor

	def get_temperature(self):
		self.scan_bluetooth()
		return self.temperature
		
		

	
	

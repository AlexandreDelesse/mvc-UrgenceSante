from bluetooth import Bluetooth

class Model:

	def __init__(self):
		self.bt_value = 0
		self.bluetooth = Bluetooth()


	def get_bluetooth_value(self):
		result = self.bluetooth.get_temperature()
		self.bt_value = result
		return  self.bt_value

	
		
		

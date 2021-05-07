import os.path
from datetime import datetime
import csv

class Persistance:
	def __init__(self):
		self.path = "/home/pi/Documents/dev/mvc_us_temperature/sauvegardes/"
	
	def writeInFile(self, beaconName, temperatureTime, temperature):
		date = datetime.now()
		date_mod = date.strftime("%d_%m_%Y.csv")

		if (os.path.exists(self.path + beaconName + "_" + date_mod)):
			print("fichier existe") 
		else:
			with open(self.path + beaconName + "_" + date_mod, 'a') as csvfile:
				newwriter = csv.writer(csvfile)
				newwriter.writerow(['nom', 'date_heure', 'temperature'])
		c = csv.writer(open(self.path + beaconName + "_" + date_mod, "a"))
		c.writerow([beaconName, temperatureTime , temperature])






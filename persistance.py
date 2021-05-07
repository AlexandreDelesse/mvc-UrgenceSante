import os.path
from datetime import datetime
import csv

class Persistance:
	def __init__(self):
		pass
	
	def writeInFile(self, beaconName, temperatureTime, temperature):
		date = datetime.now()
		date_mod = date.strftime("%d_%m_%Y.csv")

		if (os.path.exists("./sauvegardes/" + beaconName + "_" + date_mod)):
			print("fichier existe") 
		else:
			with open("./sauvegardes/" + beaconName + "_" + date_mod, 'a') as csvfile:
				newwriter = csv.writer(csvfile)
				newwriter.writerow(['nom', 'date_heure', 'temperature'])
		c = csv.writer(open("./sauvegardes/" + beaconName + "_" + date_mod, "a"))
		c.writerow([beaconName, temperatureTime , temperature])






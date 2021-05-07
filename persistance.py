import os.path
from datetime import datetime
import csv

class Persistance:
	def __init__(self):
		pass
	
	def write_in_file(self, value):
		date = datetime.now()
		date_mod = date.strftime("%d_%m_%Y.csv")

		if (os.path.exists("./sauvegardes/" + date_mod)):
			print("fichier existe") 
		else:
			with open("./sauvegardes/" + date_mod, 'a') as csvfile:
				newwriter = csv.writer(csvfile)
				newwriter.writerow(['nom', 'date_heure', 'temperature'])
		c = csv.writer(open("./sauvegardes/" + date_mod, "a"))
		c.writerow(['CT 801', date , value])

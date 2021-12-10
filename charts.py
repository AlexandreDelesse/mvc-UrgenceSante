import matplotlib.pyplot as plt
import numpy as np

class Charts:
	def __init__(self):
		pass

	def makeGraph(self):
		temperature = np.random(10, 10, 10)
		plt.plot(temperature, 50)
		plt.show()

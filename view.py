import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
	PAD = 10
	BG_COLOR = '#F09837'
	ALARME_ON = "activée"
	ALARME_OFF = "desactivée"

	def __init__(self, controller):
		super().__init__()
		self.controller = controller

		self.title('us_mvc.0')
		#self.config(background=self.BG_COLOR)
		self.attributes('-fullscreen', True)

		self.temperatureVar = tk.StringVar()
		self.alarmeVar = tk.StringVar()
		#self.temperatureVar2 = tk.StringVar()

		self._make_main_frame()
		self._make_temp_display(self.temperatureVar)
		#self._make_temp_display(self.temperatureVar2)
		self._make_button("Alarme : ",self.controller.on_off_alarme)
		#self._make_button("graph" ,self.controller.traceGraph)


	def main(self):
		self.mainloop()

	def _make_main_frame(self):
		self.main_frm = ttk.Frame(self)
		self.main_frm.pack(padx=self.PAD, pady=self.PAD)

	def _make_temp_display(self, textVar):
		frm = tk.Frame(self.main_frm)
		frm.pack()
		value_lbl = tk.Label(frm, textvariable=textVar, font=("Courrier", 40))
		label_lbl = tk.Label(frm, text = "Temperature : ", font=("Courrier", 30))
		value_lbl.pack(side = tk.RIGHT)
		label_lbl.pack(side = tk.RIGHT)

	def _make_button(self, text, function):
		frm = tk.Frame(self)
		frm.pack()
		btn_lbl = tk.Label(frm, text=text, font=("Courrier", 30))
		btn = tk.Button(frm, textvariable=self.alarmeVar, command=function , font=("Courrier", 30))
		btn_lbl.pack(side = tk.LEFT)		
		btn.pack(side = tk.LEFT)

		
	







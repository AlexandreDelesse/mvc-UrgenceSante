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
		#self.attributes('-fullscreen', True)

		self.temperatureVar = tk.StringVar()
		self.alarmeVar = tk.StringVar()

		self._make_main_frame()
		self._make_temp_display()
		self._make_button()


	def main(self):
		self.mainloop()

	def _make_main_frame(self):
		self.main_frm = ttk.Frame(self)
		self.main_frm.pack(padx=self.PAD, pady=self.PAD)

	def _make_temp_display(self):
		value_lbl = tk.Label(self.main_frm, textvariable=self.temperatureVar, font=("Courrier", 40))
		label_lbl = tk.Label(self.main_frm, text = "Temperature : ", font=("Courrier", 30))
		value_lbl.pack(side = tk.RIGHT)
		label_lbl.pack(side = tk.RIGHT)

	def _make_button(self):
		frm = tk.Frame(self)
		frm.pack()
		btn_lbl = tk.Label(frm, text="Alarme : ", font=("Courrier", 30))
		btn = tk.Button(frm, textvariable=self.alarmeVar, command=self.controller.on_off_alarme , font=("Courrier", 30))
		btn_lbl.pack(side = tk.LEFT)		
		btn.pack(side = tk.LEFT)
		
	







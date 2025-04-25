import sqlite3
from pathlib import Path
from tkinter import Tk, Spinbox
import tkinter as tkinterlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import get_data

class FeinstaubGUI(Tk):

    def __init__(self):
        super().__init__()
        self.default_column = "temperature"
        self.default_sensor = "dht22_metric"
        self.default_value = "MAX"
        self.default_startdate = "01-01"
        self.default_enddate = "31-12"
        
        self.load_window()
        self.create_ueberschrift()
        self.load_layout()
        
        
        get_data.get_plot_data_in_tkinter(self.plot_frame, self.default_sensor, self.default_column, self.default_startdate,self.default_enddate)
        self.default_wert = get_data.get_Value_from_DB(self.default_value, self.default_sensor, self.default_column ,self.default_startdate, self.default_enddate)
        # self.select_date()


    def load_window(self):
        self.geometry("1000x1000")
        self.title("Feinstaubprojekt")

    def set_Value(self,value:str):
        if value == 1:
            self.default_value = "MAX"
        if value == 2:
            self.default_value = "MIN"
        if value == 3:
            self.default_value = "AVG"

    def set_column_sensor(option:int):
        column = []

    def create_ueberschrift(self):
        ueberschrift = tkinterlib.Label(self, text= "Feinstaubprojekt", font=('Arial',18))
        ueberschrift.pack(padx=20,pady=40)

    def load_layout(self):
        self.buttonframe = tkinterlib.Frame()
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)

        self.button1= tkinterlib.Button(self.buttonframe,text="Temperatur", font=('Arial', 18))
        self.button1.grid(row=0,column=0,sticky=tkinterlib.W+tkinterlib.E)

        self.button2= tkinterlib.Button(self.buttonframe,text="Humidity", font=('Arial', 18))
        self.button2.grid(row=0,column=1,sticky=tkinterlib.W+tkinterlib.E)

        self.button3= tkinterlib.Button(self.buttonframe,text="P1", font=('Arial', 18))
        self.button3.grid(row=0,column=2,sticky=tkinterlib.W+tkinterlib.E)

        self.button4= tkinterlib.Button(self.buttonframe,text="P2", font=('Arial', 18))
        self.button4.grid(row=0,column=3,sticky=tkinterlib.W+tkinterlib.E)

        self.button5= tkinterlib.Button(self.buttonframe,text="MAX", font=('Arial', 18))
        self.button5.grid(row=1, column=1, sticky=tkinterlib.W+tkinterlib.E)

        self.button6= tkinterlib.Button(self.buttonframe,text="MIN", font=('Arial', 18))
        self.button6.grid(row=1, column=2, sticky=tkinterlib.W+tkinterlib.E)

        self.button7= tkinterlib.Button(self.buttonframe,text="AVG", font=('Arial', 18))
        self.button7.grid(row=1, column=3, sticky=tkinterlib.W+tkinterlib.E)
        self.buttonframe.pack(fill='x')

        self.plot_frame = tkinterlib.Frame(self)
        self.plot_frame.pack(fill='both', expand=True)

    def select_date(self):
        # dayselect = tkinterlib.Spinbox(self, from_=1,to=100)
        # dayselect.pack(padx=20,pady=20)

        # monthselect = tkinterlib.Spinbox(self, from_=1, to=12)
        # monthselect.pack(padx=20,pady=20)
        day_options= []
        month_options = []

        for i in range(1,32):
            day_options.append(str(i))

        for i in range(1,13):
            month_options.append(str(i))


        selected_option = tkinterlib.StringVar(self)
        selected_option.set



if __name__ == "__main__":

    app = FeinstaubGUI()
    app.mainloop()
from pathlib import Path
from tkinter import Tk
import tkinter as tkinterlib
from modules.GUI import get_data, select_date
from modules.GUI import select_date

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

        select_date.create_date_selectors(self)  # Ruft die Datumsauswahl auf
        
        # Initiales Plot und Wert aus der DB laden
        self.update_gui()

    def load_window(self):
        self.geometry("1000x1000")
        self.title("Feinstaubprojekt")

    def set_Value(self, value: str):
        """Setzt den Wert des Feinstaubs (MAX, MIN, AVG)"""
        if value in ["MAX", "MIN", "AVG"]:
            self.default_value = value
        else:
            print("Ungültiger Wert:", value)

    def create_ueberschrift(self):
        ueberschrift = tkinterlib.Label(self, text="Feinstaubprojekt", font=('Arial', 18))
        ueberschrift.pack(padx=20, pady=40)

    def load_layout(self):
        """Lädt die Layout-Komponenten und Buttons"""
        self.buttonframe = tkinterlib.Frame(self)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)

        # Buttons für Temperatur, Luftfeuchtigkeit etc.
        self.button1 = tkinterlib.Button(self.buttonframe, text="Temperatur", font=('Arial', 18),
                                        command=lambda: self.set_Sensor_and_Column("dht22_metric", "temperature"))
        self.button1.grid(row=0, column=0, sticky=tkinterlib.W + tkinterlib.E)

        self.button2 = tkinterlib.Button(self.buttonframe, text="Humidity", font=('Arial', 18),
                                        command=lambda: self.set_Sensor_and_Column("dht22_metric", "humidity"))
        self.button2.grid(row=0, column=1, sticky=tkinterlib.W + tkinterlib.E)

        self.button3 = tkinterlib.Button(self.buttonframe, text="P1", font=('Arial', 18),
                                        command=lambda: self.set_Sensor_and_Column("sds011_metric", "P1"))
        self.button3.grid(row=0, column=2, sticky=tkinterlib.W + tkinterlib.E)

        self.button4 = tkinterlib.Button(self.buttonframe, text="P2", font=('Arial', 18),
                                        command=lambda: self.set_Sensor_and_Column("sds011_metric", "P2"))
        self.button4.grid(row=0, column=3, sticky=tkinterlib.W + tkinterlib.E)


        self.button5 = tkinterlib.Button(self.buttonframe, text="MAX", font=('Arial', 18), command=lambda: self.set_Value("MAX"))
        self.button5.grid(row=1, column=1, sticky=tkinterlib.W + tkinterlib.E)

        self.button6 = tkinterlib.Button(self.buttonframe, text="MIN", font=('Arial', 18), command=lambda: self.set_Value("MIN"))
        self.button6.grid(row=1, column=2, sticky=tkinterlib.W + tkinterlib.E)

        self.button7 = tkinterlib.Button(self.buttonframe, text="AVG", font=('Arial', 18), command=lambda: self.set_Value("AVG"))
        self.button7.grid(row=1, column=3, sticky=tkinterlib.W + tkinterlib.E)

        # Buttons für die Anzeige der Werte unter MAX, MIN, AVG
        self.max_value_button = tkinterlib.Button(self.buttonframe, text="MAX Wert", font=('Arial', 18))
        self.max_value_button.grid(row=2, column=1, sticky=tkinterlib.W + tkinterlib.E)

        self.min_value_button = tkinterlib.Button(self.buttonframe, text="MIN Wert", font=('Arial', 18))
        self.min_value_button.grid(row=2, column=2, sticky=tkinterlib.W + tkinterlib.E)

        self.avg_value_button = tkinterlib.Button(self.buttonframe, text="AVG Wert", font=('Arial', 18))
        self.avg_value_button.grid(row=2, column=3, sticky=tkinterlib.W + tkinterlib.E)

        self.buttonframe.pack(fill='x')

        self.update_button = tkinterlib.Button(self, text="Aktualisieren", font=('Arial', 18), command=self.update_gui)
        self.update_button.pack(pady=20)

        self.plot_frame = tkinterlib.Frame(self)
        self.plot_frame.pack(fill='both', expand=True)

    def set_Sensor_and_Column(self, sensor: str, column: str):
        """Setzt Sensor und Column und aktualisiert die GUI"""
        self.default_sensor = sensor
        self.default_column = column
        self.update_gui()



    def update_gui(self):
        """Aktualisiert die GUI mit neuen Daten und Plot"""
        # Alte Graphen entfernen
        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        # Ausgabe der aktuellen Daten
        print(f"Aktualisiertes Startdatum: {self.default_startdate}")
        print(f"Aktualisiertes Enddatum: {self.default_enddate}")
        print(f"Aktualisierter Wert: {self.default_value}")
        

        # Den neuen Plot zeichnen
        get_data.get_plot_data_in_tkinter(self.plot_frame, self.default_sensor, self.default_column, self.default_startdate, self.default_enddate)
        self.default_wert = get_data.get_Value_from_DB(self.default_value, self.default_sensor, self.default_column, self.default_startdate, self.default_enddate)

        # MAX, MIN und AVG Werte aus der DB holen und in den Buttons anzeigen
        max_value = get_data.get_Value_from_DB("MAX", self.default_sensor, self.default_column, self.default_startdate, self.default_enddate)
        min_value = get_data.get_Value_from_DB("MIN", self.default_sensor, self.default_column, self.default_startdate, self.default_enddate)
        avg_value = get_data.get_Value_from_DB("AVG", self.default_sensor, self.default_column, self.default_startdate, self.default_enddate)

        # Setze die Texte der Buttons
        self.max_value_button.config(text=f"MAX Wert: {max_value}")
        self.min_value_button.config(text=f"MIN Wert: {min_value}")
        self.avg_value_button.config(text=f"AVG Wert: {avg_value}")

if __name__ == "__main__":
    app = FeinstaubGUI()
    app.mainloop()

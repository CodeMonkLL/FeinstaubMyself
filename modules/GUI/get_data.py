import sqlite3;
from pathlib import Path
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt

def get_plot_data_in_tkinter(plot_frame,sensor: str, column: str, startDate: str, endDate: str):
        conn = sqlite3.connect(Path(__file__).parent.parent.parent / 'feinstaub.db')
        cursor = conn.cursor()

        query = f"""
        SELECT timestamp, {column}
        FROM {sensor}
        WHERE timestamp BETWEEN '2022-{startDate}T00:00:00' AND '2022-{endDate}T23:59:59'
        ORDER BY timestamp
        """
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()

        if not results:
            print("Keine Daten gefunden.")
            return

        sample_rate = 100
        x_values = [row[0] for i, row in enumerate(results) if i % sample_rate == 0]
        y_values = [row[1] for i, row in enumerate(results) if i % sample_rate == 0]

        timestamps = [row[0] for row in results]
       
        
        tick_dates = [timestamps[0], timestamps[-1]]

        # Matplotlib-Figur erstellen
        fig = Figure(figsize=(6, 3),dpi=100) #Hauptobjekt der Zeichnung
        ax = fig.add_subplot(1, 1, 1) #Achsenbereich auf Zeichnung
        ax.plot(x_values, y_values) #Koordinatensystem gefüllt mit den Werten
        ax.set_xticks(tick_dates)
        ax.set_title(f"{column} von {startDate} bis {endDate}")
        ax.set_xlabel("Zeit")
        ax.set_ylabel(column)
        plt.xticks(rotation=45)

        # Canvas für Tkinter
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)



def get_Value_from_DB(value:str, sensor:str, column:str, startDate: str, endDate:str):
    conn = sqlite3.connect(Path(__file__).parent.parent.parent/'feinstaub.db')

    cursor = conn.cursor()

    cursor.execute(f"SELECT {value}({column}) FROM {sensor} WHERE timestamp BETWEEN '2022-{startDate}T00:00:00' AND '2022-{endDate}T23:59:59'")

    wert = cursor.fetchone()

    return wert
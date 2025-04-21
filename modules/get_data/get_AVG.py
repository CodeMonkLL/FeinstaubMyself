import sqlite3;
from pathlib import Path;

def getAVGfrom(sensor:str, column:str, startDate: str, endDate:str):
    conn = sqlite3.connect(Path(__file__).parent.parent.parent/'feinstaub.db')
    
    cursor = conn.cursor()

    cursor.execute(f"SELECT MAX({column}) FROM {sensor} WHERE timestamp BETWEEN '2022-{startDate}T00:00:00' AND '2022-{endDate}T23:59:59'")

    average = cursor.fetchone()

    if average:
        print(f"Durschnittswert in der Spalte {column}: {average[0]}")
        print(f"Im Zeitraum von {startDate} bis {endDate}")
    else: print("Keine Daten für den Zeitraum gefunden")


if __name__ == "__main__":
    getAVGfrom("sds011_metric", "P2", "02-01", "02-15")
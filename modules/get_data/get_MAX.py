import sqlite3;
from pathlib import Path;

def getMAXfrom(sensor:str, column:str, startDate: str, endDate:str):
    conn = sqlite3.connect(Path(__file__).parent.parent.parent/'feinstaub.db')




    cursor = conn.cursor()

    cursor.execute(f"SELECT MAX({column}) FROM {sensor} WHERE timestamp BETWEEN '2022-{startDate}T00:00:00' AND '2022-{endDate}T23:59:59'")

    max = cursor.fetchone()

    if max:
        print(f"Maximaler Wert in der Spalte {column}: {max[0]}")
    else: print("Keine Daten gefunden")
















if __name__ == "__main__":
    getMAXfrom("sds011_metric", "P2", "02-01", "02-15")
    
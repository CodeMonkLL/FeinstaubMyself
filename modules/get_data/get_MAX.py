import sqlite3;
from pathlib import Path;

def getMAXfrom(sensor, column:str):
    conn = sqlite3.connect(Path(__file__).parent.parent.parent/'feinstaub.db')

    cursor = conn.cursor()

    cursor.execute(f"SELECT MAX({column}) FROM {sensor}")

    max = cursor.fetchone()

    if max:
        print(f"Maximaler Wert in der Spalte {column}: {max[0]}")
    else: print("Keine Daten gefunden")

if __name__ == "__main__":
    getMAXfrom("sds011_metric", "P1")
    
import sqlite3;
from pathlib import Path;

def getMINfrom(sensor,column:str):
    conn = sqlite3.connect(Path(__file__).parent.parent.parent/'feinstaub.db')
    
    cursor = conn.cursor()

    cursor.execute(f"SELECT MIN({column}) FROM {sensor}")

    min = cursor.fetchone()

    if min:
        print(f"Maximaler Wert in der Spalte {column}: {min[0]}")
    else: print("Keine Daten gefunden")


if __name__ == "__main__":
    getMINfrom("sds011_metric", "P1")
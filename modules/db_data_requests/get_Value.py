import sqlite3;
from pathlib import Path;

def get_Value_from_DB(value:str, sensor:str, column:str, startDate: str, endDate:str):
    conn = sqlite3.connect(Path(__file__).parent.parent.parent/'feinstaub.db')

    cursor = conn.cursor()

    cursor.execute(f"SELECT {value}({column}) FROM {sensor} WHERE timestamp BETWEEN '2022-{startDate}T00:00:00' AND '2022-{endDate}T23:59:59'")

    wert = cursor.fetchone()

    if not wert:
        print(f"Daten für den Zeitraum von {startDate} bis {endDate} nicht gefunden")
        return
    
    if value == "MAX":
        print(f"Maximaler Wert in der Spalte {column}: {wert[0]}")
        print(f"Im Zeitraum von 2022-{startDate} bis 2022-{endDate}")

    elif value == "MIN":
        print(f"Minmaler Wert in der Spalte {column}: {wert[0]}")
        print(f"Im Zeitraum von 2022-{startDate} bis 2022-{endDate}")

    elif value == "AVG":
        print(f"Durchschnittlicher Wert in der Spalte {column}: {wert[0]}")
        print(f"Im Zeitraum von 2022-{startDate} bis 2022-{endDate}")

    else:
        print(f"Unbekannter Wertetyp: {value}")
        return




if __name__ == "__main__":
    get_Value_from_DB("MAX","dht22_metric", "temperature", "01-01", "01-15")
    
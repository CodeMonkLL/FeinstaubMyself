# services/create_db_tables.py

import sqlite3
from pathlib import Path

# Pfad zur Datenbank (eine Ebene über dem Ordner 'services')
DB_PATH = Path(__file__).parent.parent/"feinstaub.db"

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Tabelle für DHT22-Messwerte
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dht22_metric (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id TEXT,
            sensor_type TEXT,
            location TEXT,
            lat REAL,
            lon REAL,
            timestamp TEXT,
            p1 REAL,
            dur_p1 REAL,
            ratio_p1 REAL,
            dur_p2 REAL,
            ratio_p2 REAL
        )
    ''')

    # Tabelle für SDS011-Messwerte
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sds011_metric (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id TEXT,
            sensor_type TEXT,
            location TEXT,
            lat REAL,
            lon REAL,
            timestamp TEXT,
            temperature REAL,
            humidity REAL
        )
    ''')

    conn.commit()
    conn.close()
    print("Datenbank und Tabellen wurden erfolgreich erstellt.")

if __name__ == "__main__":
    create_tables()

from pathlib import Path
import sqlite3
import download_csv

#Convert CSV data in a DB
#Kade due CSV-Daten für das Jahr 2022 herunter und 
#importiere sie in eine SQLite-Datenbank. Prüfe ggf. den korrekten
#Import leerer EInträge als NULL-Werte.
#Basispfad
base_path = Path(__file__)

#SQLite-Datenbankverbindung
conn = sqlite3.connect('feinstaub.db')
cur = conn.cursor()

def migrate_csv_to_db():
    #CSV-Dateien herunterladen
    download_csv.download_csv_files()

    #CSV-Dateien in die SQLite-Datenbank importieren
    for csv_file in base_path.glob("*.csv"):
        issds = csv_file.name.__contains__("sds011")
        with open(csv_file, 'r') as file:
            next(file)  # Skip header row
            if issds:
                for line in file:
                    data = line.strip().split(',')
                    cur.execute("INSERT INTO sds011_metric (sensor_id,sensor_type,location,lat,lon,timestamp,P1,durP1,ratioP1,P2,durP2,ratioP2) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11]))
            else:
                for line in file:
                    data = line.strip().split(',')
                    cur.execute("INSERT INTO dht22_metric (sensor_id;sensor_type;location;lat;lon;timestamp;temperature;humidity) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))

    conn.commit()
    print("CSV-Dateien erfolgreich in die Datenbank importiert.")


#Datenbankverbindung schließen
conn.close()

#Convert soll die csv-Dateien in die Feinstaub.db importieren/migrieren
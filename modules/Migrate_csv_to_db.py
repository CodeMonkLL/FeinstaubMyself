from pathlib import Path
import sqlite3

#Basispfad
base_path = Path(__file__).parent.parent/'csv' 

def migrate_csv_to_db():
    #SQLite-Datenbankverbindung
    conn = sqlite3.connect('feinstaub.db')
    cur = conn.cursor()

    print("Starte den Import der CSV-Dateien in die Datenbank...")
    #CSV-Dateien in die SQLite-Datenbank importieren
    #print(base_path)
    for csv_file in base_path.glob("*.csv"):
        print( f"Importiere {csv_file.name} in die Datenbank...")
        issds = csv_file.name.__contains__("sds011")
        with open(csv_file, 'r') as file:
            #print(file)
            next(file)  # Skip header row
            if issds:
                for line in file:
                    print(line)
                    data = line.strip().split(';')
                    cur.execute("INSERT INTO sds011_metric (sensor_id,sensor_type,location,lat,lon,timestamp,P1,durP1,ratioP1,P2,durP2,ratioP2) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11]))
            else:
                for line in file:
                    print(line)
                    data = line.strip().split(';')
                    #print("INSERT INTO dht22_metric (sensor_id,sensor_type,location,lat,lon,timestamp,temperature,humidity) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (int(data[0]), data[1], data[2], float(data[3]), float(data[4]), data[5], float(data[6]), float(data[7])))
                    cur.execute("INSERT INTO dht22_metric (sensor_id,sensor_type,location,lat,lon,timestamp,temperature,humidity) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (int(data[0]), data[1], data[2], float(data[3]), float(data[4]), data[5], float(data[6]), float(data[7])))
    
    conn.commit()                
    print("CSV-Dateien erfolgreich in die Datenbank importiert.")
    #Datenbankverbindung schließen
    conn.close()

    #eine Klasse zu parsen
    #open - > csv reader
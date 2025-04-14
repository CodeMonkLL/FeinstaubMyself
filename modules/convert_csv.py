from pathlib import Path
import delete_files, sqlite3
import download_csv, sqlite3
import user_input, sqlite3


#Convert CSV data in a DB
#Kade due CSV-Daten für das Jahr 2022 herunter und 
#importiere sie in eine SQLite-Datenbank. Prüfe ggf. den korrekten
#Import leerer EInträge als NULL-Werte.

base_path = Path(__file__)

full_path = base_path
conn = sqlite3.connect('feinstaub.db')
cur = conn.cursor()

cur.execute("SELECT timestamp, temperature FROM tem_hum")

print("Zeit\t Temperatur")
for ts, temp in cur:
    print(ts, "\t", temp)


conn.close()

#Convert soll die csv-Dateien in die Feinstaub.db importieren/migrieren
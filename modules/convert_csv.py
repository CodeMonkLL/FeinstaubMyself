from pathlib import Path
import download_csv, sqlite3


#Convert CSV data in a DB
#Kade due CSV-Daten für das Jahr 2022 herunter und 
#importiere sie in eine SQLite-Datenbank. Prüfe ggf. den korrekten
#Import leerer EInträge als NULL-Werte.

base_path = Path(__file__)

full_path = base_path
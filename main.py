from modules import user_input
from modules import create_tables, migrate_csv_to_db
from modules import extract_gz_to_csv
from modules import download_csv
from modules import delete_files
from pathlib import Path

#löschen der alten csv und csv.gz dateien

#Datenbank erstellen
create_tables("feinstaub.db")

#runterladen der csv.gz dateien
download_csv.download_csv_month(user_input.inputDate(),user_input.inputSensors())

#Convertierung der csv.gz dateiten in csv dateien
extract_gz_to_csv('downloads', 'csv')

#Starte den Import der CSV-Dateien in die Datenbank
migrate_csv_to_db()

#To-Do : 13 Monat abfangen -> fehler beheben
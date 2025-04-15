from modules import user_input;
from modules import extract_gz_to_csv;
from modules import Migrate_csv_to_db
from modules import download_csv;
from modules import delete_files;

#löschen der alten csv und csv.gz dateien

#runterladen der csv.gz dateien
#download_csv.download_csv_month(user_input.UserInput.inputDate(),user_input.UserInput.inputSensor())

#Convertierung der csv.gz dateiten in csv dateien
#extract_gz_to_csv.extract_gz_to_csv()
#Starte den Import der CSV-Dateien in die Datenbank
Migrate_csv_to_db.migrate_csv_to_db()
from modules import user_input
from modules import create_tables, migrate_csv_to_db
from modules.extract_gz_to_csv import extract_gz_to_csv
from modules.Migrate_csv_to_db import migrate_csv_to_db
from modules import download_csv
from modules import create_db;
from pathlib import Path

#löschen der alten csv und csv.gz dateien
def main():

    #Datenbank erstellen
    create_tables("feinstaub.db")

    user_input.inputDate()


    #Convertierung der csv.gz dateiten in csv dateien
    extract_gz_to_csv()

    #Starte den Import der CSV-Dateien in die Datenbank
    migrate_csv_to_db()

   


if __name__ == "__main__":
    main()
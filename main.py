from modules.DOWNLOAD_DATA import user_input,extract_gz_to_csv,Migrate_csv_to_db
from modules.DATABASE import create_db,delete_db_data,delete_files
from modules.CONSOLE import data_user_input
from modules.GUI import FeinstaubGUI


def main():

    #Datenbank erstellen
    create_db.create_tables("feinstaub.db")


    #Abfrage für Download
    user_input.input_for_download()
    #download + entpacken
    extract_gz_to_csv.extract_gz_to_csv()
    Migrate_csv_to_db.migrate_csv_to_db()

    #Abfrage der Daten für Zeitraum X von Min/Max/Avg
    data_user_input.display_data_func()

    #Daten löschen
    delete_files.delete_GZ_and_csv()
    delete_db_data.delete_all_data()


if __name__ == "__main__":
    main()
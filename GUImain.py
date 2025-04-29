from modules.DOWNLOAD_DATA import user_input,extract_gz_to_csv,Migrate_csv_to_db, download_csv
from modules.DATABASE import create_db
from modules.CONSOLE import data_user_input
from modules.GUI import FeinstaubGUI


def main():

    #Datenbank erstellen
    create_db.create_tables("feinstaub.db")


    
    
    # #download + entpacken
    # download_csv.download_csv_year()
    # extract_gz_to_csv.extract_gz_to_csv()
    # Migrate_csv_to_db.migrate_csv_to_db()

    GUI = FeinstaubGUI.FeinstaubGUI()
    GUI.mainloop()
    



if __name__ == "__main__":
    main()
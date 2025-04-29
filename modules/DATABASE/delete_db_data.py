from pathlib import Path
import sqlite3

database_path = Path(__file__).parent.parent.parent/'feinstaub.db'

def delete_all_data():
    print(f"Verwendete Datenbank: {database_path.resolve()}")
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()

    print("Zähle Einträge vor dem Löschen...")
    cur.execute("SELECT COUNT(*) FROM sds011_metric")
    print("sds011_metric vor dem Löschen:", cur.fetchone()[0])
    
    cur.execute("SELECT COUNT(*) FROM dht22_metric")
    print("dht22_metric vor dem Löschen:", cur.fetchone()[0])

    try:
        print("Lösche sds011_metric...")
        cur.execute("DELETE FROM sds011_metric")

        print("Lösche dht22_metric...")
        cur.execute("DELETE FROM dht22_metric")

        conn.commit()
        print("Alle Daten wurden erfolgreich gelöscht.")
    except Exception as e:
        print(f"Fehler beim Löschen der Daten: {e}")
    finally:
        conn.close()
if __name__ == "__main__":
    delete_all_data()

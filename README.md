#Feinstaubprojekt
Feinstaubprojekt zum Downloaden und speichern von Feinstaubdaten für das Jahr 2022.

Get Started 1. You will need python 2. Install

matplotlib:
matplotlib-3.10.1
pip install matplotlib

urllib3 2.3.0

Übersicht verwendeter Bibiotheken:

---

## 📚 Verwendete Bibliotheken und Funktionen

### 🔹 Standardbibliotheken

| Bibliothek | Genutzte Funktionen / Klassen                            | Beschreibung                                    |
| ---------- | -------------------------------------------------------- | ----------------------------------------------- |
| `os`       | `os.path.join`, `os.listdir`, `os.remove`                | Datei- und Verzeichnisoperationen               |
| `gzip`     | `gzip.open`                                              | Entpacken von `.gz`-Dateien                     |
| `shutil`   | `shutil.move`, `shutil.unpack_archive` _(optional)_      | Dateioperationen wie Verschieben oder Entpacken |
| `sqlite3`  | `sqlite3.connect`, `cursor()`, `execute()`, `fetchall()` | Zugriff auf SQLite-Datenbank mit SQL            |
| `datetime` | `datetime.strptime`, `datetime.date`, `timedelta`        | Verarbeitung von Datumsangaben                  |
| `csv`      | `csv.reader`, `next()`                                   | Einlesen von CSV-Dateien                        |
| `pathlib`  | `Path`, `Path.exists()` _(optional)_                     | Objektorientierter Umgang mit Dateipfaden       |

---

### 🔹 Externe Bibliotheken (optional, je nach Einsatz)

| Bibliothek          | Genutzte Funktionen / Klassen                          | Beschreibung                               |
| ------------------- | ------------------------------------------------------ | ------------------------------------------ |
| `requests`          | `requests.get`, `response.content`                     | Herunterladen von Dateien über HTTP        |
| `matplotlib.pyplot` | `plot`, `show`                                         | Visualisierung von Messdaten               |
| `tkinter`           | `Tk`, `Label`, `Button`, `Entry`, `Canvas`, `mainloop` | GUI-Erstellung für eine Desktop-Oberfläche |

---

### 🗂️ Eigene Dateien und Hauptfunktionen

| Datei                     | Wichtige Funktionen                            | Aufgabe                                  |
| ------------------------- | ---------------------------------------------- | ---------------------------------------- |
| `download.py`             | `download_file()`                              | Herunterladen von CSV-Dateien            |
| `unzip.py`                | `unzip_files()`                                | Entpacken von `.gz`-Dateien              |
| `write_csv_to_db.py`      | `insert_csv_data()`                            | CSV-Inhalte in SQLite-Datenbank einfügen |
| `read_all_data.py`        | `read_all()`                                   | Gesamte Daten ausgeben                   |
| `print_data_db_dht22.py`  | `print_metrics_by_day()`                       | Ausgabe von Tageswerten nach Sensortyp   |
| `display_dht22_metric.py` | `getMAXfrom()`, `getMINfrom()`, `getAVGfrom()` | Berechnung von statistischen Werten      |
| `create_db.py`            | `create_tables()`                              | Erstellt Tabellen via SQL                |
| `delete_db.py`            | `delete_database()`                            | Löscht die Datenbankdatei                |
| _(optional)_ `utils.py`   | `inputDate()`                                  | Eingabefunktion für Datumsauswahl        |

---

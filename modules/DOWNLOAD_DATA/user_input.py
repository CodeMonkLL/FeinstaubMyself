from modules.DOWNLOAD_DATA import download_csv


def input_for_download():
    print("-------------------------------------------------------")
    print("Willkommen zum Abruf von Feinstaubdaten")
    print("Bitte geben Sie zuerst an für welchen Zeitraum Sie Messwerte in die Datenbank downloaden wollen:")
    print("Gib die 1 ein für: DOWNLOAD der Messwerte eines Monats")
    print("Oder die 2 für: DOWNLOAD der Messwerte für das Jahr 2022")
    months = [
        "Januar", "Februar", "März", "April", "Mai", "Juni",
        "Juli", "August", "September", "Oktober", "November", "Dezember"
    ]
    while True:
        date_input = input(">>>")
        if not date_input.isdigit():
            print("Fehler: keine Zahl! Bitte geb erneut 1 oder 2 ein")
            continue
        date_input_int = int(date_input)

        if date_input_int not in [1, 2]:
            print("Fehler: ungültige Zahl! Bitte geb erneut 1 oder 2 ein")
            continue

        if date_input_int == 1:
            for i in range(1, 13):
                print(f"Gib bitte {i} ein für: {months[i - 1]}")
            while True:
                months_input = input(">>>")
                if not months_input.isdigit():
                    print("Fehler: bitte gib eine gültige Zahl zwischen 1 und 12 an!")
                    continue
                months_input_int = int(months_input)
                if months_input_int < 1 or months_input_int > 12:
                    print("Fehler: Zahl für Monat nicht zwischen 1 und 12")
                    continue
                print(f"Daten für {months[months_input_int - 1]} werden geladen.")
                download_csv.download_csv_month(months_input_int, "sds011_sensor_3659")
                download_csv.download_csv_month(months_input_int, "dht22_sensor_3660")
                return 

        else:
            print("Daten für das Jahr 2022 werden geladen")
            download_csv.download_csv_year()
            return  


def build_Date(day: str, month: str):
    date_string = f"2022-{int(month):02d}-{int(day):02d}"
    return date_string


if __name__ == "__main__":
    input_for_download()


from . import download_csv

class UserInput:

    def inputDate(self):
        print("-------------------------------------------------------")
        print("Willkommen zum Abruf von Feinstaubdaten")
        print("Bitte geben Sie zuerst an für welchen Zeitraum Sie Messwerte in die Datenbank downloaden wollen:")
        print("Gib die 1 ein für: Messwerte eines ganzen Monats")
        print("Oder die 2 für: Messwerte eines einzelnen Tages")
        while True:
            date_input = input()
            if not date_input.isdigit():
                 print("Fehler:keine Zahl! Bitte geb erneut 1 oder 2 ein")
                 continue
            date_input_int = int(date_input)

            if not date_input_int in [1,2]:
                 print("Fehler:ungültige Zahl! Bitte geb erneut 1 oder 2 ein")
                 continue
            

            if date_input_int == 1:
                months = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"] 
                for i in range (1,13):
                    print("Gib bitte " + str(i) + " ein für: " + months[i - 1]  )
                months_input = input()
                months_input_int = int(months_input)
                print(months_input_int)
                return months_input_int
            
            # if date_input_int == 2:
        
    def build_Date(day: str , month:str):
        date_string = f"2022-{month:2d}-{day:2d}"
        return date_string

                
            

    def inputSensors(self):
        sensors = []
        print("Wähle die Sensoren, für die du Daten herunterladen möchtest:")
        print("Drücke 1 für DHT22")
        print("Drücke 2 für SDS011")
        print("Drücke 3 für beide Sensoren")

        while True:
            sensor_input = input()
            if sensor_input == '1':
                sensors.append("dht22_sensor_3660")
            elif sensor_input == '2':
                sensors.append("sds011_sensor_3659")
            elif sensor_input == '3':
                sensors.append("dht22_sensor_3660")
                sensors.append("sds011_sensor_3659")
            else:
                print("Ungültige Eingabe. Versuche es nochmal.")

            # Abfrage beenden, wenn mindestens ein Sensor ausgewählt wurde
            if sensors:
                break
        return sensors
                 
                 
# download_csv.download_csv_month(UserInput.inputDate(),UserInput.inputSensor())



    # def inputSensor():
    #     print("--------------------------------------------------------")
    #     print("Drücke 1 für Sensor DHT22:")
    #     print("Drücke 2 für Sensor SDS011")

    #     while True:
    #         sensor_input = input()

    #         dht22:str = "dht22_sensor_3660"
    #         sds011:str = "sds011_sensor_3659"

    #         try:
    #             sensor_input_int = int(sensor_input)
    #         except:
    #             "Fehler: Nicht 1 oder 2 eingegeben"
    #             continue


    #         if sensor_input_int == 1:
    #                 print(f"Ausgewählter Sensor:{dht22}")
    #                 return dht22
    #         if sensor_input_int == 2:
    #                 print(f"Ausgewählter Sensor:{sds011}")
    #                 return sds011
    #         else:
    #              print("Ungültige Eingabe.1 für DHT22 oder 2 Für SDS011")

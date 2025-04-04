def SensorInput():
    print("Willkommen zum Abruf von Feinstaubdaten")
    print("Bitte gib zuerst den den Sensor ein, für den du die Feinstaubdaten abrufen möchtest ")
    print("Drücke 1 für Sensor DHT22")
    print("Drücke 2 für Sensor SDS011")

    while True:
        sensor_input = input()

        dht22:str = "DHT22"
        sds011 = "SDS011"

        try:
            sensor_input_int = int(sensor_input)
        except:
            "Fehler: Nicht 1 oder 2 Eingegeben"
            continue


        if sensor_input_int == 1:
                print(f"Ausgewählter Sensor:{dht22}")
                return dht22
        if sensor_input_int == 2:
                print(f"Ausgewählter Sensor:{sds011}")
                return sds011
        else:
             print("Ungültige Eingabe.1 für DHT22 oder 2 Für SDS011")


SensorInput()
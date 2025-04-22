from get_Value import get_Value_from_DB




def set_value():
    while True:
        print("----------------------------------------------------------")
        print("Nun können Sie sich Maximalwert, Minimalwert und Durchschnittswert")
        print("eines Zeitraums ermitteln lassen:")
        print("Dazu bitte zuerst 1,2 oder 3 drücken für:")
        print("1 für Maximalwert")
        print("2 für Minimalwert")
        print("3 für Mittelwert")

        actionInput = input()

        if not actionInput.isdigit():
            print("Fehler, bitte 1,2 oder 3 für die jeweiligen Werte angeben")
            continue

        actionInput_int = int(actionInput)

        if actionInput_int not in [1,2,3]:
            print("Fehler: Zahl ist nicht 1,2 oder 3 für jeweilige Werte")
            continue

        else: print("Du hast die Zahl " + actionInput + "angegeben")
        
        if actionInput_int == 1:
            return "MAX"
        
        if actionInput_int == 2:
            return "MIN"
        
        if actionInput_int == 3:
            return "AVG"
        


def return_date():
    print("-----------------------------------------------------------")
    # print("Gib bitte das Startdatum im Format MM-DD an (für das Jahr 2022):")

    while True:
        startDate = input("Datum: ")

        parts = startDate.split("-")

        if len(parts) != 2:
            print("Fehler: Format muss MM-DD sein.")
            continue

        month, day = parts

        if not (month.isdigit() and day.isdigit()):
            print("Fehler: Monat und Tag müssen Zahlen sein.")
            continue

        month_int = int(month)
        day_int = int(day)

        if not (1 <= month_int <= 12):
            print("Fehler: Monat muss zwischen 01 und 12 liegen.")
            continue

        if not (1 <= day_int <= 31):
            print("Fehler: Tag muss zwischen 01 und 31 liegen.")
            continue

        month = month.zfill(2)
        day = day.zfill(2)

        date = month + "-" + day

        return date


def return_sensor_column():
    # print("Gib an, welchen Wert du abrufen willst: ")
    while True:
        columns = ["temperature","humidity","P1","P2",]
        sensors = ["dht22_metric","sds011_metric",]
        for i in range (1,5):
            print(f"Gib bitte {i} ein für: {columns[i-1]}")
        
        columninput = input()

        columninput_int = int(columninput)

        if not columninput.isdigit():
            print("Bitte gib eine gültige Zahl ein!")
            continue
    
        if not (1 <= columninput_int <= 4):
            print("Bitte gib eine Zahl zwischen 1 und 4 für den jeweiligen Wert ein!")
            continue

        if columninput_int == 1:
            print(f"{columns[0]} ausgewählt")
            return columns[0] , sensors[0]
        
        elif columninput_int == 2:
            print(f"{columns[1]} ausgewählt")
            return columns[1], sensors[0]
        
        elif columninput_int == 3:
            print(f"{columns[2]} ausgewählt")
            return columns[2], sensors[1]
        
        elif columninput_int == 4:
            print(f"{columns[3]} ausgewählt")
            return columns[3], sensors[1]




def display_data_func():
    value = set_value()
    
    column_sensor = return_sensor_column()

    column = column_sensor[1]

    sensor = column_sensor[0]

    print("Gib bitte das Startdatum im Fortmat MM-DD an (für 2022)")    
    startdate = return_date()

    print("Gib bitte das Enddatum im Fortmat MM-DD an (für 2022)")
    enddate = return_date()

    get_Value_from_DB(value,column,sensor,startdate, enddate)


if __name__ == "__main__":
    display_data_func()


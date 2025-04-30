from modules.CONSOLE import get_Value
from modules.GRAPH_EXTENSION import show_graph




def set_value():
    while True:
        print("----------------------------------------------------------")
        print("Nun können Sie sich Maximalwert, Minimalwert und Durchschnittswert")
        print("eines Zeitraums ermitteln lassen:")
        print("Dazu bitte zuerst 1,2 oder 3 drücken für:")
        print("1 für Maximalwert")
        print("2 für Minimalwert")
        print("3 für Mittelwert")

        actionInput = input(">>>")

        if not actionInput.isdigit():
            print("Fehler, bitte 1,2 oder 3 für die jeweiligen Werte angeben")
            continue

        actionInput_int = int(actionInput)

        if actionInput_int not in [1,2,3]:
            print("Fehler: Zahl ist nicht 1,2 oder 3 für jeweilige Werte")
            continue

        else: print("Du hast die Zahl " + actionInput + " angegeben")
        
        if actionInput_int == 1:
            return "MAX"
        
        if actionInput_int == 2:
            return "MIN"
        
        if actionInput_int == 3:
            return "AVG"
        


def return_date():
    print("-----------------------------------------------------------")

    while True:
        startDate = input(">>>")

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
    while True:
        columns = ["temperature","humidity","P1","P2",]
        sensors = ["dht22_metric","sds011_metric",]
        for i in range (1,5):
            print(f"Gib bitte {i} ein für: {columns[i-1]}")
        
        columninput = input(">>>")
        print("Du hast " + columninput + " ausgewählt")

        columninput_int = int(columninput)

        if not columninput.isdigit():
            print("Fehler:Bitte gib eine gültige Zahl ein!")
            continue
    
        if not (1 <= columninput_int <= len(columns)):
            print("Fehler: Bitte gib eine Zahl zwischen 1 und 4 für den jeweiligen Wert ein!")
            continue

        if columninput_int == 1:
            print(f"{columns[0]} ausgewählt")
            return sensors[0], columns[0]  
        
        elif columninput_int == 2:
            print(f"{columns[1]} ausgewählt")
            return sensors[0], columns[1]  
        
        elif columninput_int == 3:
            print(f"{columns[2]} ausgewählt")
            return sensors[1], columns[2]  
        
        elif columninput_int == 4:
            print(f"{columns[3]} ausgewählt")
            return sensors[1], columns[3]




def display_data_func():
    while True:
        value = set_value()
        
        column_and_sensor = return_sensor_column()

        sensor = column_and_sensor[0] # z. B. "dht22_metric"
        column = column_and_sensor[1]  # z. B. "temperature" 

        print("Gib bitte das Startdatum im Fortmat MM-DD an (für 2022)")    
        startdate = return_date()

        print("Gib bitte das Enddatum im Fortmat MM-DD an (für 2022)")
        enddate = return_date()

        get_Value.get_Value_from_DB(value,sensor,column,startdate,enddate)

        show_graph.get_plot_data(sensor, column, startdate, enddate)

        print("Möchtest du eine weitere Aufgabe machen?")
        print("Drücke e für EXIT oder beliebige Taste um erneut zu starten")
        exit = input(">>>").lower()
        if exit == "e":
            print("Programm wird beendet")
            break
            


if __name__ == "__main__":
    display_data_func()


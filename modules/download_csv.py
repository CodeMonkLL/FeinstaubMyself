from pathlib import Path;
import urllib3;
import calendar;

# Download csv zum /parent.parent/downloadverzeichnis relativ zum 
def download_csv(date:str, sensor_name:str):
    
    download_directory = Path(__file__).parent.parent/'downloads'

    download_path = download_directory / f"{date}_{sensor_name}.csv.gz"

    print(download_directory)

    url = f"https://archive.sensor.community/2022/{date}/{date}_{sensor_name}.csv.gz"

    http = urllib3.PoolManager()

    csvrequest = http.request("GET", url, preload_content=False)

    csvmessage = csvrequest.read()

    filepath = open(str(download_path),'wb')
    
    filepath.write(csvmessage)

    filepath.close()


## calendar.monthrange returnt den ersten Tag des Monats 
# und die Anzahl der Tage im Monat -> [2] ist die Anzahl
def return_days_per_month(month:int):
    year = 2022

    month = month

    days_for_month = calendar.monthrange(year, month)   
    
    print(str(days_for_month[1]))
    
    return days_for_month[1]


def download_csv_month(month:int, sensor: str):
    maximum_days = return_days_per_month(month)
    
    if sensor == "dht22_sensor_3660":
        for i in range (1,maximum_days + 1):
            if i > 0 and i <= 10:
                download_csv("2022-"+ str(month) + "-0" + str(i), "dht22_sensor_3660")
            else:
                download_csv("2022-" + str(month) + "-" + str(i), "dht22_sensor_3660")






download_csv_month(2,"dht22_sensor_3660")



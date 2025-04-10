from pathlib import Path;
import urllib3;
import calendar;
from urllib3.exceptions import HTTPError

# Download csv zum /parent.parent/downloadverzeichnis relativ zum 
def download_csv(date:str, sensor_name:str):
    
    download_directory = Path(__file__).parent.parent/'downloads'

    download_path = download_directory / f"{date}_{sensor_name}.csv.gz"

    print(download_directory)

    url = f"https://archive.sensor.community/2022/{date}/{date}_{sensor_name}.csv.gz"

    http = urllib3.PoolManager()


    try:
        csvrequest = http.request("GET", url, preload_content=False)
    
    except Exception as e:
        print (e)
        return

    if csvrequest.status == 404:
        print("Daten nicht vorhanden.")
        return
    
    elif not csvrequest.status == 200:
        print(f"Unbekannter Fehler Grund:{csvrequest.reason}")
        return 

    csvmessage = csvrequest.read()

    with open(str(download_path),'wb') as file:
    
        file.write(csvmessage)


def build_Date(day: str , month:str):
    date_string = f"2022-{month:2d}-{day:2d}"
    return date_string


## calendar.monthrange returnt den ersten Tag des Monats 
# und die Anzahl der Tage im Monat -> [1] ist die Anzahl
def return_days_per_month(month:int) -> int:

    return calendar.monthrange(2022, month)[1]


def download_csv_month(month:int, sensor: str):
    maximum_days = return_days_per_month(month)

    month_str = str(month) # => 10
    if month < 10:  # < 10
        month_str = "0" + str(month)
    
    for i in range (1,maximum_days + 1):

        day_str = str(i)
        if i < 10:
            day_str = "0" + str(i)

        download_csv("2022-"+ month_str + "-" + day_str, sensor)




if __name__ == "__main__":
    download_csv("2022-02-02","dht22_sensor_3660")



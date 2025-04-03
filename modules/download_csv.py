from pathlib import Path;
import urllib3;





def download_csv(date, sensor_name):
    
    download_directory = Path(__file__).parent.parent/'downloads'

    download_path = download_directory / f"{date}_{sensor_name}.csv.gz"

    print(download_directory)

    url = f"https://archive.sensor.community/2022/{date}/{date}_{sensor_name}.csv.gz"

    http = urllib3.PoolManager()

    csvrequest = http.request("GET", url, preload_content=False)

    csvmessage = csvrequest.read()

    filepath = open(str(download_path),'wb')
    
    filepath.write(csvmessage)

    



download_csv("2022-04-01", "dht22_sensor_3660")
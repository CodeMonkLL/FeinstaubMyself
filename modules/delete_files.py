from pathlib import Path;
import os;

def delete_download_data():
    download_directory = Path(__file__).parent.parent/'downloads'
    for file in download_directory.interdir():
        os.remove(file)


def delete_GZ_only():
    download_directory = Path(__file__).parent.parent/'downloads'
    for file in download_directory.iterdir():
        if file.suffix == '.gz':
            print("CZ File deleted:"+ str(file) ) 
            file.unlink()
    
def delete_GZ_and_csv():
    download_directory = Path(__file__).parent.parent/'downloads'
    for file in download_directory.iterdir():
        file.unlink()


delete_GZ_and_csv()
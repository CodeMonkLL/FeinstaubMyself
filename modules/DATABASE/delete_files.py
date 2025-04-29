from pathlib import Path;

def delete_download_data():
    download_directory = Path(__file__).parent.parent.parent/'downloads'
    for file in download_directory.iterdir():
        file.unlink()


def delete_GZ_only():
    download_directory = Path(__file__).parent.parent.parent/'downloads'
    for file in download_directory.iterdir():
        if file.suffix == '.gz':
            print("CZ File deleted:"+ str(file) ) 
            file.unlink()
    
def delete_GZ_and_csv():
    download_directory = Path(__file__).parent.parent.parent/'downloads'
    csv_directory = Path(__file__).parent.parent.parent/'csv'
    for file in download_directory.iterdir():
        file.unlink()
    for file in csv_directory.iterdir():
        file.unlink()

if __name__ == "__main__":
    delete_GZ_and_csv()
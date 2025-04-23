import gzip
from pathlib import Path
import os

## find all .csv.gz in 'downloads'
# extract ans save as .csv into csv ordner




def extract_gz_to_csv_func(dir_path: Path, dir_target: Path): #where to take file and where to save them
    os.makedirs(dir_target, exist_ok=True) #create target dir (if it doesn't already exist)

    for gz_file in dir_path.iterdir():
        if gz_file.is_file() and gz_file.name.endswith('.csv.gz'):
            csv_file_name = gz_file.name[:-3]  # remove ".gz" to create a new path 
            local_csv_path = dir_target / csv_file_name # generate the full path to a new CSV file

            print(f"Unpacking: {gz_file.name} => {csv_file_name}")

            #unpacking gzip => csv 
            with gzip.open(gz_file, 'rt', encoding='utf-8') as f_in:
                with open(local_csv_path, 'w', encoding='utf-8') as f_out:
                    f_out.write(f_in.read()) #reads the entire contents of a gzip file and writes it to a csv file.


def extract_gz_to_csv():
    dir_path = Path(__file__).parent.parent / 'downloads'
    dir_target = Path(__file__).parent.parent / 'csv'
    extract_gz_to_csv_func(dir_path, dir_target)

if __name__ == "__main__":
    extract_gz_to_csv()


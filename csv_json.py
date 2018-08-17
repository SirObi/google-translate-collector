import csv
import json
import os

FILE_PATH = './csv_inputs/Lesson 14-08-2018 - Phrasebook.csv'

def save_csv_to_json(file_path):
   with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)

        output_path = os.path.splitext(csvfile.name)[-2].replace('csv_inputs', 'json_files') + '.json'
        print("Output file: {}".format(output_path))

        output_dict = {row['English']: row['Hanzi'] for row in reader}
        with open(output_path, 'w') as output_file:
           json.dump(output_dict, output_file)
        return output_path

if __name__ == '__main__':
    save_csv_to_json(FILE_PATH)

import os
import json
import pathlib

def make_output_dir_if_needed(base_output_dir, input_file):
    input_filename = get_filename(input_file).strip('.txt').strip('.json')
    new_dir_path = '{}/{}/individual_recordings'.format(base_output_dir, input_filename)
    pathlib.Path(new_dir_path).mkdir(parents=True, exist_ok=True) 
    return new_dir_path

def get_filename(open_file):
    """Grab name of file that was opened with 
    open()"""
    file_path = open_file.name
    filename = os.path.basename(file_path)
    return filename

def convert_txt_to_json(file_path):
    lines = []
    with open(file_path, 'r') as infile:
        for line in infile:
            lines.append(line)

    output_path = file_path.replace('.txt', '.json')
    with open(output_path, 'w') as outfile:
        json.dump(lines, outfile)

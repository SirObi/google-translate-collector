import os
import argparse
from pydub import AudioSegment
from distutils import spawn

# MP3_OUTPUTS = argparse.ArgumentParser()
# MP3_OUTPUTS.add_argument('d1', option = os.chdir(input("paste here path to MP3_OUTPUTS file:")), help= 'paste path to MP3_OUTPUTS file')

parser = argparse.ArgumentParser()
parser.add_argument('--mp3outputs', help= 'paste path to MP3_OUTPUTS file')
parser.add_argument('--outputdir', help= 'paste path to OUTPUT_DIR file')
args = parser.parse_args()
MP3_OUTPUTS = args.path
OUTPUT_DIR = args.path2

# OUTPUT_DIR = argparse.ArgumentParser()
# OUTPUT_DIR.add_argument('d2', option = os.chdir(input("paste here path to OUTPUT_DIR file:")), help= 'paste path to OUTPUT_DIR file')

# parser2 = argparse.ArgumentParser()
# parser2.add_argument('--path2', help= 'paste path to OUTPUT_DIR file')
# args2 = parser2.parse_args()


AudioSegment.converter = spawn.find_executable('ffmpeg')

def concatenate_recording(dir_name, *args):
    '''Create a recording given an arbitrarily long
    list of mp3 files'''
    
    output_file = './{}.mp3'.format(dir_name)
    print("This is output file: {}".format(output_file))
    
    silence_file = './silence_mp3s/Silence01s.mp3'
    silence = AudioSegment.from_mp3(silence_file)
    
    final_output = silence
    
    two_secs = create_pause(silence, 2)
    for audio_file in args:
        next_phrase = AudioSegment.from_mp3(audio_file)
        pause_required = int(round(next_phrase.duration_seconds))
        pause = create_pause(silence, pause_required) + two_secs
        final_output = final_output + next_phrase + pause
    
    final_output.export(output_file, format="mp3")


def create_pause(pause, duration_required_sec):
    final_pause = pause
    for i in range(duration_required_sec):
        final_pause += pause
    return final_pause

# Example usage:
files_list = [MP3_OUTPUTS + file for file in os.listdir(MP3_OUTPUTS)]
concatenate_recording(OUTPUT_DIR, *files_list)

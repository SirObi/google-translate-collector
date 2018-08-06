import os
from pydub import AudioSegment

MP3_OUTPUTS = "./mp3_outputs/Mandarin vocab - 1/individual_recordings/"
OUTPUT_DIR = "./mp3_outputs/Mandarin vocab - 1"

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
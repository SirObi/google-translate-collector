import os
from pydub import AudioSegment
from itertools import repeat

def concatenate_recording(dir_name, *args):
    '''Create a recording given an arbitrarily long
    list of mp3 files'''
    
    output_file = './{}.mp3'.format(dir_name)
    print("This is output file: {}".format(output_file))
    
    silence_file = './silence_mp3s/Silence01s.mp3'
    silence = AudioSegment.from_mp3(silence_file)
    
    final_output = silence + silence + silence
    
    two_secs = create_pause(silence, 2)
    for audio_file in args:
        next_phrase = AudioSegment.from_mp3(audio_file)
        pause_required = int(round(next_phrase.duration_seconds))
        print(str(pause_required))
        pause = create_pause(silence, pause_required) + two_secs
        final_output = final_output + next_phrase + pause
    
    final_output.export(output_file, format="mp3")


def create_pause(pause, duration_required_sec):
    final_pause = pause
    for i in range(duration_required_sec):
        final_pause += pause
    return final_pause

# Example usage:
files_list = ["./english_words/individual_recordings/" + file for file in os.listdir("./english_words/individual_recordings/")]
concatenate_recording("english_words2", *files_list)
concatenate_recording("some_dir4", *["./english_words/individual_recordings/How_are_you.mp3", "./english_words/individua\
l_recordings/Cat.mp3"])


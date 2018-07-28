from pydub import AudioSegment

def concatenate_recording(dir_name, *args):
    '''Create a recording given an arbitrarily long
    list of mp3 files'''
    
    output_file = './{}.mp3'.format(dir_name)
    print("This is output file: {}".format(output_file))
    
    silence_file = './silence_mp3s/Silence01s.mp3'
    silence = AudioSegment.from_mp3(silence_file)
    
    final_output = silence + silence + silence

    for audio_file in args:
        print(audio_file)
        next_phrase = AudioSegment.from_mp3(audio_file)
        final_output = final_output + next_phrase + silence
    
    final_output.export(output_file, format="mp3")

# Example usage:
concatenate_recording("some_dir4", *["./english_words/individual_recordings/How_are_you.mp3", "./english_words/individua\
l_recordings/Cat.mp3"])


def concatenate_recording(dir_name, silence_dir,  *args):
    '''Create a recording given an arbitrarily long
    list of mp3 files'''
    
    output_file = './{}.mp3'.format(dir_name)
    print("This is output file: {}".format(output_file))
    
    silence_file = './silence_mp3s/Silence08s.mp3'
    with open(silence_file, 'rb') as silence_2sec:
        silence = silence_2sec.read()

    with open(output_file, 'ab') as outfile:
        for audio_file in args:
            with open(audio_file, 'rb') as infile:
                outfile.write(silence)
                input = infile.read()
                outfile.write(input)


# Example usage:
concatenate_recording("some_dir3", *["./english_words/individual_recordings/Hello.mp3", "./english_words/individual_recordings/Cat.mp3"])


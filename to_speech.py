import os

def get_filename(open_file):
    """Grab name of file that was opened with 
    open()"""
    file_path = open_file.name
    filename = os.path.basename(file_path)
    return filename

def synthesize_english_speech(file):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()
    
    with open(file, 'r') as infile:
        text_filename = get_filename(infile).strip('.txt')
        output_filename = "{}.mp3".format(text_filename)

        for line in infile:
            input_text = texttospeech.types.SynthesisInput(text=line)
            
            # Note: the voice can also be specified by name.
            # Names of voices can be retrieved with client.list_voices().
            voice = texttospeech.types.VoiceSelectionParams(
                language_code='en-US',
                ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

            audio_config = texttospeech.types.AudioConfig(
                audio_encoding=texttospeech.enums.AudioEncoding.MP3)

            response = client.synthesize_speech(input_text, voice, audio_config)

            # The response's audio_content is binary.
            with open(output_filename, 'ab') as out:
                out.write(response.audio_content)
                print('Audio content written to file "{}"'.format(output_filename))


def synthesize_english_mandarin_speech(file):
    """Synthesizes speech from a JSON input, 
    containing English-Mandarin pairs"""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    with open(file, 'r') as infile:
        text_filename = get_filename(infile).strip('.txt')
        output_filename = "{}.mp3".format(text_filename)
        
        #TODO: implement function once JSON input is available from to_mandarin.py
        #for english, mandarin in dictionary.items():
            


synthesize_english_speech("./english_words.txt")

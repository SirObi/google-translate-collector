import os
import json
import pathlib

def make_output_dir_if_needed(input_file):
    input_filename = get_filename(input_file).strip('.txt').strip('.json')
    new_dir_path = './{}/individual_recordings'.format(input_filename)
    pathlib.Path(new_dir_path).mkdir(parents=True, exist_ok=True) 
    return new_dir_path

def get_filename(open_file):
    """Grab name of file that was opened with 
    open()"""
    file_path = open_file.name
    filename = os.path.basename(file_path)
    return filename

def synthesize_speech_from_textfile(file):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()
    
    with open(file, 'r') as infile:
        output_dir = make_output_dir_if_needed(infile)

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
            
            output_filename = line.strip().replace(" ", "_")
            output_filename = '{}/{}.mp3'.format(output_dir, output_filename)
            # The response's audio_content is binary.
            with open(output_filename, 'ab') as out:
                out.write(response.audio_content)
                print('Audio content written to file "{}"'.format(output_filename))

def synthesize_speech_one_item(input_string, input_language, output_name, output_dir, google_client):
    from google.cloud import texttospeech

    input_text = texttospeech.types.SynthesisInput(text=input_string)
    
    voice = texttospeech.types.VoiceSelectionParams(
                language_code=input_language,
                ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
                audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = google_client.synthesize_speech(input_text, voice, audio_config)
    
    output_filename = output_name.strip().replace(" ", "_")
    output_filename = '{}/{}_{}.mp3'.format(output_dir, output_filename, input_language)
    
    with open(output_filename, 'ab') as out:
                out.write(response.audio_content)
                print('Audio content written to file "{}"'.format(output_filename))

def synthesize_speech_from_json(file):
    """Synthesizes speech from a JSON input, 
    containing English-Mandarin pairs"""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    with open(file, 'rb') as infile:
        output_dir = make_output_dir_if_needed(infile)
        language_pairs = json.load(infile)

    for english, mandarin in language_pairs.items():
        synthesize_speech_one_item(english, 'en-US', english, output_dir, client)
        synthesize_speech_one_item(mandarin, 'zh', english, output_dir, client)


synthesize_speech_from_json("./conversation.json")

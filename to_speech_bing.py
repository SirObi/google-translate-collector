import os
import json
import keyring
from helpers import make_output_dir_if_needed, get_filename

MP3_OUTPUT_DIR = "./mp3_outputs"
JSON_INPUT_FILE = "./json_files/Phrasebook - Mandarin (quick hack).json"
#BING_SUBSCRIPTION_KEY = 'YOUR_KEY_GOES_HERE'

def synthesize_speech_one_item(input_string, input_language, voice, output_name, output_dir):
    from bingtts import Translator
    #translator = Translator(BING_SUBSCRIPTION_KEY)
    bing_key = keyring.get_password("bing_api", "obi")
    translator = Translator(bing_key)

    output = translator.speak(input_string, input_language, voice, "audio-16khz-64kbitrate-mono-mp3 ")
    
    output_filename = output_name.strip().replace(" ", "_")
    output_filename = '{}/{}_{}.mp3'.format(output_dir, output_filename, input_language)

    with open(output_filename, "wb") as f:
        f.write(output)

    print('Audio content written to file "{}"'.format(output_filename))

def synthesize_speech_from_json(file, base_output_dir=MP3_OUTPUT_DIR):
    """Synthesizes speech from a JSON file, 
    containing English-Mandarin pairs"""
    with open(file, 'rb') as infile:
        output_dir = make_output_dir_if_needed(base_output_dir, infile)
        language_pairs = json.load(infile)

    for english, mandarin in language_pairs.items():
        synthesize_speech_one_item(english, 'en-US', 'JessaRUS', english, output_dir)
        synthesize_speech_one_item(mandarin, 'zh-CN', 'Kangkang, Apollo', english, output_dir)

def synthesize_mandarin_from_text(file, output_name):
    """Synthesizes speech from a text file,                                                                                                             
    containing Mandarin phrases"""
    with open(file, 'r') as infile:
        output_dir = make_output_dir_if_needed(infile)
        lines = json.load(infile)
         
        for line in lines:                                                                                                                                       
            file_name = output_name + "_{}".format(i)                                                                                                    
            synthesize_speech_one_item(line, 'zh-CN', 'Kangkang, Apollo', output_name, output_dir)
                
                
synthesize_speech_from_json(JSON_INPUT_FILE)

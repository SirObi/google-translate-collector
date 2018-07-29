import json
# Imports the Google Cloud client library
from google.cloud import translate

# Instantiates a client
translate_client = translate.Client()



def translate(source_text):
   # The text to translate
   text = source_text
   # The target language                                                                                          
   target = 'zh'

   # Translates some text into Mandarin                                                                           
   translation = translate_client.translate(
       text,
       target_language=target)

   return translation['translatedText']

def translate_file(file_path):
   with open(file_path, 'r') as infile:
      translations = {line.strip('\n'): translate(line) for line in infile}
      return translations

def store_translations(translations, file_path):
   """Takes dictionary of English-Mandarin pairs and stores it as a JSON"""
   with open(file_path, 'w') as outfile:
      json.dump(translations, outfile)

translations = translate_file('./english_conversation.txt')
store_translations(translations, './mandarin_translations_conversation.json')

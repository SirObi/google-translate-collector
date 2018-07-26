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
      translations = [translate(line) for line in infile]
      return translations

def store_translations(translations, file_path):
   with open(file_path, 'w') as outfile:
      for phrase in translations:
         outfile.write('{}\n'.format(phrase))

translations = translate_file('./english_words.txt')
store_translations(translations, './mandarin_translations.txt')

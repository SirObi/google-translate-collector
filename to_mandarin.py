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
   print(u'Text: {}'.format(text))
   print(u'Translation: {}'.format(translation['translatedText']))

def translate_file(file_path):
   with open(file_path, 'r') as infile:
      for line in infile:
         translate(line)

translate_file('./english_words.txt')

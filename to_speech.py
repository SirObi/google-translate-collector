def synthesize_english_speech(file):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()
    
    with open(file, 'r') as infile:
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
            with open('output.mp3', 'ab') as out:
                out.write(response.audio_content)
                print('Audio content written to file "output.mp3"')


synthesize_english_speech("./english_words.txt")

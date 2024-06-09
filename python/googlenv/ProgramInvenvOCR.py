
import sys

from googletrans import Translator

translator = Translator()

# Hindi text to be translated
# hindi_text = text  # "Hello, world"

# Translate to English
# translation = translator.translate(hindi_text, dest='en')

# Output the translated text
# print("Original:", hindi_text)
# print("Translated:", translation.text)

# Read command-line argument
arg_from_script1 = sys.argv[1]
# Process the argument


# Eglish text to be translated
english_text =   arg_from_script1 # "Hello, world"

# Translate to English
translation = translator.translate(english_text, dest='hi')

# Output the translated text
print("Original:", english_text)
print("Translated:", translation.text)

processed_arg = translation.text


from gtts import gTTS
import playsound

# Text you want to translate and speak
text_to_translate = processed_arg

# Create a Google Text-to-Speech object with the translated text and language choice
tts = gTTS(text=text_to_translate, lang='hi', slow=False)

# Save the audio to a file
audio_file = "output.mp3"
tts.save(audio_file)

# Play the audio file
playsound.playsound(audio_file)
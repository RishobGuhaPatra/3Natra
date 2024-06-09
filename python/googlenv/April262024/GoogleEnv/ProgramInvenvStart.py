
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
translation = translator.translate(english_text, dest='en')

# Output the translated text
print("Original:", english_text)
print("Translated:", translation.text)

processed_arg = translation.text
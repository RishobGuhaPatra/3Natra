#recording user prompt

import subprocess

# Define the arecord command parameters
device = "plughw:3,0"  # The specific device to use
duration = 5  # Duration of recording in seconds
sample_rate = 44100  # Sampling rate in Hz (44.1 kHz)
channels = 2  # Number of channels (stereo)
file_format = "cd"  # CD quality (16-bit, stereo, 44.1 kHz)
output_format = "wav"  # Output format
output_file = "testhi.wav"  # Name of the output file

# Construct the arecord command
arecord_command = [
    "arecord",
    "-D", device,
    "-f", file_format,
    "-t", output_format,
    "-d", str(duration),
    "-r", str(sample_rate),
    "-c", str(channels),
    output_file,
]

# Run the arecord command using subprocess

try:
    subprocess.run(arecord_command, check=True)
    print(f"Recording complete. Audio saved to {output_file}.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while recording: {e}")



import speech_recognition as sr

# Create a recognizer object
recognizer = sr.Recognizer()

# Path to the audio file
audio_file_path = "testhi.wav"  # Change this to your audio file's path

# Use an AudioFile context manager to read the audio
with sr.AudioFile(audio_file_path) as source:
    # Read the entire audio file
    audio_data = recognizer.record(source)
    
# Use Google Speech Recognition to convert audio to text

try:
    text = recognizer.recognize_google(audio_data, language="hi-IN")  # Convert the audio to text
    print("Transcription:", text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition; {0}".format(e))




from googletrans import Translator

translator = Translator()

# Hindi text to be translated
hindi_text = text  # "Hello, world"

# Translate to English
translation = translator.translate(hindi_text, dest='en')

# Output the translated text
print("Original:", hindi_text)
print("Translated:", translation.text)

# Eglish text to be translated
english_text = "Please describe the picture"  # "Hello, world"

# Translate to English
translation = translator.translate(english_text, dest='hi')

# Output the translated text
print("Original:", english_text)
print("Translated:", translation.text)


from gtts import gTTS
import os
import requests

# Text to be converted to speech
text = translation.text

# Language in which you want to convert
language = 'mr'  # Marathi

# Initialize the gTTS object with the text and language
tts = gTTS(text=text, lang=language, slow=False)

# Save the converted audio to a file
tts.save("output.mp3")

# Play the converted audio
os.system("cvlc output.mp3")

from gtts import gTTS
import playsound
import os
import speech_recognition as sr

def play_beep():
        # Using a beep sound file
        beep_sound_path = "beep.mp3"
        playsound.playsound(beep_sound_path)


# Text you want to translate and speak
text_to_translate = "Please spell the Wifi SSID in English - wait 5 secounds after the beep before you speak"

# Create a Google Text-to-Speech object with the translated text and language choice
tts = gTTS(text=text_to_translate, lang='en', slow=False)

# Save the audio to a file
audio_file = "output1.mp3"
tts.save(audio_file)

# Play the audio file
playsound.playsound(audio_file)



import subprocess

# Define the arecord command parameters
device = "plughw:3,0"  # The specific device to use
duration = 5  # Duration of recording in seconds
sample_rate = 44100  # Sampling rate in Hz (44.1 kHz)
channels = 2  # Number of channels (stereo)
file_format = "cd"  # CD quality (16-bit, stereo, 44.1 kHz)
output_format = "wav"  # Output format
output_file = "test.wav"  # Name of the output file

# Play beep sound to prompt the user to speak
print("You can start speaking now...")
play_beep()
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
    print(f"Recording complete. Audio saved to {output_file}.")
    subprocess.run(arecord_command, check=True)
    print(f"Recording complete. Audio saved to {output_file}.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while recording: {e}")


# Mapping of spoken words to symbols
symbol_mapping = {
    "underscore": "_",
    "at": "@",
    "hash": "#",
    "space": " ",
    "English": "en",
    "Hindi": "hi",
    "marathi": "mr",
    "bengali": "bn"
}

def capitalize_letter(word, index):
    return word[:index] + word[index].upper() + word[index + 1:]

# Function to interpret symbols in the transcribed text
def interpret_symbols(text):
    for word, symbol in symbol_mapping.items():
        if word in text.lower():
            text = text.replace(word, symbol)
    return text


# recorded prompt to text 

import speech_recognition as sr

# Create a recognizer object
recognizer = sr.Recognizer()

# Path to the audio file
audio_file_path = "test.wav"  # Change this to your audio file's path

# Use an AudioFile context manager to read the audio
with sr.AudioFile(audio_file_path) as source:
    # Read the entire audio file
#   print("Adjusting for ambient noise, please wait...")
#   sr.adjust_for_ambient_noise(source, duration=1)
    audio_data = recognizer.record(source)
    
# Use Google Speech Recognition to convert audio to text

try:
    text = recognizer.recognize_google(audio_data)  # Convert the audio to text
    print("Transcription:", text)
    interpreted_text = interpret_symbols(text)
    print("Interpreted text with symbols:", interpreted_text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition; {0}".format(e))


words = interpreted_text.split()  # This breaks the text into a list of words

# Join the words into a single string with spaces in between
joined_text = ''.join(words)

print("Joined SSID:", joined_text)

SSIDname = joined_text


#  input("SSID:")


# Text you want to translate and speak
text_to_translate = "Please spell the Wifi Password in English - wait 5 secounds after the beep before you speak"

# Create a Google Text-to-Speech object with the translated text and language choice
tts = gTTS(text=text_to_translate, lang='en', slow=False)

# Save the audio to a file
audio_file = "output1.mp3"
tts.save(audio_file)

# Play the audio file
playsound.playsound(audio_file)


import subprocess

# Define the arecord command parameters
device = "plughw:3,0"  # The specific device to use
duration = 5  # Duration of recording in seconds
sample_rate = 44100  # Sampling rate in Hz (44.1 kHz)
channels = 2  # Number of channels (stereo)
file_format = "cd"  # CD quality (16-bit, stereo, 44.1 kHz)
output_format = "wav"  # Output format
output_file = "test1.wav"  # Name of the output file


# Play beep sound to prompt the user to speak
print("You can start speaking now...")
play_beep()

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
    print(f"Recording complete. Audio saved to {output_file}.")
    subprocess.run(arecord_command, check=True)
    print(f"Recording complete. Audio saved to {output_file}.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while recording: {e}")




# recorded prompt to text 

import speech_recognition as sr

# Create a recognizer object
recognizer = sr.Recognizer()

# Path to the audio file
audio_file_path = "test1.wav"  # Change this to your audio file's path

# Use an AudioFile context manager to read the audio
with sr.AudioFile(audio_file_path) as source:
    # Read the entire audio file
#    print("Adjusting for ambient noise, please wait...")
#    sr.adjust_for_ambient_noise(source, duration=1)
       

    audio_data = recognizer.record(source)
    
# Use Google Speech Recognition to convert audio to text

try:
    text1 = recognizer.recognize_google(audio_data)  # Convert the audio to text
    print("Transcription:", text1)
    interpreted_text = interpret_symbols(text1)
    print("Interpreted text with symbols:", interpreted_text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition; {0}".format(e))



words1 = interpreted_text.split()  # This breaks the text into a list of words

# Join the words into a single string with spaces in between
joined_text1 = ''.join(words1)

print("Joined Password:", joined_text1)


Password = joined_text1
# input("Password:")

print(SSIDname)
print(Password)

#SSID = "Sangeeta's Wi-Fi Network"  # Replace with your Wi-Fi SSID
#PASSWORD = "Babaji4567" # Replace with your Wi-Fi password

# Command to connect to Wi-Fi using nmcli
#result = subprocess.run(
#   ["nmcli", "dev", "wifi", "connect", SSID, "password", PASSWORD],
#   stdout=subprocess.PIPE,
#   text=True,
#)

# Check for errors
#if result.returncode == 0:
#    print(f"Connected to {SSID}")
#else:
#    print(f"Failed to connect to {SSID}. Error: {result.stdout}")


#  input("SSID:")


# Text you want to translate and speak
text_to_translate = "Please speak the language support you want - wait 5 secounds after the beep before you speak"

# Create a Google Text-to-Speech object with the translated text and language choice
tts = gTTS(text=text_to_translate, lang='en', slow=False)

# Save the audio to a file
audio_file = "output1.mp3"
tts.save(audio_file)

# Play the audio file
playsound.playsound(audio_file)
       

import subprocess

# Define the arecord command parameters
device = "plughw:3,0"  # The specific device to use
duration = 5  # Duration of recording in seconds
sample_rate = 44100  # Sampling rate in Hz (44.1 kHz)
channels = 2  # Number of channels (stereo)
file_format = "cd"  # CD quality (16-bit, stereo, 44.1 kHz)
output_format = "wav"  # Output format
output_file = "test2.wav"  # Name of the output file


# Play beep sound to prompt the user to speak
print("You can start speaking now...")
play_beep()

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
    print(f"Recording complete. Audio saved to {output_file}.")
    subprocess.run(arecord_command, check=True)
    print(f"Recording complete. Audio saved to {output_file}.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while recording: {e}")




# recorded prompt to text 

import speech_recognition as sr

# Create a recognizer object
recognizer = sr.Recognizer()

# Path to the audio file
audio_file_path = "test2.wav"  # Change this to your audio file's path

# Use an AudioFile context manager to read the audio
with sr.AudioFile(audio_file_path) as source:
    
#    print("Adjusting for ambient noise, please wait...")
#    sr.adjust_for_ambient_noise(source, duration=1)
    # Read the entire audio file
    audio_data = recognizer.record(source)
    
# Use Google Speech Recognition to convert audio to text

try:
    text2 = recognizer.recognize_google(audio_data)  # Convert the audio to text
    print("Transcription language:", text2)
    interpreted_text1 = interpret_symbols(text2)
    print("Language:", interpreted_text1)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition; {0}".format(e))
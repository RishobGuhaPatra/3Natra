
from gtts import gTTS
import playsound
#recording user prompt

import speech_recognition as sr


def play_beep():
        # Using a beep sound file
        beep_sound_path = "beep.mp3"
        playsound.playsound(beep_sound_path)
        
import subprocess

# Define the arecord command parameters
device = "plughw:3,0"  # The specific device to use
duration = 5  # Duration of recording in seconds
sample_rate = 44100  # Sampling rate in Hz (44.1 kHz)
channels = 2  # Number of channels (stereo)
file_format = "cd"  # CD quality (16-bit, stereo, 44.1 kHz)
output_format = "wav"  # Output format
output_file = "test.wav"  # Name of the output file


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
    subprocess.run(arecord_command, check=True)
    print(f"Recording complete. Audio saved to {output_file}.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while recording: {e}")
    text_to_translate = "मुझे खेद है, मैं आपके प्रश्न को ठीक से समझ नहीं पाया, क्या आप कृपया उसी बटन को दोबारा दबा सकते हैं और कुछ सेकंड के बाद प्रश्न पूछ सकते हैंा"

# Create a Google Text-to-Speech object with the translated text and language choice
    tts = gTTS(text=text_to_translate, lang='hi', slow=False)

# Save the audio to a file
    audio_file = "output1.mp3"
    tts.save(audio_file)

# Play the audio file
    playsound.playsound(audio_file)

#



# recorded prompt to text 

import speech_recognition as sr

# Create a recognizer object
recognizer = sr.Recognizer()

# Path to the audio file
audio_file_path = "test.wav"  # Change this to your audio file's path

# Use an AudioFile context manager to read the audio
with sr.AudioFile(audio_file_path) as source:
    # Read the entire audio file
    audio_data = recognizer.record(source)
    
# Use Google Speech Recognition to convert audio to text

try:
    text = recognizer.recognize_google(audio_data)  # Convert the audio to text
    print("Transcription:", text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio.")
    text_to_translate = "क्षमा करें मैं आपका प्रश्न समझने में असमर्थ रहा। क्या आप कृपया अपनी आंखों के पास वाला बटन दोबारा दबा सकते हैं और मेरी बात समाप्त होने पर प्रश्न पूछ सकते हैं?"
    tts = gTTS(text=text_to_translate, lang='hi', slow=False)
    audio_file = "output1.mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
                
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition; {0}".format(e))


# send the image and prompt to fireworks for resposne, 
# 

import subprocess

# Path to the Python executable in Virtual Environment B
venv_b_python = "/home/orangepi/googlenv/bin/python"

# Path to Program B
program_b_path = "/home/orangepi/googlenv/ProgramInvenvStart.py"


#result = subprocess.run(['python', 'program_b_path', 'Please Translate in Marathi'], capture_output=True, text=True)

# Print the output of script2.py
#print("Output from script2.py:", result.stdout.decode())

# Run Program B and capture the output
result = subprocess.run(
    [venv_b_python, program_b_path, recognizer.recognize_google(audio_data)], 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE
)

# Display the output
print("Program B Output:")
print(result.stdout.decode())

#if result.returncode != 0:
#    print("Error:", result.stderr.decode())



from fireworks.client import Fireworks

client = Fireworks(api_key="u0s0V8wGKv1VyriyX9bj1Aa7V3rLwl2Fg7TxkRDtz6bwumho")
response = client.chat.completions.create(
  model="accounts/fireworks/models/llama-v2-7b-chat",
  messages=[{
    "role": "user",
    "content": text,
  }],
)
print(response.choices[0].message.content)

import subprocess

# Path to the Python executable in Virtual Environment B
venv_b_python = "/home/orangepi/googlenv/bin/python"

# Path to Program B
program_b_path = "/home/orangepi/googlenv/ProgramInvenv.py"


#result = subprocess.run(['python', 'program_b_path', 'Please Translate in Marathi'], capture_output=True, text=True)

# Print the output of script2.py
#print("Output from script2.py:", result.stdout.decode())

# Run Program B and capture the output
result = subprocess.run(
    [venv_b_python, program_b_path, response.choices[0].message.content], 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE
)

# Display the output
print("Program B Output:")
print(result.stdout.decode())

running = False

#if result.returncode != 0:
#    print("Error:", result.stderr.decode())

# 
# translare text to speech

#from gtts import gTTS
#import os

# Text to be converted to speech
#text = response.choices[0].message.content

# Language in which you want to convert
#language = 'hi'  # English

# Initialize the gTTS object with the text and language
#tts = gTTS(text=text, lang=language, slow=False)

# Save the converted audio to a file
#tts.save("/home/orangepi/googlenv/output.wav")

# Play the converted audio
#os.system("cvlc output.wav")



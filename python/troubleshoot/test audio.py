import subprocess
import sys

# Define the arecord command parameters
device = "plughw:5,0"  # The specific device to use
duration = 5 # Duration of recording in seconds
sample_rate = 44100  # Sampling rate in Hz (44.1 kHz)
channels = 2  # Number of channels (stereo)
file_format = "cd"  # CD quality (16-bit, stereo, 44.1 kHz)
output_format = "wav"  # Output format
output_file = "test.wav"  # Name of the output file

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
#    print(f"Recording complete. Audio saved to {output_file}.")
    subprocess.run(arecord_command, check=True)
    print(f"Recording complete. Audio saved to {output_file}.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while recording: {e}")

from gtts import gTTS
import playsound


# Text you want to translate and speak
text_to_translate = "test.wav"

# Create a Google Text-to-Speech object with the translated text and language choice
tts = gTTS(text=text_to_translate, lang='en', slow=False)

# Save the audio to a file
audio_file = "output1.mp3"
tts.save(audio_file)

# Play the audio file
playsound.playsound(audio_file)



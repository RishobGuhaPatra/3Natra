import cv2

# Initialize the camera capture object
cap = cv2.VideoCapture(1)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the camera.")
    exit()

# Capture a single frame from the camera
ret, frame = cap.read()

# Check if the frame is valid
if not ret:
    print("Error: Couldn't capture frame.")
    exit()

# Save the captured frame to an image file
cv2.imwrite('captured_image.jpg', frame)

# Release the camera capture object
cap.release()

print("Image captured successfully.")


def play_beep():
        # Using a beep sound file
        beep_sound_path = "beep.mp3"
        playsound.playsound(beep_sound_path)



from gtts import gTTS
import playsound

# Text you want to translate and speak
text_to_translate = "अब क्या आप कृपया त्रि-नेत्रा से कोई प्रश्न पूछ सकते हैं। कृपया ध्यान दें कि जब भी आप अपनी आंखों के पास बाईं ओर बटन दबाएंगे तो आप मेरे आस-पास जो कुछ भी देखेंगे उसके बारे में प्रश्न पूछ सकते हैं। मैं आपकी सबसे अच्छी सहायक बनने की पूरी कोशिश करूंगी। - कृपया बोलना शुरू करने से पहले बीप के बाद 5 सेकंड तक प्रतीक्षा करें।"

# Create a Google Text-to-Speech object with the translated text and language choice
tts = gTTS(text=text_to_translate, lang='hi', slow=False)

# Save the audio to a file
audio_file = "output1.mp3"
tts.save(audio_file)

# Play the audio file
playsound.playsound(audio_file)

#recording user prompt

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




import fireworks.client
import base64

# Helper function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# The path to your image
image_path = "captured_image.jpg"

# The base64 string of the image
image_base64 = encode_image(image_path)

fireworks.client.api_key = "NGLBW1jhWpSuBUE8L5I5AdkQQVN1FIq5GF9y3ZeGmjrSNnTB"

response = fireworks.client.ChatCompletion.create(
  model = "accounts/fireworks/models/firellava-13b",
  messages = [{
    "role": "user",
    "content": [{
      "type": "text",
#      "text": "Can you describe this image?",
#       "text": "please describe the image?",
        "text": "text",
    }, {
      "type": "image_url",
      "image_url": {
           "url": f"data:image/jpeg;base64,{image_base64}"
#          "url": "https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"
      },
    }, ],
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


import cv2

from gtts import gTTS
import playsound

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
cv2.imwrite('example_image.jpg', frame)

# Release the camera capture object
cap.release()

print("Image captured successfully.")

import pytesseract
from PIL import Image
import sys  # For sys.exit()

# Function to perform OCR and quit if the text is blank
def extract_text_and_check(image_path):
    # Load the image
    image = Image.open(image_path)

    # Extract text
    text = pytesseract.image_to_string(image)

    # Check if the text is blank or contains only whitespace
    if text.strip() == "":
        print("No text found. Exiting the program.")
        text_to_translate = "मेरे विचार में त्रि-नेत्र ने कोई पाठ नहीं देखा है। त्रिनेत्रा अंग्रेजी और हिंदी दोनों पाठ पढ़ सकता है और आपके लिए उनका अनुवाद कर सकता है"
        tts = gTTS(text=text_to_translate, lang='hi', slow=False)
        audio_file = "output1.mp3"
        tts.save(audio_file)
        playsound.playsound(audio_file)
        sys.exit(0)  # Exit the program with status 0 (no error)

    return text

# Test with an image
image_path = "example_image.jpg"  # Replace with your image path

text = extract_text_and_check(image_path)

print("Extracted text:")
print(text)




import subprocess

# Path to the Python executable in Virtual Environment B
venv_b_python = "/home/orangepi/googlenv/bin/python"

# Path to Program B
program_b_path = "/home/orangepi/googlenv/ProgramInvenvOCR.py"


#result = subprocess.run(['python', 'program_b_path', 'Please Translate in Marathi'], capture_output=True, text=True)

# Print the output of script2.py
#print("Output from script2.py:", result.stdout.decode())

# Run Program B and capture the output
result = subprocess.run(
    [venv_b_python, program_b_path, text], 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE
)

# Display the output
print("Program B Output:")
print(result.stdout.decode())



# from gtts import gTTS
# import os

# Text to be converted to speech
#text = "Hello, this is a test."

# Language in which you want to convert
# language = 'en'  # English

# Initialize the gTTS object with the text and language
# tts = gTTS(text=text, lang=language, slow=False)

# Save the converted audio to a file
# tts.save("output.mp3")

# Play the converted audio
# os.system("cvlc output.mp3")
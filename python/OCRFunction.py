import cv2

from gtts import gTTS
import playsound

text_to_translate = "कृपया ध्यान दें कि पाठ त्रि-नेत्र के फोकस में होना चाहिए और अंग्रेजी, मराठी और हिंदी पाठ को समझ सकता है। यदि पाठ त्रि-नेत्र की दृष्टि में नहीं है या आंशिक रूप से दृष्टि में है तो सटीक नहीं होगा। त्रि-नेत्र आपको पढ़ने में मदद करने की पूरी कोशिश करेगा।"
tts = gTTS(text=text_to_translate, lang='hi', slow=False)
audio_file = "output1.mp3"
tts.save(audio_file)
playsound.playsound(audio_file)
    
# Initialize the camera capture object
cap = cv2.VideoCapture(1)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the camera.")
    
    text_to_translate = "ट्राई-नेत्रा कैमरा खोलकर कोई टेक्स्ट कैप्चर नहीं कर सका। कृपया ट्राई-नेत्रा से कहें कि जब आपका कैमरा काम करने लगे, तब वह फिर से प्रयास करें"
    tts = gTTS(text=text_to_translate, lang='hi', slow=False)
    audio_file = "output1.mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    exit()

# Capture a single frame from the camera
ret, frame = cap.read()

# Check if the frame is valid
if not ret:
    print("Error: Couldn't capture frame.")
    text_to_translate = "त्रि-नेत्र में समस्याएँ आईं और फ़्रेम में कोई भी टेक्स्ट कैप्चर नहीं हो सका। कृपया पुनः प्रयास करें।"
    tts = gTTS(text=text_to_translate, lang='hi', slow=False)
    audio_file = "output1.mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
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
  #    image = Image.open(image_path)

    # Extract text
    text = pytesseract.image_to_string(image_path)
    return text


    # Check if the text is blank or contains only whitespace
image_path = cv2.imread("example_image.jpg")  # Replace with your image path

# Test with an image

    # Apply Gaussian blur for noise reduction

#blurred_image = cv2.GaussianBlur(image_path, (5, 5), 0)

    # Convert the image to grayscale
def get_grayscale(image_path):
    return cv2.cvtColor(image_path, cv2.COLOR_BGR2GRAY)

def blurred_image(image_path):
    return cv2.GaussianBlur(image_path, (5, 5), 0)
 
def remove_noise(image_path):
    return cv2.medianBlur(image_path, 5)

def thresholding(image_path):
    return cv2.threshold(image_path, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


image_path = get_grayscale(image_path)
#image_path = thresholding(image_path)
#image_path = remove_noise(image_path)
#image_path = blurred_image(image_path)

#cv2.imshow('Grayscale Image', image_path)

#cv2.waitKey(0)  # Wait until a key is pressed
text = extract_text_and_check(image_path)

print ("Extracted Text:")
print(text)


if text.strip() == "":
        print("No text found. Exiting the program.")
        text_to_translate = "मेरे विचार में त्रि-नेत्र ने कोई पाठ नहीं देखा है। त्रिनेत्रा अंग्रेजी और हिंदी दोनों पाठ पढ़ सकता है और आपके लिए उनका अनुवाद कर सकता है"
        tts = gTTS(text=text_to_translate, lang='hi', slow=False)
        audio_file = "output1.mp3"
        tts.save(audio_file)
        playsound.playsound(audio_file)
        sys.exit(0)  # Exit the program with status 0 (no error)



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
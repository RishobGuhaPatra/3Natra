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

#image_path = blurred_image(image_path)
image_path = get_grayscale(image_path)
#image_path = thresholding(image_path)
#image_path = remove_noise(image_path)
cv2.imshow('Grayscale Image', image_path)

cv2.waitKey(0)  # Wait until a key is pressed
text = extract_text_and_check(image_path)

print ("Extracted Text:")
print(text)


if text.strip() == "":
        print("No text found. Exiting the program.")
        text_to_translate = "मेरे विचार में त्रि-नेत्र ने कोई पाठ नहीं देखा है। त्रिनेत्रा अंग्रेजी और हिंदी दोनों पाठ पढ़ सकता है और आपके लिए उनका अनुवाद कर सकता है"
        tts = gTTS(text=text_to_translate, lang='hi', slow=False)
        audio_file = "output1.mp3"
        tts.save(audio_file)
#        playsound.playsound(audio_file)
        sys.exit(0)  # Exit the program with status 0 (no error)



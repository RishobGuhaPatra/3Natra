import cv2
import pytesseract

# Read the input image
image = cv2.imread('example_image.jpg')

# Apply Gaussian blur for noise reduction
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Convert the image to grayscale
gray_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding to convert to binary
thresholded_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# OCR with Pytesseract
text = pytesseract.image_to_string(thresholded_image)

# Print the recognized text
print("Recognized Text:")
print(text)
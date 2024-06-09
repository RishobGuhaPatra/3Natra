import cv2

# Initialize the camera capture object
# Replace '0' with the appropriate camera index (e.g., 1, 2, etc.) if you have multiple cameras
cap = cv2.VideoCapture(1)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the camera.")
    exit()

# Loop to continuously capture frames from the camera
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame is valid
    if not ret:
        print("Error: Couldn't capture frame.")
        break

    # Display the captured frame
    cv2.imshow('USB Camera', frame)
    cv2.imwrite('example_image.jpg', frame)
    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
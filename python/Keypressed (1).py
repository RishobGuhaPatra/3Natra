# MAIN PRORAM WORKING VERSION - final test-ocr(1).py and Blindapp2.py - this is keypressed(1)


from gtts import gTTS
import playsound

# Text you want to translate and speak
text_to_translate = "मैं यहाँ आपको दुनिया को देखने में मदद करने के लिए हूँ - मैं त्रिनेत्र हूँ और आपको एहसास करा सकता हूँ कि आपके आस-पास क्या है और मैं आपके आस-पास का कोई भी टेक्स्ट भी पढ़ सकता हूँ। अब, आपके चश्मे पर 3 बटन हैं। आपकी आँखों की तरफ वाला बटन मैं आपको देखने में मदद करने के लिए इस्तेमाल करूँगा। बीच वाला बटन आपके लिए कोई भी टेक्स्ट पढ़ने के लिए है और आपकी आँखों से सबसे दूर वाला बटन मुझे यह बताने के लिए है कि मैं आपको देखने में मदद करना बंद कर दूँ। किसी भी समय अगर आप जाने का फैसला करते हैं तो आप मुझे जगाने के लिए अपनी आँखों से दूर इस बटन को दबा सकते हैं। सबसे पहले मैं आपके वाईफ़ाई इंटरनेट सेटअप से शुरुआत करता हूँ।"

# Create a Google Text-to-Speech object with the translated text and language choice
tts = gTTS(text=text_to_translate, lang='hi', slow=False)

# Save the audio to a file
audio_file = "/audio/output1.mp3"
tts.save(audio_file)

# Play the audio file
playsound.playsound(audio_file)



import pygame
import sys
import subprocess

pygame.init()

# Create a window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Key Input Detection")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Detect 'q' key
                print("You pressed 'Return'. Executing Vision Glasses...")
                text_to_translate = "आपने त्रि-नेत्र से दुनिया की कल्पना करने और अनुभव साझा करने के लिए कहा है। आप इस समय मुझसे कोई भी प्रश्न पूछ सकते हैं. मैंने जो देखा वह आपके साथ साझा करूंगा"
                
                tts = gTTS(text=text_to_translate, lang='hi', slow=False)
                audio_file = "audio/output1.mp3"
                tts.save(audio_file)
                playsound.playsound(audio_file)
                
                # Path to the Python executable in Virtual Environment B
                venv_b_python = "/home/orangepi/googlenv/bin/python"

                # Path to Program B
                program_b_path = "/home/orangepi/Blindapp2.py"
                #result = subprocess.run(['python', 'program_b_path', 'Please Translate in Marathi'], capture_output=True, text=True)
                # Print the output of script2.py
                #print("Output from script2.py:", result.stdout.decode())

                # Run Program B and capture the output
                subprocess.run(["python", program_b_path])
# Display the output

                print("Program for Vision Glasses to Run:")
#               running = False
            elif event.key == pygame.K_1: 
                print("You pressed '1'. Executing OCR...")               
                    # Path to the Python executable in Virtual Environment B
                venv_b_python = "/home/orangepi/googlenv/bin/python"

                    # Path to Program B
                program_b_path = "/home/orangepi/OCRFunction.py"
                    #result = subprocess.run(['python', 'program_b_path', 'Please Translate in Marathi'], capture_output=True, text=True)

                    # Print the output of script2.py
                    #print("Output from script2.py:", result.stdout.decode())

                    # Run Program B and capture the output
                    
                subprocess.run(["python", program_b_path])

                    # Display the output
                print("Program for Vision OCR to Run:")
                
            elif event.key == pygame.K_2: 
                print("You pressed '1 and return'. Executing AI Chat...")               
                    # Path to the Python executable in Virtual Environment B
                venv_b_python = "/home/orangepi/googlenv/bin/python"

                    # Path to Program B
                program_b_path = "/home/orangepi/AIChat loop.py"
                    #result = subprocess.run(['python', 'program_b_path', 'Please Translate in Marathi'], capture_output=True, text=True)

                    # Print the output of script2.py
                    #print("Output from script2.py:", result.stdout.decode())

                    # Run Program B and capture the output
                    
                subprocess.run(["python", program_b_path])

                    # Display the output
                print("Program for AI Chat to Run:")
                     
                     
pygame.quit()
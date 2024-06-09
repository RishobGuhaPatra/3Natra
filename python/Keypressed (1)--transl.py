# MAIN PRORAM WORKING VERSION - final test-ocr(1).py and Blindapp2.py - this is keypressed(1)



from gtts import gTTS
import playsound

# Text you want to translate and speak
text_to_translate = "मैं यहां आपको दुनिया की कल्पना करने में मदद करने के लिए हूं - मैं त्रिनेत्र हूं और आपको यह एहसास दिला सकता हूं कि आपके आस-पास क्या है और मैं आपके आस-पास कोई भी पाठ भी पढ़ सकता हूं। अब, आपके चश्मे पर 3 बटन हैं। आपकी आँखों की ओर वाला वह है जिसका उपयोग मैं आपको देखने में मदद करने के लिए करूँगा। बीच में वाला आपके लिए कोई पाठ पढ़ने के लिए है और जो आपकी आँखों से सबसे दूर है वह मुझे देखने में आपकी मदद करना बंद करने के लिए कहने के लिए है। किसी भी समय यदि आप मुझे छोड़ने का निर्णय लेते हैं तो आप मुझे जगाने के लिए अपनी आंखों से दूर इस कुंजी को दबा सकते हैं।"

# Create a Google Text-to-Speech object with the translated text and language choice
tts = gTTS(text=text_to_translate, lang='hi', slow=False)

# Save the audio to a file
audio_file = "output1.mp3"
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
            if event.key == pygame.K_1:  # Detect 'q' key
                print("You pressed '1'. Executing Vision Glasses...")
                text_to_translate = "आपने त्रि-नेत्र से दुनिया की कल्पना करने और अनुभव साझा करने के लिए कहा है। आप इस समय मुझसे कोई भी प्रश्न पूछ सकते हैं. मैंने जो देखा वह आपके साथ साझा करूंगा"

# Create a Google Text-to-Speech object with the translated text and language choice
                tts = gTTS(text=text_to_translate, lang='hi', slow=False)

# Save the audio to a file
                audio_file = "output1.mp3"
                tts.save(audio_file)

# Play the audio file
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
elif event.key == pygame.K_RETURN: 
                 print("You pressed 'return'. Executing OCR...")
                 text_to_translate = "आपने त्रि-नेत्र से आसपास के किसी भी पाठ को पढ़ने और बीच में बटन दबाकर जो मैं देख सकता हूं उसे पढ़ने और सामग्री को साझा करने के लिए कहा है। इस समय आप वह सुन सकते हैं जो मैं पढ़ सकता हूँ। मैं जो देखूंगा उसे आपके साथ साझा करूंगा। कृपया अपने आस-पास किसी भी पाठ को देखने के लिए इधर-उधर घूमें। यदि मैं पढ़ नहीं सकता तो मैं तुम्हें बता दूंगा।"

# Create a Google Text-to-Speech object with the translated text and language choic
                 tts = gTTS(text=text_to_translate, lang='hi', slow=False)

# Save the audio to a file
                 audio_file = "output1.mp3"
                 tts.save(audio_file)

# Play the audio file
                 playsound.playsound(audio_file)

                    # Path to the Python executable in Virtual Environment B
                venv_b_python = "/home/orangepi/googlenv/bin/python"

                    # Path to Program B
                program_b_path = "/home/orangepi/test-ocr (1).py"
                    #result = subprocess.run(['python', 'program_b_path', 'Please Translate in Marathi'], capture_output=True, text=True)

                    # Print the output of script2.py
                    #print("Output from script2.py:", result.stdout.decode())

                    # Run Program B and capture the output
                    
                subprocess.run(["python", program_b_path])

                    # Display the output
                print("Program for Vision OCR to Run:")
                     

pygame.quit()
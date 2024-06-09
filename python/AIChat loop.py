
from fireworks.client import Fireworks


from gtts import gTTS


import playsound

# Text you want to translate and speak
text_to_translate = "आपने त्रि-नेत्र को ऐसे प्रश्न पूछने के लिए सक्रिय किया है जो यह चारों ओर देख सकता है और उन सभी चीज़ों पर विस्तार कर सकता है जिनका उत्तर त्रि-नेत्र दे सकता है। कृपया अपने मन में आने वाले किसी भी प्रश्न को पूछने के लिए आगे बढ़ें और त्रि-नेत्र आपकी सहायता करेगा। इसमें आप एक के बाद एक 3 प्रश्न पूछ सकते हैं। कृपया प्रश्न पूछने से पहले बीप के बाद 5 सेकंड के लिए रुकें"

# Create a Google Text-to-Speech object with the translated text and language choice
tts = gTTS(text=text_to_translate, lang='hi', slow=False)

# Save the audio to a file
audio_file = "output1.mp3"
tts.save(audio_file)

# Play the audio file
playsound.playsound(audio_file)

#recording user prompt
    
import subprocess

# A simple while loop that counts from 1 to 5
count = 1  # Initial value
while count <= 3:  # Loop condition
    print("Count is:", count)  # Loop body
    count += 1  # Update loop condition
    venv_b_python = "/home/orangepi/googlenv/bin/python"

                    # Path to Program B
    program_b_path = "/home/orangepi/AIChat.py"
                    #result = subprocess.run(['python', 'program_b_path', 'Please Translate in Marathi'], capture_output=True, text=True)

                    # Print the output of script2.py
                    #print("Output from script2.py:", result.stdout.decode())

                    # Run Program B and capture the output
                    
    subprocess.run(["python", program_b_path])

                    # Display the output
                
    print("Program for AI Chat to Run:")
                     
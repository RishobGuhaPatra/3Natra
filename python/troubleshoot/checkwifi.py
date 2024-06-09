import subprocess
import sys

from gtts import gTTS
import playsound

def is_wifi_connected(interface='wlan0'):
    try:
        # Run iwconfig command to get information about the wireless interface
        result = subprocess.run(['iwconfig', interface], capture_output=True, text=True)
        
        # Check if 'ESSID' (Extended Service Set Identifier) is in the output
        if 'ESSID' in result.stdout:
            return True
        else:
            return False

    except Exception as e:
        print("Error:", e)
        return False

# Check if Wi-Fi is connected
if is_wifi_connected():
    print("Wi-Fi is connected.")
    text_to_translate = "  त्रि-नेत्रा वाईफ़ाई से जुड़ा है और आप त्रि-नेत्रा चश्मे का उपयोग करने के लिए तैयार हैं  "

    tts = gTTS(text=text_to_translate, lang='hi', slow=False)
    audio_file = "output1.mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
else:
    print("Wi-Fi is not connected.")
    print("You want to setup Wifi and Password for Tri-Netra...")
    text_to_translate = "      Tr-Netra में आपका स्वागत है, कृपया अपना Wifi उपयोगकर्ता नाम और पासवर्ड बोलें और वह भाषा भी बोलें जिसमें आप चाहते हैं कि Tri Netra आपसे संवाद करे   "

    tts = gTTS(text=text_to_translate, lang='hi', slow=False)
    audio_file = "output1.mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)

    # Path to the Python executable in Virtual Environment B
    venv_b_python = "/home/orangepi/googlenv/bin/python"

    # Path to Program B
    program_b_path = "/home/orangepi/wificonnection.py"
    #result = subprocess.run(['python', 'program_b_path', 'Please Translate in Marathi'], capture_output=True, text=True)
    # Print the output of script2.py
    #print("Output from script2.py:", result.stdout.decode())

    # Run Program B and capture the output
    subprocess.run(["python", program_b_path])
    # Display the output

    print("Program for Setting Up Language and Wifi:")

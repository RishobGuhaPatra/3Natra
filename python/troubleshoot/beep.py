import speech_recognition as sr
import playsound
import os

def play_beep():
    # Using a beep sound file
    beep_sound_path = "beep.mp3"
    playsound.playsound(beep_sound_path)

def prompt_user_to_speak():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Adjust the recognizer sensitivity to ambient noise level
        print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source, duration=1)
       
        # Play beep sound to prompt the user to speak
        print("You can start speaking now...")
        play_beep()

        # Listen for the first phrase and extract it into audio data
        audio = r.listen(source, timeout=5, phrase_time_limit=10)
        print("Stop speaking.")

    try:
        # Recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    return ""

if __name__ == "__main__":
    prompt_user_to_speak()

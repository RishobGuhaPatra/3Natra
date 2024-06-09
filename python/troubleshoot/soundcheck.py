from gtts import gTTS
import os

# Text to be converted to speech
text = "Hello, this is a test."

# Language in which you want to convert
language = 'en'  # English

# Initialize the gTTS object with the text and language
tts = gTTS(text=text, lang=language, slow=False)

# Save the converted audio to a file
tts.save("output.mp3")

# Play the converted audio
os.system("cvlc output.mp3")
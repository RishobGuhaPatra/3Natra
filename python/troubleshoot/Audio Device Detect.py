import sounddevice as sd

# List all available audio devices
print(sd.query_devices())

# Set the default input and output devices by index
sd.default.device = (0, 0)  # (input device, output device)

# Record audio from the specified input device
duration = 5  # seconds
sample_rate = 44100
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)

# Play audio through the specified output device
sd.play(audio_data, sample_rate)

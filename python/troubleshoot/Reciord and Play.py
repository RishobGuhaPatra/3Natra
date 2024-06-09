import pyaudio
import wave

# Configuration
input_device_index = 4  # Set to your desired input device index
output_device_index = 4  # Set to your desired output device index
sample_rate = 44100
channels = 2
chunk = 1024
record_seconds = 5
output_filename = "specific_device_recording.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open a stream for recording with the specified input device
stream = audio.open(
    format=pyaudio.paInt16,
    channels=channels,
    rate=sample_rate,
    input=True,
    input_device_index=input_device_index,
    frames_per_buffer=chunk
)

# Record
print("Recording...")
frames = []
for _ in range(0, int(sample_rate / chunk * record_seconds)):
    data = stream.read(chunk)
    frames.append(data)
print("Finished recording.")

# Close the stream
stream.stop_stream()
stream.close()

# Save the recorded audio to a WAV file
with wave.open(output_filename, 'wb') as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))

# Open a stream for playback with the specified output device
stream = audio.open(
    format=pyaudio.paInt16,
    channels=channels,
    rate=sample_rate,
    output=True,
    output_device_index=output_device_index,
)

# Play the recorded audio
with open(output_filename, 'rb') as f:
    data = f.read(chunk)
    while data:
        stream.write(data)
        data = f.read(chunk)

# Close the stream and terminate PyAudio
stream.stop_stream()
stream.close()
audio.terminate()

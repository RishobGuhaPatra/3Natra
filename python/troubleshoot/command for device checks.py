
# arecord -l

# alpay -l

#  aplay -D plughw:4,0 test.wav


# arecord -D plughw:4,0 -d 10 -f dat test.wav

import sounddevice as sd

# Set default output device
sd.default.device = (4, 4)  # Output (playback), then input (recording)

# Play a sine wave to the selected output device
import numpy as np
frequency = 48000  # Frequency of the sine wave in Hz
duration = 10  # Duration in seconds
sample_rate = 48100  # Sample rate in Hz
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
sine_wave = np.sin(2 * np.pi * frequency * t)

sd.play(sine_wave, sample_rate)
sd.wait()

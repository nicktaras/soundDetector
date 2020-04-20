import aubio
import numpy as num
import pyaudio
import wave

# PyAudio object.
p = pyaudio.PyAudio()

# print("Debugging: test if the the device sample rate is correct e.g. 44100")
# print(p.get_device_info_by_index(0)['defaultSampleRate'])

# Open stream.
stream = p.open(format=pyaudio.paFloat32,
    channels=1, rate=44100, input=True,
    frames_per_buffer=1024)

# Aubio's pitch detection.
pDetection = aubio.pitch("default", 2048,
    2048//2, 44100)

# Set unit.
pDetection.set_unit("Hz")
pDetection.set_silence(-40)

while True:
    data = stream.read(1024, exception_on_overflow = False)
    samples = num.fromstring(data,
        dtype=aubio.float_type)
    pitch = pDetection(samples)[0]
    # Compute the energy (volume) of the
    # current frame (gives most accurate result)
    volume = samples[len(samples) - 1]
    print("pitch: ")
    print(pitch)
    print("volume: ")
    print(volume)

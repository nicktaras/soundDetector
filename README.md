# soundDetector
Python Sound Detector

# A POC to detect if a signal is being picked up from an input signal.

## Task List

- Define the range for volume (0 to X)
- Define the range pitch (0 to Y)
- Write a function that detects metal
- Documentation install Dependancies (Raspberry Pi)
- Gotchas with dependancies installs (not so easily to know)
- Documentation for usage of library


## Reading

- Examples: https://www.programcreek.com/python/example/52624/pyaudio.PyAudio

## Code

````
# List all devices:

def list_devices():
    """List all available microphone devices."""
    try:
        import pyaudio
    except ImportError:
        print("You have to install extra 'sound' in order to use this shell script")
        return 99

    pa = pyaudio.PyAudio()
    for i in range(pa.get_device_count()):
        dev = pa.get_device_info_by_index(i)
        input_chn = dev.get('maxInputChannels', 0)
        if input_chn > 0:
            name = dev.get('name')
            rate = dev.get('defaultSampleRate')
            print("Index {i}: {name} (Max Channels {input_chn}, Default @ {rate} Hz)".format(
                i=i, name=name, input_chn=input_chn, rate=int(rate)

            ))
    return 0 

# Play a file

def wavplay(sound):
    #print(sound)
    #mp3 to wav
    #AudioSegment.from_mp3(sound).export(("{}.wav".format(fp.name)), format="wav")
    #play wav
    chunk=1024
    file =(sound)
    #print(file)
    f = wave.open(file,"rb")
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
            channels = f.getnchannels(),
            rate = f.getframerate(),
            output = True)
    data = f.readframes(chunk)
    while len(data)>0:
    #while data != "":
    #while True:
        stream.write(data)
        data = f.readframes(chunk)
    #stream.stop_stream()
    stream.close()
    p.terminate()
    #end 

````
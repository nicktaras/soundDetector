# soundDetector
Python Sound Detector

## Installation

1. Install PyAudio library

sudo apt-get install python3-pyaudio 

2. Install Numpy

sudo apt-get install python3-numpy

## Debugging the Pi / Audio 

- https://snowboy.kitt.ai/docs
- https://github.com/Arkq/bluez-alsa/issues/26
- https://github.com/Kitt-AI/snowboy/issues/45
- https://www.raspberrypi.org/forums/viewtopic.php?t=224856

````
# Locate Sound Device
import pyaudio
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
  dev = p.get_device_info_by_index(i)
  print((i,dev['name'],dev['maxInputChannels']))
````

(0, 'bcm2835 ALSA: IEC958/HDMI (hw:0,1)', 0)
(1, 'bcm2835 ALSA: IEC958/HDMI1 (hw:0,2)', 0)
(2, 'USB Audio Device: - (hw:1,0)', 1)
(3, 'dmix', 0)
(4, 'default', 1)

## Notes

- The Pitch functionality becomes inaccurate over 10 khz (to be further tested - it could be the external sound card I'm using to develop with)

## Reading

API examples: https://www.programcreek.com/python/example/52624/pyaudio.PyAudio

## Example code from API (to enhance this repository)

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

# sudo shutdown -h now

````

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

## Notes

- The Pitch functionality becomes inaccurate over 10 khz

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

````

Common Pi Commands

````
# sudo shutdown -h now
````

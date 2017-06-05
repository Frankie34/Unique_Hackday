from pyaudio import PyAudio, paInt16
import struct
import time
import pykeyboard
from pykeyboard import PyKeyboard

def Voice_Game():
     button_1 = PyKeyboard()
     NUM_SAMPLES = 1000
     pa = PyAudio()
     while True:
         SAMPLING_RATE = int(pa.get_device_info_by_index(0)['defaultSampleRate'])
         stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True, frames_per_buffer= NUM_SAMPLES)
         string_audio_data = stream.read(NUM_SAMPLES)
         k = max(struct.unpack('1000h', string_audio_data))
         if k > 3000:
            button_1.press_key("a")
            time.sleep(1)
            button_1.release_key("a")
         if k > 8000:
        #    button_1.tap_key("^[[D")
             button_1.tap_key("w")
             time.sleep(1)
             button_1.release_key("w")
         if k > 13000:
        #    button_1.tap_key("^[[D")
             button_1.tap_key("s")
             time.sleep(1)
             button_1.release_key("s")
         time.sleep(0.1)
     return 0;


Voice_Game()

import queue

import numpy as np
import sounddevice as sd


class AudioCapture:
    def __init__(self):
        self.queue = queue.Queue()

        self.stream = sd.InputStream(
            channels=1,
            samplerate=44100,
            blocksize=2048,
            callback=self.audio_callback,
        )

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(status)

        self.queue.put(indata.copy())

    def start(self):
        self.stream.start()

    def stop(self):
        self.stream.stop()

    def get_audio(self):
        try:
            return self.queue.get_nowait()
        except queue.Empty:
            return None
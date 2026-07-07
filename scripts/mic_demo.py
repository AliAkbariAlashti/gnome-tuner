"""Print detected pitch from the microphone. Run from the repo root:

    python3 -m scripts.mic_demo
"""

import time

from src.audio.capture import AudioCapture
from src.audio.detector import PitchDetector, frequency_to_note

audio = AudioCapture()
detector = PitchDetector()

audio.start()

print("Listening... (Ctrl+C to stop)")

try:
    while True:
        chunk = audio.get_audio()

        if chunk is not None:
            frequency = detector.detect(chunk)

            if frequency > 20:
                note, cents = frequency_to_note(frequency)
                print(f"{note}  {frequency:7.2f} Hz  {cents:+5.1f} cents")

        time.sleep(0.05)
except KeyboardInterrupt:
    audio.stop()

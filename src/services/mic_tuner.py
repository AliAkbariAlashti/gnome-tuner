from src.audio.capture import AudioCapture
from src.audio.detector import PitchDetector, frequency_to_note

MIN_FREQUENCY = 20.0


class MicTuner:
    """Live tuner readings from the microphone.

    Same polling interface as FakeTuner: get_reading() returns
    {"note", "frequency", "cents"} for the latest captured chunk,
    or None when nothing pitched is being heard.
    """

    def __init__(self):
        self._capture = AudioCapture()
        self._detector = PitchDetector(sample_rate=44100)
        self._capture.start()

    def get_reading(self):
        # Drain the queue so we always analyze the freshest chunk
        chunk = None
        while True:
            latest = self._capture.get_audio()
            if latest is None:
                break
            chunk = latest

        if chunk is None:
            return None

        frequency = self._detector.detect(chunk)
        if frequency < MIN_FREQUENCY:
            return None

        note, cents = frequency_to_note(frequency)
        return {"note": note, "frequency": frequency, "cents": cents}

    def stop(self):
        self._capture.stop()

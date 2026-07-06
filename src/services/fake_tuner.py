import random


class FakeTuner:
    """Simulated tuner readings until real microphone pitch detection lands."""

    def __init__(self):
        self._cents = random.uniform(-35.0, 35.0)

    def get_reading(self):
        # Drift toward pitch with jitter, like a string slowly being tuned
        self._cents += random.uniform(-4.0, 4.0) - self._cents * 0.1
        self._cents = max(-50.0, min(50.0, self._cents))

        return {
            "note": "A4",
            "frequency": 440 * 2 ** (self._cents / 1200),
            "cents": self._cents,
        }
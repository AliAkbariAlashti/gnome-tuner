import unittest

import numpy as np

from src.audio.detector import PitchDetector, frequency_to_note

SAMPLE_RATE = 44100


def sine(frequency, n=4096, amplitude=0.5):
    t = np.arange(n) / SAMPLE_RATE
    return (amplitude * np.sin(2 * np.pi * frequency * t)).astype(np.float32)


class PitchDetectorTests(unittest.TestCase):
    def setUp(self):
        self.detector = PitchDetector(sample_rate=SAMPLE_RATE)

    def test_detects_a4(self):
        self.assertAlmostEqual(self.detector.detect(sine(440.0)), 440.0, delta=1.0)

    def test_detects_guitar_low_e(self):
        detected = self.detector.detect(sine(82.41, n=8192))
        self.assertAlmostEqual(detected, 82.41, delta=1.0)

    def test_accepts_2d_input_like_sounddevice(self):
        stereo_shaped = sine(440.0).reshape(-1, 1)
        self.assertAlmostEqual(self.detector.detect(stereo_shaped), 440.0, delta=1.0)

    def test_silence_returns_zero(self):
        self.assertEqual(self.detector.detect(np.zeros(4096)), 0.0)

    def test_quiet_noise_returns_zero(self):
        rng = np.random.default_rng(seed=7)
        noise = (rng.standard_normal(4096) * 0.001).astype(np.float32)
        self.assertEqual(self.detector.detect(noise), 0.0)

    def test_too_few_samples_returns_zero(self):
        self.assertEqual(self.detector.detect(sine(440.0, n=100)), 0.0)


class FrequencyToNoteTests(unittest.TestCase):
    def test_a4_exact(self):
        note, cents = frequency_to_note(440.0)
        self.assertEqual(note, "A4")
        self.assertAlmostEqual(cents, 0.0, places=6)

    def test_sharp_of_a4(self):
        note, cents = frequency_to_note(445.0)
        self.assertEqual(note, "A4")
        self.assertAlmostEqual(cents, 19.56, delta=0.05)

    def test_middle_c(self):
        note, cents = frequency_to_note(261.63)
        self.assertEqual(note, "C4")
        self.assertAlmostEqual(cents, 0.0, delta=0.1)

    def test_guitar_low_e(self):
        note, _ = frequency_to_note(82.41)
        self.assertEqual(note, "E2")


if __name__ == "__main__":
    unittest.main()

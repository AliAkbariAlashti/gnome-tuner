import unittest

from src.services.fake_tuner import FakeTuner


class FakeTunerTests(unittest.TestCase):
    def setUp(self):
        self.tuner = FakeTuner()

    def test_reading_has_expected_keys(self):
        reading = self.tuner.get_reading()
        self.assertEqual(set(reading), {"note", "frequency", "cents"})

    def test_cents_stay_in_meter_range(self):
        for _ in range(200):
            reading = self.tuner.get_reading()
            self.assertGreaterEqual(reading["cents"], -50)
            self.assertLessEqual(reading["cents"], 50)

    def test_frequency_matches_cents_offset(self):
        reading = self.tuner.get_reading()
        expected = 440 * 2 ** (reading["cents"] / 1200)
        self.assertAlmostEqual(reading["frequency"], expected, places=6)


if __name__ == "__main__":
    unittest.main()

import math

import numpy as np

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

A4_FREQUENCY = 440.0
A4_MIDI = 69


class PitchDetector:
    """YIN pitch detection (de Cheveigné & Kawahara, 2002) in pure numpy.

    detect() returns the fundamental frequency in Hz, or 0.0 when the
    signal is silent or has no clear pitch — the same contract as
    aubio's yin detector, without the unmaintained aubio dependency.
    """

    def __init__(self, sample_rate=44100, threshold=0.15, rms_gate=0.01):
        self.sample_rate = sample_rate
        self.threshold = threshold
        self.rms_gate = rms_gate

    def detect(self, samples):
        samples = np.asarray(samples, dtype=np.float64)
        if samples.ndim == 2:
            samples = samples[:, 0]

        n = len(samples)
        if n < 256:
            return 0.0

        samples = samples - samples.mean()
        if math.sqrt(float(np.mean(samples**2))) < self.rms_gate:
            return 0.0

        window = n // 2

        # Difference function d(tau) over the first half-window,
        # with the cross-correlation term computed via FFT
        energy = np.concatenate(([0.0], np.cumsum(samples**2)))
        spectrum = np.fft.rfft(samples, 2 * n)
        window_spectrum = np.fft.rfft(samples[:window], 2 * n)
        correlation = np.fft.irfft(spectrum * np.conj(window_spectrum))[: window + 1]

        taus = np.arange(window + 1)
        difference = (
            energy[window]
            + (energy[taus + window] - energy[taus])
            - 2 * correlation
        )

        # Cumulative mean normalized difference
        cmnd = np.ones(window + 1)
        running_sum = np.cumsum(difference[1:])
        nonzero = running_sum > 0
        cmnd[1:][nonzero] = (
            difference[1:][nonzero] * taus[1:][nonzero] / running_sum[nonzero]
        )

        min_tau = int(self.sample_rate / 1500.0)  # ignore pitches above 1500 Hz
        below = np.where(cmnd[min_tau:] < self.threshold)[0]
        if len(below) == 0:
            return 0.0
        tau = int(below[0]) + min_tau

        # Descend to the local minimum of this dip
        while tau + 1 <= window and cmnd[tau + 1] < cmnd[tau]:
            tau += 1

        # Parabolic interpolation for sub-sample precision
        if 0 < tau < window:
            left, mid, right = cmnd[tau - 1], cmnd[tau], cmnd[tau + 1]
            denominator = left - 2 * mid + right
            if denominator != 0:
                tau += 0.5 * (left - right) / denominator

        return self.sample_rate / tau


def frequency_to_note(frequency):
    """Map a frequency in Hz to (note name with octave, cents offset).

    >>> frequency_to_note(440.0)
    ('A4', 0.0)
    """
    midi = A4_MIDI + 12 * math.log2(frequency / A4_FREQUENCY)
    nearest = round(midi)
    cents = (midi - nearest) * 100
    name = NOTE_NAMES[nearest % 12]
    octave = nearest // 12 - 1
    return f"{name}{octave}", cents

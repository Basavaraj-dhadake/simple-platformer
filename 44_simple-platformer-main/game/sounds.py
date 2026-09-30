import math
import array
import pygame

SAMPLE_RATE = 44100


def _tone(segments, volume=0.35):
    """Build a Sound from [(start_freq, end_freq, seconds), ...] sine sweeps."""
    samples = array.array("h")
    phase = 0.0
    for f0, f1, dur in segments:
        n = int(SAMPLE_RATE * dur)
        for i in range(n):
            t = i / max(1, n - 1)
            freq = f0 + (f1 - f0) * t
            phase += 2 * math.pi * freq / SAMPLE_RATE
            fade = min(1.0, (n - i) / (SAMPLE_RATE * 0.02))  # avoid clicks
            samples.append(int(32767 * volume * fade * math.sin(phase)))
    return pygame.mixer.Sound(buffer=samples.tobytes())


class SoundManager:
    """Generates simple sound effects in code (no asset files needed).
    If no audio device is available the game keeps running silently."""

    def __init__(self):
        self.enabled = False
        self.sounds = {}
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init(frequency=SAMPLE_RATE, size=-16, channels=1)
            self.sounds = {
                "jump": _tone([(300, 650, 0.15)]),
                "goal": _tone([(523, 523, 0.10), (659, 659, 0.10), (784, 784, 0.10), (1047, 1047, 0.20)]),
                "die": _tone([(400, 90, 0.5)], volume=0.4),
            }
            self.enabled = True
        except (pygame.error, NotImplementedError):
            print("Audio unavailable - running without sound.")

    def play(self, name):
        if self.enabled and name in self.sounds:
            self.sounds[name].play()

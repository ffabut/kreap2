"""
This is an experiment with sorting the audio samples in small windows.
It sounds quite dull and metalic, like a weird granular effect.
Overall it is not very interesting. But maybe someone could find a way to make it sound better, or use it in a creative way.
"""

from pedalboard.io import AudioFile, AudioStream
import numpy

with AudioFile("../samples/piano_loop.wav") as f:
    audio = f.read(f.frames)
    sr = f.samplerate

print("starting sort")
channels, samples = audio.shape
window_size = 50
for ch in range(channels):
    for start in range(0, samples, window_size):
        end = min(start + window_size, samples)
        audio[ch, start:end] = numpy.sort(audio[ch, start:end])
print("finished sort")


out_dev = AudioStream.default_output_device_name
print("Using output:", out_dev)
AudioStream.play(audio, sr, output_device_name=out_dev)

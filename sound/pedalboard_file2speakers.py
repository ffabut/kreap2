from pedalboard import Pedalboard, Chorus, Compressor, Gain, Reverb, Phaser
from pedalboard.io import AudioFile, AudioStream

board = Pedalboard([
    Compressor(threshold_db=-50, ratio=25),
    Gain(gain_db=30),
    Chorus(),
    Phaser(),
    Reverb(room_size=1),
])

with AudioFile("samples/piano_loop.wav") as f:
    audio = f.read(f.frames)
    sr = f.samplerate

effected = board(audio, sr)

out_dev = AudioStream.default_output_device_name
print("Using output:", out_dev)
AudioStream.play(effected, sr, output_device_name=out_dev)

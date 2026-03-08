### REVERSED REVERB ###
# aka: https://www.soundonsound.com/techniques/creating-reverse-reverb
#
# This is a simple example showing how to create a reversed reverb effect using the Pedalboard library.
# 1. we read an audio file and reverse it (flip along the time axis)
# 2. we apply a reverb effect to the reversed audio
# 3. we reverse the effected audio back to its original order
# This creates an effect in which reverb runs before the actual sound is produced.

from pedalboard import Pedalboard, Reverb
from pedalboard.io import AudioFile, AudioStream
import numpy

board = Pedalboard([
    Reverb(room_size=0.2),
])

with AudioFile("samples/piano_loop.wav") as f:
    audio = f.read(f.frames)
    # axis=0 je levy/pravy kanal, obraceni by prohodilo kanaly, na mono signalu by neudelalo nic
    # axis=1 je cas, obraceni zpusobi, ze se zvuk bude prehravat odzadu
    rev_audio = numpy.flip(audio, axis=1)
    del audio # idealni kandidat na uvolneni pamet
    sr = f.samplerate

effected = board(rev_audio, sr)
rev_effected = numpy.flip(effected, axis=1) # otacime zpet, aby originalni zvuk byl v puvodnim poradi, ale reverb ted pojede naopak - tedy driv nez zdrojovy zvuk
del effected # uvolnime pamet

out_dev = AudioStream.default_output_device_name
print("Using output:", out_dev)
AudioStream.play(rev_effected, sr, output_device_name=out_dev)

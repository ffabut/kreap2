from pedalboard import Pedalboard, Chorus, Compressor, Gain, Reverb, Phaser
from pedalboard.io import AudioStream

print("INPUTS:")
for i, name in enumerate(AudioStream.input_device_names):
    print("-", i, name)
x = int(input("Use input number (default 0): ") or 0)
in_dev = AudioStream.input_device_names[x]

print("\nOUTPUTS:")
for i ,name in enumerate(AudioStream.output_device_names):
    print("-", i, name)    
y = int(input("Use output number (default 0): ") or 0)
out_dev = AudioStream.output_device_names[y]


with AudioStream(
  input_device_name=in_dev,
  output_device_name=out_dev
) as stream:
  stream.plugins = Pedalboard([
      Compressor(threshold_db=-50, ratio=25),
      Gain(gain_db=30),
      Chorus(),
      Phaser(),
      Reverb(room_size=0.25),
  ])
  input("Press enter to stop streaming...")


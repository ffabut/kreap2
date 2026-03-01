# Ukázka přehrávání zvukového souboru pomocí miniaudio.
# Skript načte zvukový soubor "samples/piano_loop.wav"
# a přehraje ho na výchozím přehrávacím zařízení, dokud uživatel nestiskne Enter.

import miniaudio

info = miniaudio.get_file_info("samples/piano_loop.wav")
print(f"Loading file: {info}")

stream = miniaudio.stream_file("samples/piano_loop.wav")
with miniaudio.PlaybackDevice() as device:
    device.start(stream)
    input("Audio file playing in the background. Enter to stop playback: ")


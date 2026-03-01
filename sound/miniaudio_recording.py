# Ukázka jednoduchého záznamu zvuku z mikrofonu pomocí miniaudio.
# Skript nahrává zvuk z výchozího nahrávacího zařízení do proměnné recorded, dokud uživatel nestiskne Enter.
# Zvuk je pak uložen do souboru "recorded.wav".
# Zvuk je nahráván do proměnné recorded, tedy do RAM paměti. Pro delší nahrávky by bylo vhodnější ukládat průběžně do souboru, aby nedošlo k zaplnění RAM paměti.

import miniaudio
import wave

OUTPUT_FILE = "recorded.wav"
SAMPLE_RATE = 44100
CHANNELS = 1
SAMPLE_WIDTH_BYTES = 2 # 16-bit audio = 2 bytes per sample

recorded = bytearray()
capture_device = miniaudio.CaptureDevice(
    sample_rate=SAMPLE_RATE,
    nchannels=CHANNELS,
    input_format=miniaudio.SampleFormat.SIGNED16,
)

def capture_generator():
    """Endless generator that gets captured PCM bytes via yield and appends them to the global `recorded` bytearray.
    For more information about generators: https://www.w3schools.com/python/python_generators.asp
    """
    while True:
        pcm_bytes = yield
        recorded.extend(pcm_bytes)

gen = capture_generator()
next(gen) # generator musí být "primed" před prvním použitím, proto zavoláme next() pro posun na první yield


print("Recording... press Enter to stop.")
capture_device.start(gen)
input()
capture_device.stop()
capture_device.close()

# Ukládání recorded bytearray do WAV souboru pomocí standardní knihovny wave.
with wave.open(OUTPUT_FILE, "wb") as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SAMPLE_WIDTH_BYTES)
    wf.setframerate(SAMPLE_RATE)
    wf.writeframes(recorded)

print(f"Saved: {OUTPUT_FILE}")

# Zvuk

## Simple audio playback

Pro jednoduché přehrávání zvuku existuje řada knihoven, ale řada z nich je dlouho neudržovaná, případně určená jen pro jeden operační systém.
Z udržovaných a multiplatformních knihoven můžeme doporučit například tyto:
- Playsound3 - https://github.com/szmikler/playsound3
- Miniaudio - https://github.com/irmen/pyminiaudio

### Miniaudio

Podporuje přehrávání wav, flac, vorbis a mp3.
Umožňuje také nahrávání zvuku z mikrofonu.

```python
import miniaudio

## Můžeme zobrazit info o souboru
info = miniaudio.get_file_info("samples/piano_loop.wav")
print(f"Loading file: {info}") 

# načtení souboru do paměti
stream = miniaudio.stream_file("samples/piano_loop.wav")

# vytvoření přehrávacího zařízení - volbu necháváme na defaults miniaudio
with miniaudio.PlaybackDevice() as device:
    device.start(stream) # spustíme non-blocking přehrávání
    input("Audio file playing in the background. Enter to stop playback: ") # čekáme na vstup od uživatele, jinak by skriptu skončil a přehrávání by se zastavilo
```

## Audio manipulation 

### Pydub

Populární knihovna, ale poslední aktualizace je z roku 2022.
V případě nouze se ale asi dá použít...
https://github.com/jiaaro/pydub


## Audio I/O

https://github.com/bastibe/python-soundfile
https://github.com/bastibe/SoundCard



## Sound processing in real time

https://github.com/spotify/pedalboard


## CREDITS

piano_loops.wav is a sound [Piano loops 200 octave short loop 120 bpm](https://freesound.org/people/josefpres/sounds/841765/) by [Josef Pres](https://freesound.org/people/josefpres/)

kick.wav is a sound [
Kick - Proper Bottom.wav](https://freesound.org/people/TechGeekMusic/sounds/353396/) by [TechGeekMusic](https://freesound.org/people/TechGeekMusic/)

Thank you all!
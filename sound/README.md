# Zvuk

## Simple audio playback

Pro jednoduché přehrávání zvuku existuje řada knihoven, ale řada z nich je dlouho neudržovaná, případně určená jen pro jeden operační systém.
Z udržovaných a multiplatformních knihoven můžeme doporučit například tyto:
- Playsound3 - https://github.com/szmikler/playsound3
- Miniaudio - https://github.com/irmen/pyminiaudio
- SoundCard -https://github.com/bastibe/SoundCard

### Playsound3

Playsound3 je opravdu velmi jednoduchá a efektivní knihovna pro přehrávání zvuku.
Playsound3 podporuje pouze přehrávání a to formátů wav a mp3 - další formáty jsou závislé na platformě a použitém zvukovém backendu.
Nahrávání zvuků není podporováno.
Pro instalaci: `pip install playsound3`.

```python
from playsound3 import playsound

# přehrávání z disku by default blokuje
playsound("samples/piano_loop.wav") # můžeme nahradit URL!

# pro neblokující přehrávání použijeme argument block=False
sound = playsound("samples/piano_loop.wav", block=False)

# můžeme zkontrolovat, jestli se zvuk stále přehrává
if sound.is_alive():
    print("Sound is still playing!")

# kdykoliv můžeme přehrávání zastavit
sound.stop()
# pripadne bysme taky mohlyi pockat skrze sound.wait()
```

#### Zjištění dostupných backendů

Playsound3 používá pro přehrávání zvuku různé backendy v závislosti na platformě a dostupnosti knihoven.
Pro zjištění, které backendy jsou dostupné na našem systému, můžeme použít následující kód:

```python
from playsound3 import AVAILABLE_BACKENDS, DEFAULT_BACKEND

print(AVAILABLE_BACKENDS)  # for example: ["gstreamer", "ffmpeg", ...]
print(DEFAULT_BACKEND)  # for example: "gstreamer"
```


### Miniaudio

Podporuje přehrávání wav, flac, vorbis a mp3.
Umožňuje také nahrávání zvuku z mikrofonu.

Jednoduchý příklad přehrávání zvuku pomocí miniaudio vypadá takto:

```python
import miniaudio

## Můžeme zobrazit info o souboru
info = miniaudio.get_file_info("samples/piano_loop.wav")
print(f"Loading file: {info}") 

# načtení souboru do paměti
stream = miniaudio.stream_file("samples/piano_loop.wav")

# vytvoření přehrávacího zařízení - volbu necháváme na defaults miniaudio
# mělo by do vzít aktuálně používané zařízení v OS
with miniaudio.PlaybackDevice() as device:
    device.start(stream) # spustíme non-blocking přehrávání
    input("Audio file playing in the background. Enter to stop playback: ") # čekáme na vstup od uživatele, jinak by skriptu skončil a přehrávání by se zastavilo
```

Samozřejmě device nemusíme otevírat skrze `with .. as ..`, ale pak musíme dbát na zavření device:

```python
import miniaudio

stream = miniaudio.stream_file("samples/piano_loop.wav")

# otevření device bez with..as - nezapomenout na konci zavřit!
device = miniaudio.PlaybackDevice()
device.start(stream) # spustíme non-blocking přehrávání
input("Audio file playing in the background. Enter to stop playback: ")

print("Closing the playback device manually...")
device.close() # bez with..as musíme device manuálně zavřít
```

#### Informace o zařízeních

Knihovna nám umožňuje zobrazit informace o dostupných přehrávacích a nahrávacích zařízeních:

```python
import miniaudio

devices = miniaudio.Devices()
playbacks = devices.get_playbacks()
captures = devices.get_captures()

print("Playback devices:")
for playback in playbacks:
    print(f"- {playback}")

print("\nCapture devices:")
for capture in captures:
    print(f"- {capture}")
```

Což později můžeme využít pro výběr konkrétního zařízení pro přehrávání nebo nahrávání, například takto:

```python
import miniaudio

devices = miniaudio.Devices()
playbacks = devices.get_playbacks()

for x, device in enumerate(playbacks):
    print(f"{x}: {device['name']} (id: {device['id']})")

x = int(input("Choose playback device number: "))
chosen_device = playbacks[x]
chosen_id = chosen_device["id"]
print(f"Chosen device: {chosen_device['name']} (id: {chosen_id})")

device = miniaudio.PlaybackDevice(device_id = chosen_id)

stream = miniaudio.stream_file("samples/piano_loop.wav")
device.start(stream)
input("Enter to stop playback...")

device.close()
```

#### Nahrávání zvuku z mikrofonu

Pro nahrávání zvuku z mikrofonu můžeme použít `miniaudio.CaptureDevice()` a jeho metodu `start()`.
Metodě `start()` musíme předat generator, který bude zpracovávat nahrávané PCM data.

Celý example mužeme najít v souboru [miniaudio_recording.py](miniaudio_recording.py).


## Sound processing in real time
### Pedalboard
Pokud chceme v reálnem čase efektovat zvuk, je ideálním řešením knihovna [Pedalboard](https://github.com/spotify/pedalboard) od Spotify.
Je možné ji použít jak pro přímé zpraování živého vstupu do efektů a živého výstupu, tak pro zpracování zvukových souborů.

Instalace jednoduchá:
```
pip install pedalboard
```

Ukázky použití v souborech:
- [pedalboard_hello.py](pedalboard_hello.py)
- [pedalboard_file2speakers.py](pedalboard_file2speakers.py)
- [pedalboard_mic2speakers.py](pedalboard_mic2speakers.py)
- [pedalboard_reversed_reverb.py](pedalboard_reversed_reverb.py)

## Další knihovny pro práci se zvukem 

### Pydub

Populární knihovna, ale poslední aktualizace je z roku 2022.
V případě nouze se ale asi dá použít...
https://github.com/jiaaro/pydub


### Soundfile

Pro zápis a čtení zvukových souborů.
https://github.com/bastibe/python-soundfile

## CREDITS

piano_loops.wav is a sound [Piano loops 200 octave short loop 120 bpm](https://freesound.org/people/josefpres/sounds/841765/)
by [Josef Pres](https://freesound.org/people/josefpres/)

kick.wav is a sound [Kick - Proper Bottom.wav](https://freesound.org/people/TechGeekMusic/sounds/353396/)
by [TechGeekMusic](https://freesound.org/people/TechGeekMusic/)

voice.mp3 is a sound [Shoutout Twice Female Voice](https://freesound.org/people/miradeshazer/sounds/382759/)
by [miradeshazer](https://freesound.org/people/miradeshazer/)

Thank you all!

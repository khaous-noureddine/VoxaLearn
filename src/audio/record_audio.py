import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from pathlib import Path
import keyboard


def record_audio(
    output_path: str = "recordings/output.wav",
    sample_rate: int = 16000,
) -> str:
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    print("Press SPACE to start recording...")
    keyboard.wait("space")
    print("Recording... Press SPACE again to stop.")

    frames = []

    def callback(indata, frames_count, time, status):
        frames.append(indata.copy())

    stream = sd.InputStream(
        samplerate=sample_rate,
        channels=1,
        dtype="float32",
        callback=callback,
    )

    stream.start()

    keyboard.wait("space")
    stream.stop()
    stream.close()

    audio = np.concatenate(frames, axis=0)
    audio = np.squeeze(audio)
    audio_int16 = np.int16(audio * 32767)

    write(out, sample_rate, audio_int16)

    return str(out)
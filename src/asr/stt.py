import whisper
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline


# ---------- Whisper ----------
_whisper_model = None
def _load_whisper():
    global _whisper_model
    if _whisper_model is None:
        _whisper_model = whisper.load_model("base")
    return _whisper_model


# ---------- Kyutai STT ----------
_kyutai_pipe = None
def _load_kyutai():
    global _kyutai_pipe
    if _kyutai_pipe is None:
        model_id = "kyutai/stt-1b-en_fr"
        pipe = pipeline(
            task="automatic-speech-recognition",
            model=AutoModelForSpeechSeq2Seq.from_pretrained(model_id),
            tokenizer=AutoProcessor.from_pretrained(model_id),
            return_timestamps=False
        )
        _kyutai_pipe = pipe
    return _kyutai_pipe


# ---------- Unified API ----------
def transcribe_audio(path: str, engine="whisper") -> str:
    engine = engine.lower()

    if engine == "whisper":
        model = _load_whisper()
        out = model.transcribe(path)
        return out["text"]

    elif engine == "kyutai":
        pipe = _load_kyutai()
        out = pipe(path)
        return out["text"]

    else:
        raise ValueError(f"Unknown STT engine: {engine}. Use 'whisper' or 'kyutai'.")
from src.audio.record_audio import record_audio
from src.asr.stt import transcribe_audio
from src.feedback.llm import generate_feedback





def main():
    print("Recording...")
    audio_path = record_audio(
        output_path="recordings/output.wav"
    )

    print("\nTranscribing...")
    spoken_text = transcribe_audio(
        path = audio_path,
        engine = "whisper"
    )
    print("You said:", spoken_text)
    
    
    
    target = "I have been learning English for two years."
    native = "French"
    
    feedback = generate_feedback(target, spoken_text, native)
    print("\n--- FEEDBACK FROM LOCAL MODEL ---\n")
    print(feedback)
    

if __name__ == "__main__":
    main()






# def main():
#     target = "I have been learning English for two years."
#     native = "French"

#     audio_path = record_audio()
#     spoken_text = transcribe_audio(audio_path, engine="whisper")

#     print("You said:", spoken_text)

#     feedback = generate_feedback_local(target, spoken_text, native)
#     print("\n--- FEEDBACK FROM LOCAL MODEL ---\n")
#     print(feedback)

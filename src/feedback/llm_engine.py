from feedback.llm import lmstudio_llm

def generate_feedback_local(target: str, spoken: str, native: str = "French"):
    prompt = f"""
You are a language tutor.

Target sentence: "{target}"
User said: "{spoken}"
User's native language: {native}

Give:
- Whether the sentence is correct.
- List all mistakes.
- The corrected version.
- An explanation in the user's native language.
- A score from 0 to 100.

Keep the answer short and structured.
"""

    return lmstudio_llm(prompt)

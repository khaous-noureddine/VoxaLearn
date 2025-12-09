import requests

# ------------------------------
# CONFIG
# ------------------------------
# Replace with your LM Studio server URL shown in the GUI (Server Settings)
LMSTUDIO_URL = "http://10.230.0.47:1234/v1/chat/completions"

# Replace with the model name shown under “API Identifier” in LM Studio
DEFAULT_MODEL = "llama-3.2-1b-instruct"


# ------------------------------
# LOW-LEVEL LLM CALL
# ------------------------------
def lmstudio_query(prompt: str, model: str = DEFAULT_MODEL) -> str:
    """Send a prompt to the local LM Studio server."""
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
    }

    response = requests.post(LMSTUDIO_URL, json=payload)
    response.raise_for_status()
    data = response.json()

    return data["choices"][0]["message"]["content"]


# ---------------
# FEEDBACK ENGINE
# ---------------
def generate_feedback(target: str, spoken: str, native: str = "French") -> str:
    prompt = f"""
You are a language-learning tutor.

Target sentence: "{target}"
User said: "{spoken}"
User's native language: {native}

Provide:
1. Whether the sentence is correct.
2. A list of all mistakes (grammar, vocabulary, word order).
3. The corrected sentence.
4. A short explanation in the user's native language.

Keep it short and structured.
"""

    return lmstudio_query(prompt)


# ------------------------------
# OPTIONAL: quick manual test
# ------------------------------
if __name__ == "__main__":
    # Example usage
    target_sentence = "I have been learning English for two years."
    spoken_sentence = "I have learn English for two year."

    print("\n--- FEEDBACK ---\n")
    print(generate_feedback(target_sentence, spoken_sentence))
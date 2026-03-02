import requests

def generate_flashcards(text):
    if not text.strip():
        return [("Error", "No text provided.")]

    text = text[:2000]  # prevent memory overload

    prompt = f"""
Create 5 flashcards from the text below.
Format EXACTLY like this:

Q: Question here
A: Answer here

Text:
{text}
"""

    try:
        response = requests.post(
        "http://localhost:11434/api/generate",
    json={
        "model": "phi3",   # or mistral if you insist
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_ctx": 1024,     # reduce memory usage
            "num_predict": 200,  # limit output size
            "temperature": 0.7
        }
    },
    timeout=500
)

        response.raise_for_status()
        if response.status_code != 200:
            return [("Error", response.text)]
        result = response.json().get("response", "")

    except Exception as e:
        return [("Error", f"Ollama request failed: {str(e)}")]

    # Parse output safely
    flashcards = []
    question = None

    for line in result.split("\n"):
        line = line.strip()
        if line.startswith("Q:"):
            question = line[2:].strip()
        elif line.startswith("A:") and question:
            answer = line[2:].strip()
            flashcards.append((question, answer))
            question = None

    if not flashcards:
        return [("Error", "No flashcards generated. Check model output.")]

    return flashcards

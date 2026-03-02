# AI-Flashcard
# 📚 AI Flashcard Generator (Local LLM + Flask)

This project is a simple AI-powered flashcard generator built using:

- Python (Flask)
- Ollama (Local LLM)
- Phi-3 model (lightweight model for low RAM systems)
- PDF text extraction

It allows users to:
- Upload a PDF
- Or paste text manually
- Automatically generate flashcards in Q/A format

---

## 🚀 Why Phi-3?

This project uses **phi3** instead of larger models like mistral or llama3 because:

- My system has limited available RAM.
- Larger models require 4–5GB+ free memory.
- Phi-3 is lightweight and works reliably on lower-memory systems.
- It is ideal for small PDFs (KB-sized files).

⚠️ Currently tested with small PDFs (~KB size, around 100–300 words).

---

## 🧠 How It Works

1. User uploads a PDF or pastes text.
2. Text is extracted.
3. Text is sent to Ollama locally via API (`localhost:11434`).
4. Phi-3 generates 5 flashcards.
5. The app parses Q/A pairs and displays them.

Everything runs locally — no external API required.

---

# 🛠 Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd your-project-folder
2️⃣ Install Python Dependencies
pip install flask requests pymupdf
3️⃣ Install Ollama (Required)
Download Ollama

Go to:

👉 https://ollama.com/download

Download and install the Windows version.

After installation, open PowerShell and verify:

ollama --version
4️⃣ Download the Phi-3 Model

Run:

ollama pull phi3

This downloads the lightweight model used in this project.

5️⃣ Start Ollama Server

Before running Flask, make sure Ollama is running:

ollama serve

If it says "address already in use", it means Ollama is already running in the background.

6️⃣ Run the Flask App

In another terminal:

python app.py

Then open your browser:

http://127.0.0.1:5000
📂 Project Structure
project/
│
├── app.py
├── flashcard_generator.py
├── pdf_utils.py
├── templates/
│     └── index.html
└── README.md
⚠️ Limitations

Designed for small PDFs (KB-sized).

Large PDFs may fail due to RAM limits.

Scanned PDFs (image-based) will not work unless OCR is added.

Model output formatting may vary slightly.

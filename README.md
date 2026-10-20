# 📚 AI Flashcard Generator

A lightweight AI-powered flashcard generator that uses a **local Large Language Model (LLM)** to turn PDF content or pasted text into study questions and answers.

The application is built with **Python, Flask, Ollama, and PyMuPDF**, with local inference through the **Phi-3** model.

> The project was designed to explore practical local LLM application development on hardware with limited memory.

---

## ✨ Features

- 📄 Upload a PDF and extract its text
- ✍️ Paste text directly into the application
- 🤖 Generate AI-powered question-and-answer flashcards
- 🧠 Run LLM inference locally using Ollama
- 🔒 Keep document content and inference on the local machine
- 🃏 Display generated flashcards through a web interface
- ⚡ Lightweight setup suitable for resource-constrained systems

---

## 🏗️ Architecture

```text
                  User
                   │
             PDF / Text Input
                   │
                   ▼
            ┌─────────────┐
            │    Flask    │
            │  Web App    │
            └──────┬──────┘
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
     PyMuPDF          Text Input
   PDF Extraction          │
          │                │
          └────────┬───────┘
                   ▼
             Prompt Builder
                   │
                   ▼
              Ollama API
             localhost:11434
                   │
                   ▼
                Phi-3
             Local LLM
                   │
                   ▼
            Q/A Flashcards
                   │
                   ▼
              Web Interface
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Application development |
| **Flask** | Web application and HTTP handling |
| **Ollama** | Local LLM inference |
| **Phi-3** | Lightweight local language model |
| **PyMuPDF** | PDF text extraction |
| **HTML/CSS** | Flashcard interface |

---

## 🧠 How It Works

1. The user uploads a PDF or enters text manually.
2. PDF content is extracted using **PyMuPDF**.
3. The extracted/input text is passed to the flashcard generation component.
4. A prompt is sent to the local **Ollama API**.
5. **Phi-3** generates question-and-answer pairs.
6. The application parses the generated output.
7. The resulting flashcards are displayed through the Flask interface.

The application communicates with Ollama locally through:

```text
http://localhost:11434
```

No external LLM API is required.

---

## 💡 Engineering Decisions

### Why use a local LLM?

The application was designed around local inference rather than a hosted AI API.

This provides:

- Local processing of document content
- No external AI API dependency
- No API key requirement
- An inexpensive development environment
- A practical way to experiment with LLM applications on local hardware

### Why Phi-3?

The original implementation was developed on a system with limited available RAM.

Larger models such as Mistral or Llama can require significantly more memory, while Phi-3 provides a lightweight option for experimentation and smaller documents.

The model can be changed through Ollama depending on available hardware.

---

## 🚀 Getting Started

### Prerequisites

Install:

- Python 3.x
- Ollama

Verify Ollama:

```bash
ollama --version
```

### 1. Clone the repository

```bash
git clone https://github.com/Cooky09/AI-Flashcard.git
cd AI-Flashcard
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the Phi-3 model

```bash
ollama pull phi3
```

### 4. Start Ollama

If Ollama is not already running:

```bash
ollama serve
```

Ollama runs locally on:

```text
http://localhost:11434
```

### 5. Start the Flask application

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```text
AI-Flashcard/
│
├── app.py
├── flashcard_generator.py
├── pdf_utils.py
├── requirements.txt
├── templates/
│   └── index.html
├── .gitignore
└── README.md
```

### Key components

**`app.py`**

Flask application and web request handling.

**`flashcard_generator.py`**

Handles communication with Ollama and flashcard generation.

**`pdf_utils.py`**

Extracts text from uploaded PDF documents.

**`templates/index.html`**

Provides the web interface for uploading content and displaying flashcards.

---

## ⚠️ Current Limitations

The current implementation is intentionally lightweight.

- Large PDFs may exceed the practical context or memory available to the local model.
- Scanned/image-based PDFs require OCR before text can be extracted.
- LLM output formatting can vary.
- The application currently targets relatively small documents.
- Flashcard quality depends on the selected local model and source text.

---

## 🔮 Potential Improvements

Possible future improvements include:

- OCR support for scanned documents
- Structured JSON output validation
- Better handling of large documents through chunking
- Configurable number of flashcards
- Multiple Ollama model selection
- Automated testing
- Docker-based deployment
- Persistent flashcard storage
- User accounts and saved study sets
- Improved evaluation of generated flashcard quality

---

## 🎯 Project Purpose

This project represents an early stage of my exploration into **local LLM application development**.

It demonstrates the fundamentals of integrating a locally hosted language model into a web application, processing user-provided documents, constructing prompts, and turning model output into a usable application feature.

It also provides the foundation for my later work with **RAG, semantic search, AI agents, evaluation, and production-oriented AI systems**.
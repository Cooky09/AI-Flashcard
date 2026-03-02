from flask import Flask, render_template, request
from flashcard_generator import generate_flashcards
from pdf_utils import extract_text_from_pdf

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    flashcards = None

    if request.method == "POST":
        if "file" in request.files and request.files["file"].filename != "":
            file = request.files["file"]
            text = extract_text_from_pdf(file)
        else:
            text = request.form["text"]

        flashcards = generate_flashcards(text)

    return render_template("index.html", flashcards=flashcards)


if __name__ == "__main__":
    app.run(debug=True)
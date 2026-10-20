from io import BytesIO

from pdf_utils import extract_text_from_pdf


class FakePage:
    def __init__(self, text):
        self.text = text

    def extract_text(self):
        return self.text


class FakeReader:
    def __init__(self, pages):
        self.pages = pages


def test_extract_text_skips_pages_without_text(monkeypatch):
    def fake_pdf_reader(_file):
        return FakeReader([
            FakePage("First page"),
            FakePage(None),
            FakePage("Third page"),
        ])

    monkeypatch.setattr(
        "pdf_utils.PyPDF2.PdfReader",
        fake_pdf_reader,
    )

    result = extract_text_from_pdf(BytesIO(b"fake pdf"))

    assert result == "First pageThird page"

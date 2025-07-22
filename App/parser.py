from docx import Document

def extract_text(path: str) -> str:
    """
    Read a PDF or DOCX at `path` and return its raw text.
    Raise ValueError on unsupported types.
    """
    ext = path.lower().split('.')[-1]# make it lowercase to handle all inputs and check the last element in case of multiple items after .
    if ext == "pdf":
        import fitz  # PyMuPDF
        doc = fitz.open(path)
        full_text = []
        for page in doc:
            full_text.append(page.get_text())
        return "\n".join(full_text)

    elif ext == "docx":
        from docx import Document
        doc = Document(path)
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n".join(paragraphs)


    else:
        raise ValueError(f"Unsupported file type: {ext}")


def clean_text(raw: str) -> str:
    """
    Normalize whitespace, remove headers/footers noise,
    unify line breaks, strip out non-printable chars.
    """
    pass


def segment_plaintext(text: str) -> list[str]:
    """
    For job descriptions in .txt form,
    maybe just split on double newlines or headings.
    Returns list of paragraphs or sections.
    """
    pass





from docx import Document
import pdfplumber

def parse_pdf_resume(file_stream):
    with pdfplumber.open(file_stream) as pdf:
        text = '\n'.join(page.extract_text() for page in pdf.pages if page.extract_text())
    return extract_resume_data(text)

def parse_docx_resume(file_stream):
    doc = Document(file_stream)
    text = '\n'.join(p.text for p in doc.paragraphs)
    return extract_resume_data(text)

def extract_resume_data(text):
    return {
        "hero": {"name": "John Doe", "bio": "A passionate software developer."},
        "about": {"summary": "Experienced in Python and Flask."},
        "skills": ["Python", "Flask", "REST APIs"],
        "experience": ["Software Engineer at XYZ"],
        "education": ["MCA, GLA University"]
    }

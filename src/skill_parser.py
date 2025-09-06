import os
import re
from PyPDF2 import PdfReader
from docx import Document

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + " "
    return text

def extract_text_from_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    elif file_path.endswith(".txt"):
        return extract_text_from_txt(file_path)
    else:
        return ""

def extract_skills(text, skills_list):
    return [skill for skill in skills_list if skill.lower() in text.lower()]

def extract_email(text):
    emails = re.findall(r'\S+@\S+', text)
    return emails[0] if emails else None

def extract_phone(text):
    phones = re.findall(r'\+?\d[\d -]{8,12}\d', text)
    return phones[0] if phones else None

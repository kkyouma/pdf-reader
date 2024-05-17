import PyPDF2
import sys
import re

examen_2024 = "data/muestra_pdf.pdf"

with open(examen_2024, "rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)

    text = ""

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

# Redireccionar la salida estándar a un archivo
with open("output.txt", "w", encoding="utf-8") as output_file:
    sys.stdout = output_file
    print(text)

from pdf2docx import Converter
import os
import uuid

def convert_pdf_to_docx(uploaded_file):
    unique_id = uuid.uuid4().hex
    input_path = f"temp_{unique_id}.pdf"
    output_path = f"converted_{unique_id}.docx"

    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    cv = Converter(input_path)
    cv.convert(output_path, start=0, end=None)
    cv.close()

    os.remove(input_path)

    return output_path

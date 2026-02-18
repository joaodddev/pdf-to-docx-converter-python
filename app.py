import streamlit as st
from converter import convert_pdf_to_docx
import os

st.set_page_config(page_title="PDF to DOCX Converter", layout="centered")

st.title("📄 PDF → DOCX Converter")
st.markdown("Faça upload de um ou mais arquivos PDF para converter automaticamente.")

uploaded_files = st.file_uploader(
    "Selecione os arquivos PDF",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        with st.spinner(f"Convertendo {uploaded_file.name}..."):
            try:
                output_path = convert_pdf_to_docx(uploaded_file)

                with open(output_path, "rb") as file:
                    st.download_button(
                        label=f"📥 Baixar {uploaded_file.name.replace('.pdf', '.docx')}",
                        data=file,
                        file_name=uploaded_file.name.replace(".pdf", ".docx"),
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )

                os.remove(output_path)

            except Exception as e:
                st.error(f"Erro ao converter {uploaded_file.name}: {e}")

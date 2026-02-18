import streamlit as st
from converter import convert_pdf_to_docx
import os

# Configuração da página
st.set_page_config(
    page_title="DocuConvert | PDF to DOCX",
    page_icon="📄",
    layout="centered"
)

# ===== CSS Customizado =====
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.05);
    }
    .stButton>button {
        background-color: #4F46E5;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #4338CA;
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ===== Header =====
st.title("📄 DocuConvert")
st.markdown("### Converta seus PDFs em DOCX de forma rápida e profissional")

st.divider()

# ===== Upload =====
uploaded_files = st.file_uploader(
    "Arraste ou selecione seus arquivos PDF",
    type=["pdf"],
    accept_multiple_files=True
)

# ===== Conversão =====
if uploaded_files:
    for uploaded_file in uploaded_files:
        with st.spinner(f"Convertendo {uploaded_file.name}..."):
            try:
                output_path = convert_pdf_to_docx(uploaded_file)

                st.success(f"{uploaded_file.name} convertido com sucesso!")

                with open(output_path, "rb") as file:
                    st.download_button(
                        label=f"⬇️ Baixar {uploaded_file.name.replace('.pdf', '.docx')}",
                        data=file,
                        file_name=uploaded_file.name.replace(".pdf", ".docx"),
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )

                os.remove(output_path)

            except Exception as e:
                st.error(f"Erro ao converter {uploaded_file.name}: {e}")

st.divider()

# ===== Footer =====
st.caption("© 2026 DocuConvert • Desenvolvido em Python + Streamlit")

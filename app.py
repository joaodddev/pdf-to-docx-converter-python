import streamlit as st
from converter import convert_pdf_to_docx
import os
import time

# ==============================
# CONFIGURAÇÃO DA PÁGINA
# ==============================
st.set_page_config(
    page_title="DocuConvert | PDF to DOCX",
    page_icon="📄",
    layout="centered"
)

# ==============================
# CSS CUSTOMIZADO (Visual SaaS)
# ==============================
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

# ==============================
# HEADER
# ==============================
st.title("📄 DocuConvert")
st.markdown("### Converta seus PDFs em DOCX de forma rápida e profissional")

st.divider()

# ==============================
# SIDEBAR
# ==============================
with st.sidebar:
    st.header("📌 Sobre o Projeto")
    st.write(
        "Aplicação web para conversão automática de arquivos PDF para DOCX."
    )
    st.write("Desenvolvido com:")
    st.write("- Python")
    st.write("- Streamlit")
    st.write("- pdf2docx")
    st.divider()
    st.subheader("⚙️ Como funciona?")
    st.write("1️⃣ Faça upload do PDF")
    st.write("2️⃣ O sistema converte automaticamente")
    st.write("3️⃣ Baixe o arquivo convertido")

# ==============================
# UPLOAD
# ==============================
uploaded_files = st.file_uploader(
    "Arraste ou selecione seus arquivos PDF",
    type=["pdf"],
    accept_multiple_files=True
)

# ==============================
# MÉTRICA ESTILO SAAS
# ==============================
if uploaded_files:
    st.metric("📂 Arquivos enviados", len(uploaded_files))

    st.divider()

    for uploaded_file in uploaded_files:
        with st.spinner(f"Convertendo {uploaded_file.name}..."):
            try:
                time.sleep(1)  # pequena pausa para UX
                output_path = convert_pdf_to_docx(uploaded_file)

                st.success(f"✅ {uploaded_file.name} convertido com sucesso!")

                with open(output_path, "rb") as file:
                    st.download_button(
                        label=f"⬇️ Baixar {uploaded_file.name.replace('.pdf', '.docx')}",
                        data=file,
                        file_name=uploaded_file.name.replace(".pdf", ".docx"),
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )

                os.remove(output_path)

            except Exception as e:
                st.error(f"❌ Erro ao converter {uploaded_file.name}: {e}")

# ==============================
# FOOTER
# ==============================
st.divider()
st.caption("© 2026 DocuConvert • Built with Python + Streamlit • Deploy via Streamlit Cloud")

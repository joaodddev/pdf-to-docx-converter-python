import streamlit as st
from converter import convert_pdf_to_docx
import utils
import os

st.set_page_config(page_title="DocuConvert", page_icon="📄")

st.title("📄 DocuConvert")
st.markdown("Conversão automática de PDF para DOCX")

uploaded_files = st.file_uploader(
    "Envie arquivos PDF",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    st.metric("Arquivos enviados", len(uploaded_files))

    for uploaded_file in uploaded_files:

        valido, erro = utils.validar_arquivo(uploaded_file)

        if not valido:
            st.error(erro)
            continue

        with st.spinner("Convertendo..."):
            try:
                output_path = convert_pdf_to_docx(uploaded_file)

                st.success(f"{uploaded_file.name} convertido com sucesso!")

                with open(output_path, "rb") as file:
                    st.download_button(
                        label="Baixar DOCX",
                        data=file,
                        file_name=output_path,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )

                os.remove(output_path)

            except Exception as e:
                st.error(f"Erro: {e}")

st.divider()
st.caption("Python • Streamlit • pdf2docx • Deploy via Streamlit Cloud")

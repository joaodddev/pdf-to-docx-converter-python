def validar_arquivo(uploaded_file):
    if uploaded_file is None:
        return False, "Nenhum arquivo enviado."

    if not uploaded_file.name.lower().endswith(".pdf"):
        return False, "Arquivo precisa ser PDF."

    return True, None

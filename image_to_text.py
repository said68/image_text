import streamlit as st
from PIL import Image
import pytesseract

def extract_text_from_image(image):
    # Convertir l'image en texte
    text = pytesseract.image_to_string(image)
    return text

st.title('Application OCR avec Streamlit')

uploaded_file = st.file_uploader("Choisissez une image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Image téléchargée', use_column_width=True)
    st.write("")

    if st.button('Extraire'):
        with st.spinner("Conversion en cours..."):
            text = extract_text_from_image(image)
        st.write("Texte extrait :")
        st.write(text)

    if st.button('Initialiser'):
        st.experimental_rerun()

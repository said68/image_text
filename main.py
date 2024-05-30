import streamlit as st
from PIL import Image
import io
from google.cloud import vision
from google.oauth2 import service_account
import os
import json

# Charger les credentials depuis la variable d'environnement
credentials_info = json.loads(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
credentials = service_account.Credentials.from_service_account_info(credentials_info)
client = vision.ImageAnnotatorClient(credentials=credentials)

def extract_text_from_image(image):
    content = io.BytesIO()
    image.save(content, format='PNG')
    image_content = content.getvalue()
    
    image = vision.Image(content=image_content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    if texts:
        return texts[0].description
    else:
        return "Aucun texte détecté"

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

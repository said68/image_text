#!/usr/bin/env bash
apt-get update
apt-get install -y tesseract-ocr tesseract-ocr-fra
streamlit run main.py --server.port 8080

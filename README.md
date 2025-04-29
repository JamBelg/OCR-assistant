# 🚀 OCR Assistant

A lightweight and intuitive Streamlit application that uses **LLMs and image input** to extract structured text from uploaded images. This app serves as an intelligent OCR (Optical Character Recognition) assistant powered by **[Ollama](https://ollama.com/)** and models like **Gemma3**.

![App Screenshot](screenshot.png) <!-- Optional: Add a screenshot of your app here -->

---

## 🧠 Features

- Upload any image file (PNG, JPG, BMP, GIF, etc.)
- Automatically extract and structure text using a Large Language Model
- Clean, modern UI with Streamlit
- Responsive layout with sidebar controls
- Error handling and OCR fallback messaging

---

## 🔧 Technologies Used

- [Streamlit](https://streamlit.io/): for creating the web app UI
- [Ollama](https://ollama.com/): for local LLM inference
- [Gemma3](https://ollama.com/library/gemma): open-source LLM used for OCR extraction
- [Pillow](https://python-pillow.org/): for image processing

---

## 📦 Installation

1. **Install dependencies**  
   Make sure Python 3.8+ is installed, then run:

   ```bash
   pip install -r requirements.txt

2. **Run app**  
   Launch the streamlit application:

   ```bash
   streamlit run streamlit-app.py

import streamlit as st
import ollama
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Streamlit OCR",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown('<h1 style="text-align: left;">🚀 OCR Assistant</h1>', unsafe_allow_html=True)

# Columns
col1, col2 = st.columns([5,2])
with col2:
    if st.button("Clear 🗑️"):
        if 'ocr_output' in st.session_state:
            del st.session_state['ocr_output']
        st.rerun()

st.markdown('<p style="margin-top: -20px;">Extract structured text from images</p>', unsafe_allow_html=True)
st.markdown("---")

# Move upload controls to sidebar
with st.sidebar:
    st.header("Upload your image")
    uploaded_file = st.file_uploader("Select an image...", type=['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'], label_visibility="collapsed")
    
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image")
        
        if st.button("Extract Text 🔍", type="primary"):
            with st.spinner("Processing image..."):
                try:
                    response = ollama.chat(
                        model='gemma3:12b', #gemma3:27b
                        messages=[{
                            'role': 'user',
                            'content': """You are an OCR assistant. Analyze the image and extract structured text from it.
                            Provide the text in a clear and organized format. 
                            If the image is not clear, inform the user that you cannot extract text from it.""",

                            'images': [uploaded_file.getvalue()]
                        }]
                    )
                    st.session_state['ocr_output'] = response.message.content
                except Exception as e:
                    st.error(f"Error processing image: {str(e)}")

#Results
if 'ocr_output' in st.session_state:
    st.markdown(st.session_state['ocr_output'])
else:
    st.info("Upload an image and click 'Extract Text' to see the results.")

# Footer
st.markdown("---")
st.markdown("Made with Streamlit and Ollama")
st.markdown("Make sure to install Ollama and Gemma3. Check out the [Ollama](https://ollama.com/) and [Streamlit](https://streamlit.io/) documentation for more information.")
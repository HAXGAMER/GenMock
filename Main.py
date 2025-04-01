pip install fastapi uvicorn pillow streamlit requests numpy opencv-python pydantic python-multipart moviepy
import streamlit as st
import requests
from PIL import Image
import io

# Streamlit UI setup
st.title("AI Mockup Generator 🎨")

# File upload for base image (T-shirt) and design
base_image = st.file_uploader("Upload Blank T-Shirt Image", type=["png", "jpg", "jpeg"])
design_image = st.file_uploader("Upload Design Image", type=["png", "jpg", "jpeg"])

if base_image and design_image:
    st.image(base_image, caption="Blank T-Shirt", use_column_width=True)
    st.image(design_image, caption="Design", use_column_width=True)

    if st.button("Generate Mockup"):
        files = {
            "base_image": base_image.getvalue(),
            "design_image": design_image.getvalue(),
        }
        response = requests.post("http://127.0.0.1:8000/generate-mockup/", files=files)

        if response.status_code == 200:
            mockup_path = response.json()["file"]
            st.image(mockup_path, caption="Generated Mockup", use_column_width=True)
        else:
            st.error("Error generating mockup")

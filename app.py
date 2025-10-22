import streamlit as st
from PIL import Image
from utils import predict_flatfoot

st.title("🦶 AI Chuẩn đoán bàn chân bẹt")

uploaded_file = st.file_uploader("Tải ảnh bàn chân lên", type=["jpg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Ảnh đã tải", use_column_width=True)
    result = predict_flatfoot(image)
    st.success(f"Kết quả: {result}")
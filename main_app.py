import streamlit as st
from PIL import Image

# text
st.title("おみくじアプリ")
st.caption("今日の運勢はどうかな？")

# image
image = Image.open("./pic/pic.png")
st.image(image, width=200)

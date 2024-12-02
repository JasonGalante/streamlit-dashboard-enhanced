import streamlit as st
import pandas as pd
from PIL import Image
import io
st.header("Jason Galante 2024 AHI 507 Streamlit Example")
st.subheader("Proof of concept")

st.text("""And everyone clapped.""")


# Display a GIF
gif_path = "C:\\Users\\grift\\OneDrive\\Documents\\GitHub\\streamlit-dashboard-enhanced\\clap gif.webp" 
st.image(gif_path, caption="Your GIF", use_container_width=True)

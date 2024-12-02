import streamlit as st
import pandas as pd
from PIL import Image
import io
st.header("Jason Galante 2024 AHI 507 Streamlit Example")
st.subheader("Proof of concept")

st.text("""And everyone clapped.""")


# Display a GIF
st.image("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHU0bzFlMjNkeDFjNWFpZnlldHEzYnNyejZtdnQ3ODlhOG5xaWdrNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zGnnFpOB1OjMQ/giphy.gif", caption="Online GIF")
st.image(gif_path, caption="Your GIF", use_container_width=True)

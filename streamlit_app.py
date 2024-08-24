import numpy as np
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

# UI
st.title("Streamlit Example")
col1, col2 = st.columns(2)

with col1:
    st.header("Small Dataset - Max 1,000 samples")
    num_1 = st.slider("Pick a number:", 100, 1000, value=100, step=100, key=1)
    x_small, y_small = np.random.rand(num_1), np.random.rand(num_1)
    st.plotly_chart(px.scatter(x=x_small, y=y_small))
with col2:
    st.header("Large Dataset - Max 1,000,000 samples")
    num_2 = st.slider(
        "Pick a number:",
        50000,
        1000000,
        value=50000,
        step=50000,
        key=2,
    )
    x_large, y_large = np.random.rand(num_2), np.random.rand(num_2)
    st.plotly_chart(px.scatter(x=x_large, y=y_large, opacity=0.5))

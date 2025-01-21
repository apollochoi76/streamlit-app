import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")
col1, col2 = st.columns([0.3, 0.7])
data = np.random.randn(10, 1)

# def main():   
with col1:
# st.title('This is title')
# st.header('This is header')
# st.subheader('This is subheader')
        col1.subheader('Chart')
        col1.line_chart(data)

with col2:
        col2.subheader('Data')
        col2.write(data)
# view = [100, 150, 30]
# st.write('# Title 1')
# st.write('## Title 2')
# st.bar_chart(view)
# sview = pd.DataFrame(view)
# sview

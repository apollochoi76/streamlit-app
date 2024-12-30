import streamlit as st
import pandas as pd

view = [100, 150, 30]
st.write('# Title 1')
st.write('## Title 2')
st.bar_chart(view)
sview = pd.DataFrame(view)
sview

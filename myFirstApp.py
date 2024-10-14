import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({'first column': [1,2,3,4], 'second colomn': [10,20,30,40]})

st.write("Here's our first attempt at using data to creat a table:")
st.write(pd.DataFrame({'first column': [1,2,3,4], 'second colomn': [10,20,30,40]}))

st.table(df)

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)
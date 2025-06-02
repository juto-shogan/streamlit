import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Create two columns
col1, col2 = st.columns(2)

# First plot in the first column
with col1:
    st.header("Plot 1")
    fig1, ax1 = plt.subplots()
    ax1.plot(np.random.randn(10))
    st.pyplot(fig1)

# Second plot in the second column
with col2:
    st.header("Plot 2")
    fig2, ax2 = plt.subplots()
    ax2.plot(np.random.randn(10), color='orange')
    st.pyplot(fig2)
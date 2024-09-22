import streamlit as st

# Sample data (replace with your actual data)
data = {
    "Retailer": ["Foot Locker", "Walmart", "Sports Direct", "West Gear", "Kohl's", "Amazon"],
    "Total Sales": [220000000, 100000000, 150000000, 250000000, 120000000, 100000000]
}

# Create columns
col1, col2 = st.columns(2)

# Display logo in the first column
with col1:
    st.image("/home/juto/Desktop/ML_libraries/streamlit/logo.jpeg")

# Display charts in the second column
with col2:
    st.title("Adidas Interactive Sales Dashboard")
    st.bar_chart(data)  # Example: Bar chart
    st.line_chart(data)  # Example: Line chart
    
    

# Add more charts and metrics as needed



import streamlit as st

# First row
col5, col6 = st.columns(2)
col5.write("This is column 1 in row 1")
col6.write("This is column 2 in row 1")

# Second row
col3, col4 = st.columns(2)
col3.write("This is column 1 in row 2")
col4.write("This is column 2 in row 2")

import streamlit as st
import pandas as pd

# Assume you have a DataFrame df
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Convert DataFrame to CSV data
csv = df.to_csv(index=False).encode()

# Create a button for downloading the data
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name="my_data.csv",
    mime="text/csv",
)
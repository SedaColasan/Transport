import streamlit as st
import pandas as pd

# Sample data

ireland = pd.read_csv("THA25 - Passenger Journeys by Public Transport.csv")

ireland = pd.DataFrame(ireland)

# Streamlit app
st.title('Transportation Dashboard')

# Display the dataframe
st.dataframe(ireland)

# Interactive components (e.g., filters, plots)
selected_week = st.selectbox('Select Week:', ireland['Week'].unique())
filtered_data = ireland[ireland['Week'] == selected_week]

st.bar_chart(filtered_data.groupby('Mode of Transport')['VALUE'].sum())


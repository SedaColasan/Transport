import streamlit as st
import pandas as pd
import altair as alt

# Load Ireland dataset
ireland = pd.read_csv("THA25 - Passenger Journeys by Public Transport.csv")

# Load UK dataset
uk = pd.read_csv("full_data_clean.csv")  # Replace "your_uk_dataset.csv" with the actual file path

# Streamlit app
st.title('Transportation Dashboard')

# Choose dataset using radio button
selected_dataset = st.radio("Select Dataset:", ["Ireland", "UK"])

if selected_dataset == "Ireland":
    selected_df = ireland
    category_column = 'Mode of Transport'
    value_column = 'VALUE'
else:
    selected_df = uk
    category_column = 'transport_type'  # Adjust column name as per your dataset
    value_column = 'value'  # Adjust column name as per your dataset

# Display the selected dataframe
st.dataframe(selected_df)

# Interactive components (e.g., filters, plots)
if selected_dataset == "Ireland":
    selected_week = st.selectbox('Select Week:', selected_df['Week'].unique())
    filtered_data = selected_df[selected_df['Week'] == selected_week]
else:
    # Convert 'date' column to datetime format
    if 'date' in selected_df.columns:
        selected_df['date'] = pd.to_datetime(selected_df['date'])
    
        # Provide a default date (you can adjust this based on your dataset)
        default_date = selected_df['date'].min()
        
        # Use date picker for interactive date selection
        selected_date = st.date_input('Select Date:', min_value=selected_df['date'].min(), max_value=selected_df['date'].max(), value=default_date)
        
        filtered_data = selected_df[selected_df['date'] == selected_date]
    else:
        # If there is no date column, use the entire dataframe
        filtered_data = selected_df

# Display bar chart with Altair
chart = alt.Chart(filtered_data).mark_bar().encode(
    x=alt.X(category_column, type='nominal'),
    y=alt.Y(value_column, type='quantitative')
).properties(width=600)

st.altair_chart(chart, use_container_width=True)

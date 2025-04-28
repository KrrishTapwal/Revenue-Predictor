# 📚 Import Libraries
import streamlit as st
import pandas as pd
import joblib

# 🛠 Load Data & Model
df = pd.read_csv('Cleaned_Dataset.csv')  # ✅ File renamed to generic name
model = joblib.load('multioutput_model.pkl')  # ✅ Model renamed to generic name

st.set_page_config(page_title="Financial Forecasting App", page_icon="📈", layout="wide")

st.title("📈 Financial Forecasting Application")

st.markdown("""
Welcome to the Financial Metrics Predictor!  
Use the sidebar to input your parameters and predict:
- Revenue
- Operating Income
- Net Income
""")

# 📋 Sidebar Inputs
st.sidebar.header('Input Parameters')

# Manual Year List including 2025 and 2026
year = st.sidebar.selectbox('Select Year:', [2020, 2021, 2022, 2023, 2024, 2025, 2026])

# Quarter
quarter_options = ['All'] + sorted(df['Quarter'].unique().tolist())
quarter = st.sidebar.selectbox('Select Quarter:', quarter_options)

# Region
region_options = ['All'] + sorted(df['Region'].unique().tolist())
region = st.sidebar.selectbox('Select Region:', region_options)

# Business Unit
business_unit_options = ['All'] + sorted(df['Business Unit'].unique().tolist())
business_unit = st.sidebar.selectbox('Select Business Unit:', business_unit_options)

# ✨ Filter Data Based on Inputs
df_filtered = df.copy()

if quarter != 'All':
    df_filtered = df_filtered[df_filtered['Quarter'] == quarter]

if region != 'All':
    df_filtered = df_filtered[df_filtered['Region'] == region]

if business_unit != 'All':
    df_filtered = df_filtered[df_filtered['Business Unit'] == business_unit]

# Dynamically get allowed Employee Counts
if not df_filtered.empty:
    employee_counts = sorted(df_filtered['Employee Count'].unique())
else:
    employee_counts = sorted(df['Employee Count'].unique())

employee_count = st.sidebar.selectbox('Select Employee Count:', employee_counts)

# 📋 Show the Input Summary
st.subheader('📝 Input Summary')
input_summary = {
    'Year': year,
    'Quarter': quarter if quarter != 'All' else 'Any',
    'Region': region if region != 'All' else 'Any',
    'Business Unit': business_unit if business_unit != 'All' else 'Any',
    'Employee Count': employee_count
}
st.table(pd.DataFrame([input_summary]))

# 🧠 Prepare Input for Model
input_data = pd.DataFrame({
    'Year': [year],
    'Quarter': [quarter if quarter != 'All' else df['Quarter'].mode()[0]],
    'Region': [region if region != 'All' else df['Region'].mode()[0]],
    'Business Unit': [business_unit if business_unit != 'All' else df['Business Unit'].mode()[0]],
    'Employee Count': [employee_count]
})

# 🚀 Predict Button
if st.button('Predict Revenue, Operating Income & Net Income'):
    prediction = model.predict(input_data)
    revenue_pred, operating_income_pred, net_income_pred = prediction[0]

    st.subheader('🎯 Predicted Results:')
    st.success(f"**Revenue (Million USD):** {revenue_pred:.2f}")
    st.success(f"**Operating Income (Million USD):** {operating_income_pred:.2f}")
    st.success(f"**Net Income (Million USD):** {net_income_pred:.2f}")

st.sidebar.markdown("---")
st.sidebar.markdown("Built with ❤️ by Krizz")



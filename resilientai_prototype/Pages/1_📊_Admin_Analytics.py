import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Admin Analytics — ResilientAI")

st.markdown("This page provides high-level insights for government agencies and emergency responders.")

col1, col2 = st.columns(2)

with col1:
    st.metric("Communities Monitored", "52")
    st.metric("Alerts Sent (Past 30 Days)", "1,284")

with col2:
    st.metric("High-Risk Events Predicted", "7")
    st.metric("Average Warning Time", "48 hours")

st.subheader("📈 Sample Alert Distribution")
st.bar_chart(pd.DataFrame({
    "Alerts": [500, 300, 200, 150, 134],
    "Region": ["Maiduguri", "Jere", "Konduga", "Guzamala", "Gamboru"]
}))

st.markdown("---")
st.caption("For demonstration purposes only.")
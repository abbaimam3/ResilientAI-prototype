import streamlit as st
import pandas as pd

st.title("🗺️ Flood Hotspot Map (Prototype)")

st.markdown("This page simulates geospatial visualization for flood-risk zones.")

df = pd.DataFrame({
    'lat': [11.83, 11.85, 11.81],
    'lon': [13.15, 13.19, 13.13],
    'risk': ['HIGH', 'MODERATE', 'LOW']
})

st.map(df)

st.markdown("---")
st.caption("Prototype geolocation data for Maiduguri axis.")
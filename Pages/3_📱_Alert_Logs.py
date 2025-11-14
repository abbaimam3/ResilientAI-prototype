import streamlit as st
import pandas as pd

st.title("📱 Alert Log History")

data = {
    "Timestamp": [
        "2025-01-05 14:21", "2025-01-05 10:11", 
        "2025-01-04 16:02", "2025-01-04 09:41"
    ],
    "Community": ["Gwange", "Bulabulin", "Muna", "Custom Area"],
    "Risk Level": ["High", "Moderate", "High", "Low"],
}

df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True)

st.markdown("---")
st.caption("Simulated dataset for demonstration.")
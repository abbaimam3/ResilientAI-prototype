import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="ResilientAI", layout="wide")

# HEADER
st.title("🌊 ResilientAI – Early Flood Warning System")
st.caption("Predict • Prepare • Protect")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/sample_flood_data.csv")

df = load_data()

# SIDEBAR INPUTS
st.sidebar.header("🌦️ Simulation Inputs")
rainfall = st.sidebar.slider("Rainfall (mm)", 0, 200, 60)
river = st.sidebar.slider("River Level (m)", 0.0, 10.0, 4.1)
soil = st.sidebar.slider("Soil Moisture (%)", 0, 100, 72)
temp = st.sidebar.slider("Temperature (°C)", 20, 45, 28)

# SIMPLE AI RISK MODEL
def compute_risk(rainfall, river, soil):
    score = (0.4 * rainfall) + (25 * river) + (0.3 * soil)
    return score

score = compute_risk(rainfall, river, soil)

def risk_label(score):
    if score < 120: return "LOW"
    if score < 250: return "MODERATE"
    return "HIGH"

risk = risk_label(score)

# PAGE LAYOUT
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Flood Risk Indicator")
    st.metric("Current Risk Level", risk, f"Score: {int(score)}")

    if risk == "HIGH":
        st.error("⚠️ HIGH RISK — Flooding likely within 24–72 hrs.")
    elif risk == "MODERATE":
        st.warning("🟧 MODERATE RISK — Stay alert.")
    else:
        st.success("🟩 LOW RISK — No immediate threat.")

with col2:
    st.subheader("📈 Trend Analysis")
    fig, ax = plt.subplots()
    ax.plot(df["date"], df["rainfall_mm"], label="Rainfall (mm)")
    ax.plot(df["date"], df["river_level_m"], label="River Level (m)")
    ax.legend()
    ax.set_xticklabels(df["date"], rotation=45)
    st.pyplot(fig)

# SMS Simulation
st.subheader("📱 Simulated SMS Alert")
alert_msg = f"""
ResilientAI Alert:
Risk Level: {risk}
Rainfall: {rainfall} mm
River Level: {river} m
Soil Moisture: {soil}%

Stay safe. Follow local guidelines.
"""
st.code(alert_msg, language="text")

st.markdown("---")
st.caption("Team ResilientAI — 3MTT Hackathon 2025")
🌊 ResilientAI — AI-Powered Early Flood Warning Prototype

3MTT “Resilience Through Innovation” Hackathon 2025
Team: ResilientAI

Predict • Prepare • Protect

🚀 Overview

ResilientAI is an AI-powered early warning system designed to help communities, emergency responders, and government agencies anticipate flood disasters before they happen.
This demo is a prototype built specifically for the 3MTT Hackathon to showcase how AI, data, and accessible communication channels can dramatically improve disaster preparedness across Nigeria.

Flooding is one of Nigeria’s deadliest and costliest climate-related hazards. Millions of people depend on early information to make life-saving decisions — yet current warning systems are fragmented, reactive, and often inaccessible to rural communities without internet access.

ResilientAI closes this gap.

🎯 Hackathon Prototype Features

This Streamlit prototype demonstrates the core functionality of the full ResilientAI platform:

✅ 1. Real-Time Flood Risk Simulation

Adjustable sliders to simulate rainfall, river-level, soil moisture, and temperature

Built-in simple AI model

Risk classification: LOW / MODERATE / HIGH

✅ 2. Automated Alert Simulation

Instant SMS-style alert preview

Shows how real warnings will be delivered via USSD/SMS

✅ 3. Multi-Page Dashboard

Home Page
Flood risk assessment + weather trend chart

Admin Analytics Page
Community monitoring metrics, alert distribution charts

Flood Hotspot Map Page
Prototype map showing at-risk areas

Alert Logs Page
Historical logs of sample alerts

✅ 4. Offline-Friendly and Local-Language Ready

Designed for SMS/USSD delivery in Hausa, Kanuri, and English.

🧠 How It Works (Prototype Architecture)
📡 Data Input (Simulated)
      ├── Rainfall
      ├── River level
      ├── Soil moisture
      └── Temperature

🧠 AI Risk Model (Simplified)
      └── Computes risk score → LOW / MODERATE / HIGH

📊 Dashboard (Streamlit)
      ├── Trend analysis
      ├── Risk indicators
      ├── Community analytics
      └── Alert logs

📱 Alert System Simulation
      └── SMS-style preview


This prototype uses simulated data only, ensuring consistent performance during live demo.

🗂️ Repository Structure
/
├── app.py                      # Main Streamlit dashboard
├── pages/
│   ├── 1_📊_Admin_Analytics.py
│   ├── 2_🗺️_Risk_Map.py
│   └── 3_📱_Alert_Logs.py
├── data/
│   └── sample_flood_data.csv   # Simulated environmental dataset
├── requirements.txt
├── README.md
└── .streamlit/
    └── config.toml             # App theme & UI settings

🛠️ Tech Stack

Python

Streamlit (Dashboard UI)

Pandas, NumPy

Matplotlib

scikit-learn (prepared for future ML integration)

▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py


public URL: https://resilientai-prototype-3nvhypbufffdqge2msnpke.streamlit.app

📌 Hackathon Team – ResilientAI

Abba Abdullahi Imam — AI Lead & presenter
Mahmud Alhassan - Data Collection & documentation
Adamu Ibrahim Farashi — Prototype Deployment

Contact:
📧 abbaimam3@gmail.com

🔗 https://github.com/abbaimam3

🌍 Vision

ResilientAI aims to become a continental early warning and climate resilience platform — a reliable system protecting millions across Nigeria and the Sahel through predictive analytics, real-time communication, and accessible technology.

⚠️ Note

This is a prototype made exclusively for the 3MTT Hackathon 2025.
The full platform will integrate:

Real-time weather APIs

River-level sensors

GIS flood zone mapping

SMS/USSD gateway

Scalable AI forecasting models

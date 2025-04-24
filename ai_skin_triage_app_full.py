
import streamlit as st
import pandas as pd

# Load the full mock database
df = pd.read_csv("AI_Skin_Triage_MockDatabase_FULL.csv")

st.set_page_config(page_title="AI Skin Triage Assistant", layout="centered")

st.title("🧠 AI Skin Triage Assistant")
st.write("Upload an image or pick one below to simulate AI-driven skin condition analysis.")

# Image selector (simulated)
img_name = st.selectbox("📸 Choose a simulated image:", df['Mock Image Name'].tolist())

if img_name:
    record = df[df['Mock Image Name'] == img_name].iloc[0]
    
    st.image("https://via.placeholder.com/300x200.png?text=" + img_name.split('.')[0], caption="Simulated Preview", use_column_width=True)

    st.subheader("🩺 Simulated Diagnosis")
    st.markdown(f"**Classified As:** {record['Simulated Class']}")
    st.markdown(f"**Severity Level:** `{record['Severity Level']}`")
    st.markdown(f"**Common Location:** {record['Common Location']}")
    st.markdown(f"**Painful:** {record['Painful?']}")
    st.markdown(f"**Infectious:** {record['Infectious?']}")
    st.markdown(f"**AI Confidence:** {record['AI Confidence Score (%)']}%")

    st.subheader("🧾 Suggested Action")
    st.info(record['Suggested Action'])

    st.caption("🔍 This is a mock prototype using simulated outputs for educational purposes.")

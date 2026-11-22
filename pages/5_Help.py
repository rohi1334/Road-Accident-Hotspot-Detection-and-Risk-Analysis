import streamlit as st
st.set_page_config(page_title="Help", layout="wide")
st.title("❓ Help - Road Accident Hotspot Detection & Risk Analysis System")
st.write("""
This page explains how to use the system and understand the results.
""")
st.divider()
# ---------------- HOTSPOT MAP ----------------
st.subheader("🗺 Hotspot Map")
st.write("""
• This page displays accident locations on an interactive map.
• Each marker represents a recorded accident location.
• Areas with many accidents indicate **accident hotspots**.
         
Purpose:
- Identify dangerous locations
- Understand accident density
- Improve travel awareness
""")
st.divider()
# ---------------- ROUTE RISK ANALYSIS ----------------
st.subheader("🚗 Route Risk Analysis")
st.write("""
Steps to use:

1. Enter **Source Location** (Example: Chennai).
2. Enter **Destination Location** (Example: Bangalore).
3. Click **Analyze Route Risk**.

The system will:
- Convert locations into coordinates
- Analyze accident records near the route
- Display risk level on the map
""")
st.write("""
Risk Levels:

🟢 **No Risk** → No accidents detected near route  
🟡 **Low Risk** → Few accidents detected  
🔴 **High Risk** → Many accidents detected
""")
st.divider()
# ---------------- DASHBOARD ----------------
st.subheader("📊 Dashboard")
st.write("""
The dashboard provides accident statistics and trends.
It shows:

• Total accident records  
• Accident severity distribution  
• Accidents by day of the week  
• Urban vs Rural accident percentage  
• Time-based accident trends

Purpose:
- Understand accident patterns
- Identify high-risk periods
""")
st.divider()
# ---------------- PROJECT PURPOSE ----------------
st.subheader("🎯 Project Purpose")
st.write("""
The goal of this system is to analyze historical road accident data and identify accident-prone areas.
Benefits:

• Helps travelers choose safer routes  
• Helps authorities identify dangerous zones  
• Improves road safety awareness
""")
st.divider()
st.success("Use the sidebar to navigate through different system features.")
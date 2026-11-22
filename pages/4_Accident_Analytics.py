import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Accident Dashboard", layout="wide")

st.title("📊 Road Accident Analytics Dashboard")

df = pd.read_csv("data/Accidents_AP_TS.csv", low_memory=False)

# Lowercase columns
df.columns = df.columns.str.lower()

st.metric("Total Accident Records", len(df))
st.divider()

# ------------------ MANUAL COLUMN MAPPING ------------------
# Change these if needed (based on your dataset)

severity_col = "accident_severity"   # try changing if not found
day_col = "day_of_week"
area_col = "urban_or_rural_area"
time_col = "time"

# ------------------ SEVERITY ------------------
st.subheader("Accident Severity Distribution")

if severity_col in df.columns:
    fig, ax = plt.subplots()
    df[severity_col].value_counts().plot(kind="bar", ax=ax)
    st.pyplot(fig)
else:
    st.error(f"{severity_col} not found")

st.divider()

# ------------------ DAY ------------------
st.subheader("Accidents by Day of Week")

if day_col in df.columns:
    fig, ax = plt.subplots()
    df[day_col].value_counts().plot(kind="bar", ax=ax)
    st.pyplot(fig)
else:
    st.error(f"{day_col} not found")

st.divider()

# ------------------ URBAN/RURAL ------------------
st.subheader("Urban vs Rural Accidents")

if area_col in df.columns:
    filtered = df[df[area_col].isin([1, 2])]
    counts = filtered[area_col].value_counts().sort_index()

    fig, ax = plt.subplots()
    ax.pie(counts, labels=["Urban", "Rural"], autopct="%1.1f%%")
    st.pyplot(fig)
else:
    st.error(f"{area_col} not found")

st.divider()

# ------------------ TIME ------------------
st.subheader("Accidents by Hour of Day")

if time_col in df.columns:
    df["hour"] = df[time_col].astype(str).str[:2]
    df["hour"] = pd.to_numeric(df["hour"], errors="coerce")

    fig, ax = plt.subplots()
    df["hour"].value_counts().sort_index().plot(kind="line", marker="o", ax=ax)
    st.pyplot(fig)
else:
    st.error(f"{time_col} not found")
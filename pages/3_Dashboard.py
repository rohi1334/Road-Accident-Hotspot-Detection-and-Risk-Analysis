import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Accident Dashboard", layout="wide")

st.title("📊 Road Accident Analytics Dashboard")

st.write("This dashboard shows accident statistics and trends based on historical data.")

# Load dataset
df = pd.read_csv("data/AccidentsBig.csv", low_memory=False)

# Convert column names to lowercase
df.columns = df.columns.str.lower()

# ---------- TOTAL ACCIDENTS ----------
st.subheader("Total Accidents")

total_accidents = len(df)

st.metric("Total Accident Records", total_accidents)

st.divider()

# ---------- SEVERITY DISTRIBUTION ----------
st.subheader("Accident Severity Distribution")

if "accident_severity" in df.columns:

    severity_counts = df["accident_severity"].value_counts()

    fig, ax = plt.subplots()

    severity_counts.plot(kind="bar", ax=ax)

    ax.set_xlabel("Severity Level")
    ax.set_ylabel("Number of Accidents")

    st.pyplot(fig)

st.divider()

# ---------- ACCIDENTS BY DAY ----------
st.subheader("Accidents by Day of Week")

if "day_of_week" in df.columns:

    day_counts = df["day_of_week"].value_counts().sort_index()

    fig, ax = plt.subplots()

    day_counts.plot(kind="bar", ax=ax)

    ax.set_xlabel("Day of Week")
    ax.set_ylabel("Number of Accidents")

    st.pyplot(fig)

st.divider()

# ---------- URBAN VS RURAL ----------
st.subheader("Urban vs Rural Accidents")

if "urban_or_rural_area" in df.columns:

    # Keep only Urban(1) and Rural(2)
    filtered = df[df["urban_or_rural_area"].isin([1, 2])]

    area_counts = filtered["urban_or_rural_area"].value_counts().sort_index()

    fig, ax = plt.subplots()

    ax.pie(
        area_counts,
        labels=["Urban", "Rural"],
        autopct="%1.1f%%",
        colors=["green", "red"],
        startangle=90
    )
    ax.set_ylabel("")
    st.pyplot(fig)
st.divider()
# ---------- TIME BASED ANALYSIS ----------
st.subheader("Accidents by Hour of Day")

if "time" in df.columns:

    # Extract hour directly from time string
    df["hour"] = df["time"].astype(str).str[:2]

    df["hour"] = pd.to_numeric(df["hour"], errors="coerce")

    hour_counts = df["hour"].value_counts().sort_index()
    fig, ax = plt.subplots()
    hour_counts.plot(kind="line", marker="o", ax=ax)
    ax.set_xlabel("Hour of Day")
    ax.set_ylabel("Number of Accidents")
    st.pyplot(fig)
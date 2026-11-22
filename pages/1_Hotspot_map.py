import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium


st.title("Accident Hotspot Map")


@st.cache_data
def load_data():

    df = pd.read_csv("data/raw/Accidents_AP_TS.csv")

    df = df.dropna()

    # demo severity
    df["severity"] = df.index % 3

    return df


df = load_data()


# -------------------------
# Sidebar filter
# -------------------------

st.sidebar.title("Filter Panel")

show_safe = st.sidebar.checkbox("Safe", True)
show_medium = st.sidebar.checkbox("Medium", True)
show_danger = st.sidebar.checkbox("Danger", True)


# -------------------------
# City select
# -------------------------

city_list = sorted(df["city"].unique())

city = st.selectbox("Select City", city_list)

df_city = df[df["city"] == city]


# severity filter

allowed = []

if show_safe:
    allowed.append(0)

if show_medium:
    allowed.append(1)

if show_danger:
    allowed.append(2)


df_city = df_city[df_city["severity"].isin(allowed)]


st.write("Rows:", len(df_city))


# -------------------------
# Map
# -------------------------

if len(df_city) > 0:

    center_lat = df_city["latitude"].mean()
    center_lon = df_city["longitude"].mean()

    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=11
    )

    for i in range(len(df_city)):

        lat = df_city.iloc[i]["latitude"]
        lon = df_city.iloc[i]["longitude"]
        sev = df_city.iloc[i]["severity"]

        if sev == 0:
            color = "green"
        elif sev == 1:
            color = "orange"
        else:
            color = "red"

        folium.Circle(
            location=[lat, lon],
            radius=200,
            color=color,
            fill=True,
        ).add_to(m)


    st_folium(m, width=700, height=500)
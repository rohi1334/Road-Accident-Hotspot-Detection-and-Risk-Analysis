import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
import openrouteservice


# API client
client = openrouteservice.Client(key="eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjFmMDAzMWQyNzk4ZjQ2ODY5ZGRjNTYxMDJmYmRmYjIxIiwiaCI6Im11cm11cjY0In0=")


st.title("Route Risk Analysis")

# Session state
if "route_data" not in st.session_state:
    st.session_state.route_data = None

# Inputs
start = st.text_input("Enter Start Location")
end = st.text_input("Enter End Location")

geolocator = Nominatim(user_agent="route_app")


def get_lat_lon(place):
    location = geolocator.geocode(place)
    if location:
        return location.latitude, location.longitude
    return None, None


# Button
if st.button("Analyze Route"):

    start_lat, start_lon = get_lat_lon(start)
    end_lat, end_lon = get_lat_lon(end)

    if start_lat and end_lat:

        st.session_state.route_data = (start_lat, start_lon, end_lat, end_lon)

    else:
        st.error("Invalid location")

# Show map
if st.session_state.route_data:

    start_lat, start_lon, end_lat, end_lon = st.session_state.route_data

    # create map
    m = folium.Map(location=[start_lat, start_lon], zoom_start=7)

    # markers
    folium.Marker([start_lat, start_lon], tooltip="Start").add_to(m)
    folium.Marker([end_lat, end_lon], tooltip="End").add_to(m)

    try:
        # get real route
        coords = [(start_lon, start_lat), (end_lon, end_lat)]

        route = client.directions(coords)

        geometry = route['routes'][0]['geometry']

        decoded = openrouteservice.convert.decode_polyline(geometry)

        route_coords = [(p[1], p[0]) for p in decoded['coordinates']]

        # draw road
        folium.PolyLine(
            route_coords,
            color="blue",
            weight=5
        ).add_to(m)

    except Exception as e:
        st.error("Error getting route")
        st.write(e)

    st_folium(m, width=700, height=500)
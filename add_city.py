import pandas as pd
from geopy.geocoders import Nominatim
import time

df = pd.read_csv("data/raw/Accidents_AP_TS.csv")

geolocator = Nominatim(user_agent="accident_project")

for i, row in df.iterrows():

    if pd.notna(row["city"]) and row["city"] != "":
        continue

    lat = row["latitude"]
    lon = row["longitude"]

    try:
        location = geolocator.reverse((lat, lon), timeout=10)

        if location and "address" in location.raw:

            address = location.raw["address"]

            city = (
                address.get("city")
                or address.get("town")
                or address.get("village")
                or address.get("state_district")
            )

        else:
            city = None

    except:
        city = None

    df.at[i, "city"] = city

    print(i, city)

    time.sleep(1)


df.to_csv("data/raw/Accidents_AP_TS.csv", index=False)

print("Updated file saved")
import pandas as pd
from sklearn.cluster import KMeans

def detect_hotspots(data):

    # Use only coordinates
    coords = data[["latitude", "longitude"]]

    # KMeans clustering
    kmeans = KMeans(n_clusters=10, random_state=42)

    data["cluster"] = kmeans.fit_predict(coords)

    return data, kmeans
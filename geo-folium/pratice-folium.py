import folium

import os

import pandas as pd


# Path: non-1b/geo-folium/pratice-folium.py

if __name__ == "__main__":
    map_file = os.path.join(os.path.dirname(__file__), 'map.html')
    map = folium.Map(location=[43.7, -79.4], zoom_start=12)

    folium.vector_layers.Circle(
        location=[43.7, -79.4],
        radius=25_000,

    )
    map.save(map_file)
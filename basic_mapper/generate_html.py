# -*- coding: utf-8 -*-
"""
@author: Matheus Boni Vicari
"""

import os
import folium
import pandas as pd
from folium.plugins import MarkerCluster

db = pd.read_csv("../data/fieldwork_database.csv")

m = folium.Map([0, 0], zoom_start=2)

marker_cluster = MarkerCluster().add_to(m)


for index, row in db.iterrows():
    df = pd.DataFrame(row)
    html = df.to_html()
    popup = folium.Popup(html)
    folium.Marker([row['SITE_LAT'], row['SITE_LONG']], popup=popup).add_to(marker_cluster)

m.save(os.path.join('../html', 'plot_sites.html'))

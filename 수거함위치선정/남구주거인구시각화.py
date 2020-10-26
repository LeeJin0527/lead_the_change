#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import folium





df = pd.read_csv('data/남구.csv')
df['dong'] = df['dong'].astype('str')






geo_data = open('data/namgu.json', 'r', encoding='utf-8').read()
geo_data





m = folium.Map(location=[35.8649155,128.5963041], zoom_start=10)





folium.Choropleth(
    geo_data=geo_data,
    data=df,
    columns=['dong','count'],
    key_on='feature.properties.adm_cd2',
    fill_color='BuPu',fill_opacity=0.7, line_opacity=0.5,
    legend_name='populations',
).add_to(m)





m








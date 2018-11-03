# Hayden Riewe
# CoordinateMapMaker
# v 0.1
# hrcyber.tech
# www.github.com/hriewe

import os
from urllib.request import pathname2url
import folium
import webbrowser

longitude = float(input("Enter the lognitude: "))
latitude = float(input("Enter the latitude: "))

map = folium.Map(location = [longitude, latitude], zoom_start = 7)
print(map.save('map.html'))

url = 'file:{}'.format(pathname2url(os.path.abspath('map.html')))
webbrowser.open(url)
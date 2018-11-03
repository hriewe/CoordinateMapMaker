# Hayden Riewe
# CoordinateMapMaker
# v 0.1
# hrcyber.tech
# www.github.com/hriewe

import os
from urllib.request import pathname2url
import folium
import webbrowser

# get coordinates from user
longitude = float(input("Enter the lognitude: "))
latitude = float(input("Enter the latitude: "))

# Generate the map
map = folium.Map(location = [longitude, latitude], zoom_start = 7)
folium.Marker(location = [longitude, latitude], popup = 'Your exact coordinates',
	icon = folium.Icon(color = 'red')).add_to(map)
map.save('map.html')

# Open the map in the users browser
url = 'file:{}'.format(pathname2url(os.path.abspath('map.html')))
webbrowser.open(url)
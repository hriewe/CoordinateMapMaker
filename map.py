import os
from urllib.request import pathname2url # Python 3.x
import folium
import webbrowser

map = folium.Map(location = [40.897934, -73.885948], zoom_start = 7)
print(map.save('map.html'))

url = 'file:{}'.format(pathname2url(os.path.abspath('map.html')))
webbrowser.open(url)
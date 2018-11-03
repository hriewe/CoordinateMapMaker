# Hayden Riewe
# CoordinateMapMaker
# v 0.1
# hrcyber.tech
# www.github.com/hriewe

import os
import sys
from urllib.request import pathname2url
import folium
import webbrowser
import PySimpleGUI as sg


sg.SetOptions(button_color=('white','#475841'), font=('Helvetica', 20))

layout = [[sg.Text('Welcome to Coordinate Map Maker', auto_size_text=False, justification='center')],
	[sg.Text('')],
	[sg.Text('Written by Hayden Riewe', auto_size_text=False, justification='center')],
	[sg.Text('')],
	[sg.Text('Enter the longitude', size=(20,1)), sg.InputText(size=(15,1))],
	[sg.Text('Enter the latitude', size=(20,1)), sg.InputText(size=(15,1))],
	[sg.Button('Go', auto_size_button=True), sg.Exit()]]

window = sg.Window('Welcome to CoordinateMapMaker!').Layout(layout)
button, value = window.Read()

if button == 'Go':
	# get coordinates from user
	longitude = float(value[0])
	latitude = float(value[1])

	# Generate the map
	map = folium.Map(location = [longitude, latitude], zoom_start = 7)
	folium.Marker(location = [longitude, latitude], popup = 'Your exact coordinates',
		icon = folium.Icon(color = 'red')).add_to(map)
	map.save('mymap.html')

	# Open the map in the users browser
	url = 'file:{}'.format(pathname2url(os.path.abspath('mymap.html')))
	webbrowser.open(url)
else:
	sys.exit()


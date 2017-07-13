import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

#data.columns
lat = list(data['LAT'])
lon = list(data['LON'])

map = folium.Map(location=[38,-100], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My map")

#for cordinates in [[38,-100],[37,-90]]:
    #fg.add_child(folium.Marker(location=cordinates, popup="Hi, I am a marker", icon=folium.Icon(color="green")))
    
for lt,ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=[lt,ln], popup="Hi, I am a marker", icon=folium.Icon(color="green")))

    
map.add_child(fg)

map.save("Map1.html")

#help(folium.Map)

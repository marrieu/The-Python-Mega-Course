import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

#data.columns
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_producer(elevation):
    if elevation < 1000:
        return("green")
    elif 1000 <= elevation <3000:
        return("orange")
    else:
        return("red")
    
map = folium.Map(location=[38,-100], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My map")

#for cordinates in [[38,-100],[37,-90]]:
    #fg.add_child(folium.Marker(location=cordinates, popup="Hi, I am a marker", icon=folium.Icon(color="green")))
    
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup="Elevation: "+str(el)+" m", icon=folium.Icon(color=color_producer(el))))

    
map.add_child(fg)

map.save("Map1.html")

#help(folium.Map)

import folium

map = folium.Map(location=[38,-100], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My map")
fg.add_child(folium.Marker(location=[38,-100], popup="Hi, I am a marker", icon=folium.Icon(color="greenq")))
map.add_child(fg)

map.save("Map1.html")

#help(folium.Map)

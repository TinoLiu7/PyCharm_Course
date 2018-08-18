import folium
import pandas as pd

sample_data = pd.read_csv('.//data//shilin-utf8.csv', sep=',')
print sample_data.shape
print sample_data.columns
# set column
sample_data.columns = ['section', 'road', 'road_detail', 'lon', 'lat', 'extra']
print sample_data.columns

taipei = [25.089995, 121.523401]
zoom = 15
map_osm = folium.Map(location=taipei, zoom_start=zoom)

for i in range(len(sample_data)):
    coord = [sample_data.iloc[i, 4], sample_data.iloc[i, 3]]
    message = "(%d)[%s]%s" % (i, sample_data.iloc[i, 1], sample_data.iloc[i, 2])
    message_utf8 = unicode(message, 'utf-8')
    icon1 = folium.Icon(color='blue', icon='info-sign')
    folium.Marker(coord, icon=icon1, popup=message_utf8).add_to(map_osm)

spot = [25.093619, 121.525654]
folium.Circle(spot, radius=500, popup='Shilin station',
              fill_color='#CCCC86').add_to(map_osm)
map_osm.save('.\\map\\result1.html')

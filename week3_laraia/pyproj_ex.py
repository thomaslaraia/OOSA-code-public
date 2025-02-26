#from pyproj import Proj, transform

#inProj = Proj("epsg:4326")
#outProj = Proj("epsg:27700")

#lat,lon = 67.26,26.53
#x,y = transform(inProj, outProj, lon, lat)

#print(lon,lat)
#print(x,y)

from pyproj import Transformer
transformer = Transformer.from_crs("EPSG:4326", "EPSG:27700")
lon, lat = 26.53, 67.26
x,y = transformer.transform(lon,lat)
print(lon,lat)
print(x,y)

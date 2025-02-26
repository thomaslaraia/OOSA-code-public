from osgeo import gdal
#import os

inName = "/geos/netdata/oosa/week3/raster/discRefl.LT.refl.tif"
outName = "warped.tif"
#print(1)
#print(os.path.exists(inName))

ds = gdal.Open(inName)
print(ds)

#gdal.Warp(outName,inName,dstSRS='EPSG:4326')

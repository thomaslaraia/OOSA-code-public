
'''
Example of producing an
NDVI image with rasterio
'''

# import packages needed
import rasterio
from glob import glob
import numpy as np


#################################

if __name__ == "__main__":
  '''Main block'''

  #dir='/geos/netdata/oosa/week3/sentinel-2/L2A_T30VVH_A020126_20210112T113447_2021-01-12'
  dir='/Users/dougal/data/teaching/key_meth/week2/sentinel-2/L2A_T30VVH_A020126_20210112T113447_2021-01-12'
  fileList=glob(dir+"/*"+".jp2")

  # NDVI at 10 m res is Band 4 and band 8. Search for those band
  band4name=list(filter(lambda x: x.endswith("B04.jp2"), fileList))[0]
  band8name=list(filter(lambda x: x.endswith("B08.jp2"), fileList))[0]

  # open the two datasets
  band4file=rasterio.open(band4name)
  band8file=rasterio.open(band8name)

  # read the rasters and scale to be in relfectance
  band4=band4file.read(1)/10000
  band8=band8file.read(1)/10000

  # remove missing data
  band4[band4>1.0]=-999.0
  band8[band8>1.0]=-999.0

  # calculate ndvi
  ndvi=(band8-band4)/(band8+band4)
  # filter out missing data
  ndvi[ndvi>1]=-999.0
  ndvi[ndvi<-1]=-999.0

  # open a new dataset ready to write, with the same dimensions as the above data
  outName='sentinel2.ndvi.tif'
  new_dataset=rasterio.open(outName,'w',driver='GTiff',height=band4file.height,
                 width=band4file.width,count=1,dtype=ndvi.dtype,crs=band4file.crs,transform=band4file.transform)
  new_dataset.write(ndvi, 1)
  new_dataset.nodata = -999.0
  new_dataset.close()
  print("NDVI written to",outName)


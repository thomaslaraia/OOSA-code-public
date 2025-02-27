import rasterio
from matplotlib import pyplot as plt
import numpy as np
import argparse
from rasterio.warp import calculate_default_transform, reproject, Resampling

parser = argparse.ArgumentParser(description='Allowing the EPSG to change')
parser.add_argument('--epsg', type=int, default=-1, help='Change to EPSG:#### of choice')
args = parser.parse_args()

bands = ['04','08']
filenames = ['/geos/netdata/oosa/week3/sentinel-2/L2A_T30VVH_A020126_20210112T113447_2021-01-12/T30VVH_A020126_20210112T113447_B'+b+'.jp2' for b in bands]

data = []
for i, f in enumerate(filenames):

  dataset=rasterio.open(f)
  bandLayer = dataset.read(1)/10000
  bandLayer[bandLayer>1.0]=np.nan
  data.append(bandLayer)

ndvi = np.divide(data[1]-data[0], data[1]+data[0], where=data[1]+data[0]!=0)
ndvi_scaled = (ndvi*10000).astype(np.int16)

outName = '../../sentinel2.ndvi.tif'

if args.epsg != -1 and dataset.crs.to_epsg() != args.epsg:
    target_crs = f'EPSG:{args.epsg}'

    transform, width, height = calculate_default_transform(
        dataset.crs, target_crs, dataset.width, dataset.height,
        *dataset.bounds)
        
    new_metadata = dataset.meta.copy()
    new_metadata.update({
        'crs': target_crs,
        'transform': transform,
        'width': width,
        'height': height,
        'dtype': np.int16})

    #print(new_metadata['height'],dataset.height)
    with rasterio.open(outName, 'w',**new_metadata) as new_dataset:
        reproject(source=ndvi_scaled,
            destination=rasterio.band(new_dataset,1),
            src_transform=dataset.transform,
            src_crs=dataset.crs,
            dst_transform=transform,
            dst_crs=target_crs,
            resampling=Resampling.nearest)

else:
    new_dataset = rasterio.open(outName,'w',driver='Gtiff',height=dataset.height,
        width=dataset.width,count=1,dtype=ndvi.dtype,crs=dataset.crs,
        transform=dataset.transform)

    new_dataset.write(ndvi,1)

    new_dataset.close()


#plt.savefig('three_bands.png')

import rasterio
from matplotlib import pyplot as plt

bands = ['02','03','04']
filenames = ['/geos/netdata/oosa/week3/sentinel-2/L2A_T30VVH_A020126_20210112T113447_2021-01-12/T30VVH_A020126_20210112T113447_B'+b+'.jp2' for b in bands]

fig, ax = plt.subplots(1,3)
ax.flatten()


for i, f in enumerate(filenames):

  dataset=rasterio.open(f)
#print(dataset.width)

  bandLayer = dataset.read(1)
  ax[i].imshow(bandLayer)

plt.savefig('three_bands.png')

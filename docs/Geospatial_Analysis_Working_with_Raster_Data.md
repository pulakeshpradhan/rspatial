# Reading Raster Data with GDAL


```python
from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
```


```python
file_name=r'data/L3-NE43H11-095-060-30nov09-BAND2.tif'
```


```python
dataset=gdal.Open(file_name)
```


```python
print(dataset)
```


```python
if not dataset:
    print('Error in Reading File',file_name)
else:
    print('File reading success')
```

### Getting dataset information


```python
print('Driver:',dataset.GetDriver().ShortName)
```


```python
print('Size is ',dataset.RasterXSize,' x', dataset.RasterYSize)
```


```python
print('Bands in image ',dataset.RasterCount)
```


```python
print('Projection is', dataset.GetProjection())
```


```python
geotransform=dataset.GetGeoTransform()
```


```python
geotransform
```


```python
if geotransform:
    print('Origin=',geotransform[0],geotransform[3])
    print('Pixel Size=',geotransform[1], geotransform[5])
    print('Rotation=',geotransform[2],geotransform[4])
```

### Fetching a Raster Band


```python
band = dataset.GetRasterBand(1) #1-indexed number
```


```python
print(band)
```


```python
print('Band Type=',gdal.GetDataTypeName(band.DataType))
```


```python
minimum,maximum = band.ComputeRasterMinMax(True)
```


```python
print(minimum,maximum)
```

### Reading Raster Data


```python
data = band.ReadAsArray()
```


```python
data
```


```python
data.shape
```


```python
plt.figure(figsize=(8,8))
plt.imshow(data,cmap='gist_gray')
```

### Closing the Dataset


```python
dataset=None
del dataset
```

### Reading Multi band Raster Data with GDAL


```python
file_name=r'data/fcc.tif'
```


```python
dataset=gdal.Open(file_name,gdal.GA_ReadOnly)
```


```python
if not dataset:
    print('Error in Reading File',file_name)
```


```python
print('Driver:',dataset.GetDriver().ShortName)
```


```python
bands=dataset.RasterCount
print('Bands in image ',dataset.RasterCount)
```


```python
plt.figure(figsize=(30,30))
for i in range(1,bands+1):
    band=dataset.GetRasterBand(i)
    data=band.ReadAsArray()
    ax = plt.subplot(1,3,i)
    ax.set_title('Band {}'.format(i))
    plt.imshow(data,cmap='Greys')
plt.show()
```


```python
plt.figure(figsize=(7,7))
data=dataset.ReadAsArray() #reads whole file into a np array
print(data.shape)
data=np.dstack((data[0],data[1],data[2]))
print(data.shape)
i = plt.imshow(data*2)
```


```python
dataset=None
del dataset
```

# Writing  Raster Data with GDAL


```python
fileformat = 'HFA'
```


```python
driver = gdal.GetDriverByName(fileformat)
```

### Using CreateCopy()
### Information is copied from the source dataset


```python
src_filename=r'data/L3-NE43H11-095-060-30nov09-BAND2.tif'
dst_filename=r'data/BAND2.img'
src_ds = gdal.Open(src_filename)
```


```python
src_ds
```


```python
dst_ds = driver.CreateCopy(dst_filename, src_ds)
```


```python
band=src_ds.GetRasterBand(1)
```


```python
data=band.ReadAsArray()
```


```python
data=data+10
```


```python
out_band=dst_ds.GetRasterBand(1)
```


```python
out_band.WriteArray(data)
```


```python
dst_ds.FlushCache()
dst_ds=None
src_ds=None
```

### Using Create()


```python
from osgeo import osr
```


```python
fileformat = 'HFA'
```


```python
driver=gdal.GetDriverByName(fileformat)
```


```python
src_ds=gdal.Open(src_filename,gdal.GA_ReadOnly)
```


```python
dst_filename=r'data/new_file.img'
```


```python
dst_ds = driver.Create(dst_filename, xsize=512, ysize=512,
                       bands=1, eType=gdal.GDT_Byte)
```


```python
geo_trf=[444720, 30, 0, 3751320, 0, -30]
```


```python
srs=osr.SpatialReference()
srs.SetUTM(11,1)
srs.SetWellKnownGeogCS('WGS84')
```


```python
dst_ds.SetGeoTransform(geo_trf)
dst_ds.SetProjection(srs.ExportToWkt())
```


```python
srs.ExportToWkt()
```


```python
data=np.random.randint(low=0,high=255,size=(512,512))
```


```python
plt.imshow(data,cmap='Greys')
```


```python
out_band=dst_ds.GetRasterBand(1)
out_band.WriteArray(data)
```


```python
dst_ds.FlushCache()
dst_ds=None
del dst_ds
```

# Stacking Individual Raster Bands


```python
input_files=['data/L3-NE43H11-095-060-30nov09-BAND4.tif','data/L3-NE43H11-095-060-30nov09-BAND3.tif',
            'data/L3-NE43H11-095-060-30nov09-BAND2.tif']
```


```python
dst_filename=r'data/LISS_3_fcc.tif'
```


```python
driver=gdal.GetDriverByName('GTiff')
```


```python
dst_ds=driver.Create(dst_filename,xsize=1153,ysize=1153,bands=3,eType=gdal.GDT_UInt16)
```


```python
index=1
for file_name in input_files:
    src_ds=gdal.Open(file_name,gdal.GA_ReadOnly)
    src_data=src_ds.GetRasterBand(1).ReadAsArray()
    dst_band=dst_ds.GetRasterBand(index)
    dst_band.WriteArray(src_data)
    index+=1
```


```python
dst_ds.FlushCache()
dst_ds.BuildOverviews('average')
dst_ds.BuildOverviews
dst_ds=None
```

### Creating Color Table


```python
file_name=r'data/lulc.tif'
dst_file=r'data/lulc_map.tif'
```


```python
src_ds=gdal.Open(file_name,gdal.GA_ReadOnly)
```


```python
driver=gdal.GetDriverByName('GTiff')
dst_ds=driver.CreateCopy(dst_file,src_ds)
```


```python
band=dst_ds.GetRasterBand(1)
```


```python
colors=gdal.ColorTable()
```


```python
colors.SetColorEntry(1, (5, 69, 10))
colors.SetColorEntry(2, (8, 106, 16))
colors.SetColorEntry(3, (84, 167, 8))
colors.SetColorEntry(4, (120, 210, 3))
colors.SetColorEntry(5, (0, 153, 0))
colors.SetColorEntry(6, (198, 176, 68))
colors.SetColorEntry(7, (220, 209, 89))
colors.SetColorEntry(8, (218, 222, 72))
colors.SetColorEntry(9, (251, 255, 19))
colors.SetColorEntry(10, (182, 255, 5))
colors.SetColorEntry(11, (39, 255, 135))
colors.SetColorEntry(12, (194, 79, 68))
colors.SetColorEntry(13, (165, 165, 165))
colors.SetColorEntry(14, (255, 109, 76))
colors.SetColorEntry(15, (105, 255, 248))
colors.SetColorEntry(16, (249, 255, 164))
colors.SetColorEntry(17, (28, 13, 255))
```


```python
band.SetColorTable(colors)
band.SetColorInterpretation(gdal.GCI_PaletteIndex)
```


```python
dst_ds.FlushCache()
del band
del dst_ds
```

## Mosaicing images


```python
import glob
```


```python
file_names = glob.glob('data/mosaic/*.tif')
print('Number of files found in the mosaic folder: ', (list(file_names)))
```


```python
plt.figure(figsize=(7,7))
datasets=list()
for index, eachfile in enumerate(file_names):
    data_set=gdal.Open(str(eachfile))
    datasets.append(data_set)
    # next statements are required for plotting only
    data=data_set.ReadAsArray()
    plt.subplot(2,2,index+1)
    plt.imshow(data,cmap='Greys')
    data_set=None

plt.show()
```


```python
datasets
```


```python
mosiac=gdal.Warp("data/mosaic.tif", datasets, format='GTiff')
```


```python
plt.figure(figsize=(8, 8))
plt.imshow(mosiac.ReadAsArray(),cmap='Greys')
```

## Water body mapping

The LISS 3 data has the following bands


| Sensor                | LISS-3              |
|-----------------------|---------------------|
| Number of   Bands     | 4                   |
| Spectral   Band 2 (µ) | 0.52 – 0.59 (green) |
| Spectral   Band 3 (µ) | 0.62 – 0.68 (red)   |
| Spectral   Band 4 (µ) | 0.77 – 0.86 (NIR)   |
| Spectral   Band 5 (µ) | 1.55 – 1.70 (SWIR)  |

Water bodies are generally identified by using an index called the Normalized Difference Water Index. There are 2 well known formula for NDWI.


$NDWI = (G-NIR)/(G+NIR)$

and

$NDWI = (NIR-SWIR)/(NIR+SWIR)$

where $G$, $NIR$ and $SWIR$ stand for the green (band 2), NIR (band 4) and SWIR (band 5) bands.


```python
# let us apply the first formula and see the output
green_file_name = r'data/L3-NE43H11-095-060-30nov09-BAND2.tif'
nir_file_name = r'data/L3-NE43H11-095-060-30nov09-BAND4.tif'

green = gdal.Open(green_file_name).ReadAsArray()
nir = gdal.Open(nir_file_name).ReadAsArray()

ndwi = (green - nir) / (green + nir)
print('Min NDWI = {}, Max NDWI = {}'.format(ndwi.min(), ndwi.max()))
plt.imshow(ndwi,cmap='Greys')
```


```python
from scipy.ndimage import gaussian_filter
```


```python
filtered_ndwi = gaussian_filter(ndwi, sigma=2)
print('Min NDWI = {}, Max NDWI = {}'.format(filtered_ndwi.min(), filtered_ndwi.max()))
plt.imshow(filtered_ndwi,cmap='Greys')
```


```python
histogram, bin_edges = np.histogram(filtered_ndwi, bins=128, range=(0.0, 1.0))
fig, ax = plt.subplots()
plt.plot(bin_edges[0:-1], histogram)
plt.title("Graylevel histogram")
plt.xlabel("gray value")
plt.ylabel("pixel count")
plt.xlim(0, 1)
```


```python
# create a binary mask with the manual threshold
binary_mask = filtered_ndwi < 0.58

fig, ax = plt.subplots()
plt.imshow(binary_mask, cmap="gray")
```


```python
file_name=r'data/fcc.tif'
data=gdal.Open(file_name).ReadAsArray()
data=np.dstack((data[0],data[1],data[2]))
water = np.ma.masked_where(binary_mask == 0, binary_mask)

plt.figure(figsize=(30,30))
ax = plt.subplot(1,3,1)
ax.set_title('FCC')
plt.imshow(data*2)

ax = plt.subplot(1,3,2)
ax.set_title('Water mask')
plt.imshow(water, cmap="winter")

ax = plt.subplot(1,3,3)
ax.set_title('Water mask overlaid with FCC')
plt.imshow(data*2)
plt.imshow(water, cmap="winter")
```

## Exercise

Can you attempt the steps above for the second NDWI formula? What is the threshold in this case? Does it give a better approximation of the water body?


```python

```

## Challenge problem

Install the [scikit-image](https://scikit-image.org/docs/stable/install.html) library and find the threshold based on [OTSU's method](https://scipy-lectures.org/packages/scikit-image/auto_examples/plot_threshold.html). Apply the threshold as shown above to generate water body map. Does it give a better approximation of the water body? Using which NDWI formula?

Notebook created by Prasun Kumar Gupta, Geoinformatics Department, Indian Institute of Remote Sensing (ISRO), Dehradun. Contact: prasun@iirs.gov.in


<iframe width="560" height="315" src="https://www.youtube.com/embed/3JHdxtNQbv8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

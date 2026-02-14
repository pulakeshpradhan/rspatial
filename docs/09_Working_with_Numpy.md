## Numpy Module


```python
import numpy as np
```


```python
list1=[1,2,3,4]
list2=[5,6,7,8]
```


```python
#creation of numpy array by passing a list to np.array() method
a = np.array(list1)
```


```python
a
```




    array([1, 2, 3, 4])




```python
#shape attribute of 1D numpy array displays a tuple with no of elements
a.shape
```




    (4,)




```python
#ndim attribute gives the dimension of numpy array
a.ndim
```




    1




```python
#dtype attribute gives the data type of elements of numpy array
a.dtype
```




    dtype('int32')




```python
#creation of 2D numpy array by passing a list of lists
b=np.array([list1,list2])
```


```python
b
```




    array([[1, 2, 3, 4],
           [5, 6, 7, 8]])




```python
#shape attribute of 2D numpy array gives a tuple with no. of rows and columns
b.shape
```




    (2, 4)




```python
#ndim attribute gives the dimension of numpy array
b.ndim
```




    2




```python
#dtype attribute gives the data type of elements of numpy array
b.dtype
```




    dtype('int32')




```python
list3=[9.0,10.0,11.0,12.0]
```


```python
#creation of 2D numpy array by passing a list of lists
c=np.array([list1,list2,list3])
```


```python
c
```




    array([[ 1.,  2.,  3.,  4.],
           [ 5.,  6.,  7.,  8.],
           [ 9., 10., 11., 12.]])




```python
#dtype attribute gives the data type of elements of numpy array
c.dtype
```




    dtype('float64')




```python
#ndim attribute gives the dimension of numpy array
c.ndim
```




    2




```python
#shape attribute of 2D numpy array gives a tuple with no. of rows and columns
c.shape
```




    (3, 4)




```python
help(np.arange)
```

    Help on built-in function arange in module numpy:
    
    arange(...)
        arange([start,] stop[, step,], dtype=None, *, like=None)
        
        Return evenly spaced values within a given interval.
        
        Values are generated within the half-open interval ``[start, stop)``
        (in other words, the interval including `start` but excluding `stop`).
        For integer arguments the function is equivalent to the Python built-in
        `range` function, but returns an ndarray rather than a list.
        
        When using a non-integer step, such as 0.1, the results will often not
        be consistent.  It is better to use `numpy.linspace` for these cases.
        
        Parameters
        ----------
        start : integer or real, optional
            Start of interval.  The interval includes this value.  The default
            start value is 0.
        stop : integer or real
            End of interval.  The interval does not include this value, except
            in some cases where `step` is not an integer and floating point
            round-off affects the length of `out`.
        step : integer or real, optional
            Spacing between values.  For any output `out`, this is the distance
            between two adjacent values, ``out[i+1] - out[i]``.  The default
            step size is 1.  If `step` is specified as a position argument,
            `start` must also be given.
        dtype : dtype
            The type of the output array.  If `dtype` is not given, infer the data
            type from the other input arguments.
        like : array_like
            Reference object to allow the creation of arrays which are not
            NumPy arrays. If an array-like passed in as ``like`` supports
            the ``__array_function__`` protocol, the result will be defined
            by it. In this case, it ensures the creation of an array object
            compatible with that passed in via this argument.
        
            .. versionadded:: 1.20.0
        
        Returns
        -------
        arange : ndarray
            Array of evenly spaced values.
        
            For floating point arguments, the length of the result is
            ``ceil((stop - start)/step)``.  Because of floating point overflow,
            this rule may result in the last element of `out` being greater
            than `stop`.
        
        See Also
        --------
        numpy.linspace : Evenly spaced numbers with careful handling of endpoints.
        numpy.ogrid: Arrays of evenly spaced numbers in N-dimensions.
        numpy.mgrid: Grid-shaped arrays of evenly spaced numbers in N-dimensions.
        
        Examples
        --------
        >>> np.arange(3)
        array([0, 1, 2])
        >>> np.arange(3.0)
        array([ 0.,  1.,  2.])
        >>> np.arange(3,7)
        array([3, 4, 5, 6])
        >>> np.arange(3,7,2)
        array([3, 5])
    
    


```python
#creation of numpy array using arange() method
d = np.arange(12)
d
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])




```python
#dtype attribute gives the data type of elements of numpy array
d.dtype
```




    dtype('int32')




```python
#change of data type of numpy array using astype() method
d.astype(np.float32)
```




    array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11.],
          dtype=float32)




```python
#data type of numpy array can be specified at the time of its creation
e = np.array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11.],
      dtype='float64')
e
```




    array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11.])




```python
#dtype attribute gives the data type of elements of numpy array
e.dtype
```




    dtype('float64')




```python
#creation of 3D numpy array using arange() and reshape() methods
f = np.arange(24).reshape(2,3,4)
```


```python
f
```




    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],
    
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])




```python
#shape attribute of 3D numpy array 
f.shape
```




    (2, 3, 4)




```python
#ndim attribute gives the dimension of numpy array
f.ndim
```




    3




```python
#creation of a 2D numpy array of zeros
np.zeros((2,2))
```




    array([[0., 0.],
           [0., 0.]])




```python
#creation of a 2D numpy array of ones
np.ones((2,3))
```




    array([[1., 1., 1.],
           [1., 1., 1.]])




```python
# empty() method can be used to create a numpy array with garbage values for further assignment
np.empty((2,4))
```




    array([[0.00000000e+000, 0.00000000e+000, 0.00000000e+000,
            0.00000000e+000],
           [0.00000000e+000, 9.66392403e-321, 1.33511018e-306,
            1.33511969e-306]])




```python
a
```




    array([1, 2, 3, 4])




```python
#elements of 1D numpy array can be accessed using their index as in the case of python built-in lists
a[0]
```




    1




```python
#slicing of 1D numpy array is similar to slicing of python built-in lists
a[0:3]
```




    array([1, 2, 3])




```python
b
```




    array([[1, 2, 3, 4],
           [5, 6, 7, 8]])




```python
#rows of 2D numpy array can be accessed with their indexes 
b[0]
```




    array([1, 2, 3, 4])




```python
#slicing of 2D numpy array
b[:,2]
```




    array([3, 7])




```python
# slicing of 2D numpy array results in another 2D numpy array if both start and end indexes are specified
b[1:,1:3]
```




    array([[6, 7]])




```python
b[1:,1:3].ndim
```




    2




```python
a
```




    array([1, 2, 3, 4])




```python
#subsetting of discontiguos data of a numpy array in the  order of indexes passed
a[[3,0]]
```




    array([4, 1])




```python
b
```




    array([[1, 2, 3, 4],
           [5, 6, 7, 8]])




```python
#extraction of values from a 2D numpy array by providing a list of lists containing row and column offsets
b[[0,0,1],[0,2,3]]
```




    array([1, 3, 8])




```python
g = b[:,1:3]
g
```




    array([[2, 3],
           [6, 7]])




```python
#changes made in a subset of numpy array are also reflected in the original numpy array
#original values can be preserved by making a  copy of the original using copy() method
g[0][0]=9
g
```




    array([[9, 3],
           [6, 7]])




```python
b
```




    array([[1, 9, 3, 4],
           [5, 6, 7, 8]])




```python
x=np.array([[1,2],[3,4]])
x
```




    array([[1, 2],
           [3, 4]])




```python
y = np.array(([-1,3],[4,3]))
y
```




    array([[-1,  3],
           [ 4,  3]])




```python
#element by element addition of two 2D numpy arrays
x+y
```




    array([[0, 5],
           [7, 7]])




```python
#element by element subtraction of two 2D numpy arrays
x-y
```




    array([[ 2, -1],
           [-1,  1]])




```python
#element by element multiplication of two 2D numpy arrays
x*y
```




    array([[-1,  6],
           [12, 12]])




```python
#element by element comparison of two 2D numpy arrays with logical operators
h = x>y
h
```




    array([[ True, False],
           [False,  True]])




```python
h.dtype
```




    dtype('bool')




```python
#where() method can be used to implement if else statements in numpy arrays using conditional check
np.where(x>y,10,20)
```




    array([[10, 20],
           [20, 10]])




```python
i = np.zeros((2,2))
i
```




    array([[0., 0.],
           [0., 0.]])




```python
j= np.ones((2,2))
j
```




    array([[1., 1.],
           [1., 1.]])




```python
np.where(x>y,i,j)
```




    array([[0., 1.],
           [1., 0.]])




```python
a
```




    array([1, 2, 3, 4])




```python
a[0]=0
a
```




    array([0, 2, 3, 4])




```python
# division by zero results either in nan or inf
a/0
```

    C:\Users\COMP109\AppData\Local\Temp/ipykernel_13080/2320887286.py:2: RuntimeWarning: divide by zero encountered in true_divide
      a/0
    C:\Users\COMP109\AppData\Local\Temp/ipykernel_13080/2320887286.py:2: RuntimeWarning: invalid value encountered in true_divide
      a/0
    




    array([nan, inf, inf, inf])




```python
a
```




    array([0, 2, 3, 4])




```python
a[3]=100
a
```




    array([  0,   2,   3, 100])




```python
#Application of conditional check and selection of elements based on the condition
a[a<10]
```




    array([0, 2, 3])




```python
a
```




    array([  0,   2,   3, 100])




```python
#sum() method returns the sum of all elements of a numpy array
a.sum()
```




    105




```python
#max() method returns the maximum of all elements
a.max()
```




    100




```python
#min() method returns the minimum of all elements
a.min()
```




    0




```python
b
```




    array([[1, 9, 3, 4],
           [5, 6, 7, 8]])




```python
#summation of elements along columns of 2D numpy array
b.sum(axis=0)
```




    array([ 6, 15, 10, 12])




```python
#summation of elements along rows of 2D numpy array
b.sum(axis=1)
```




    array([17, 26])




```python
#maximum element along columns of 2D numpy array
b.max(axis=0)
```




    array([5, 9, 7, 8])




```python
c
```




    array([[ 1.,  2.,  3.,  4.],
           [ 5.,  6.,  7.,  8.],
           [ 9., 10., 11., 12.]])




```python
#creation of 3D numpy array by specifying the elements
c=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
```


```python
c

```




    array([[[ 1,  2,  3,  4],
            [ 5,  6,  7,  8]],
    
           [[ 9, 10, 11, 12],
            [13, 14, 15, 16]]])




```python
#ndim attribute gives the dimension of numpy array
c.ndim
```




    3




```python
#shape attribute of 3D numpy array gives no of layers, rows and columns 
c.shape
```




    (2, 2, 4)




```python
# maximum element in Row and columns in both layers
c.max(axis=0)
```




    array([[ 9, 10, 11, 12],
           [13, 14, 15, 16]])




```python
#maximum elements in layers
c.max(axis=(1,2))
```




    array([ 8, 16])




```python
#maximum elements in rows across layers
c.max(axis=(0,2))
```




    array([12, 16])




```python
#maximum elements in columns across layers
c.max(axis=(0,1))
```




    array([13, 14, 15, 16])




```python
a
```




    array([  0,   2,   3, 100])




```python
a.dtype
```




    dtype('int32')




```python
a=a.astype('float32')
```


```python
a
```




    array([  0.,   2.,   3., 100.], dtype=float32)




```python
#np.nan can be assigned only in case of float arrays
# np.nan can be used for missing values or outliers
a[3]=np.nan
```


```python
a
```




    array([ 0.,  2.,  3., nan], dtype=float32)




```python
#any arithmetic operation involving nan returns nan
a.sum()
```




    nan




```python
#use of nansum() method to ignore nan elements
np.nansum(a)
```




    5.0




```python
#use of isnan() method to check no-data elements
np.isnan(a)
```




    array([False, False, False,  True])



## Working with Raster Data using Rasterio


```python
import rasterio
import pathlib
import os
import glob
```


```python
#define file path to SRTM dem file for Pune region
fp_dem= pathlib.Path.home()/'PythonWRM'/'Data'/'SRTM_Pune_Region.tif'
```


```python
fp_dem
```




    WindowsPath('C:/Users/COMP109/PythonWRM/Data/SRTM_Pune_Region.tif')




```python
help(rasterio.open)
```

    Help on function open in module rasterio:
    
    open(fp, mode='r', driver=None, width=None, height=None, count=None, crs=None, transform=None, dtype=None, nodata=None, sharing=False, **kwargs)
        Open a dataset for reading or writing.
        
        The dataset may be located in a local file, in a resource located by
        a URL, or contained within a stream of bytes.
        
        In read ('r') or read/write ('r+') mode, no keyword arguments are
        required: these attributes are supplied by the opened dataset.
        
        In write ('w' or 'w+') mode, the driver, width, height, count, and dtype
        keywords are strictly required.
        
        Parameters
        ----------
        fp : str, file object or pathlib.Path object
            A filename or URL, a file object opened in binary ('rb') mode,
            or a Path object.
        mode : str, optional
            'r' (read, the default), 'r+' (read/write), 'w' (write), or
            'w+' (write/read).
        driver : str, optional
            A short format driver name (e.g. "GTiff" or "JPEG") or a list of
            such names (see GDAL docs at
            http://www.gdal.org/formats_list.html). In 'w' or 'w+' modes
            a single name is required. In 'r' or 'r+' modes the driver can
            usually be omitted. Registered drivers will be tried
            sequentially until a match is found. When multiple drivers are
            available for a format such as JPEG2000, one of them can be
            selected by using this keyword argument.
        width : int, optional
            The number of columns of the raster dataset. Required in 'w' or
            'w+' modes, it is ignored in 'r' or 'r+' modes.
        height : int, optional
            The number of rows of the raster dataset. Required in 'w' or
            'w+' modes, it is ignored in 'r' or 'r+' modes.
        count : int, optional
            The count of dataset bands. Required in 'w' or 'w+' modes, it is
            ignored in 'r' or 'r+' modes.
        crs : str, dict, or CRS; optional
            The coordinate reference system. Required in 'w' or 'w+' modes,
            it is ignored in 'r' or 'r+' modes.
        transform : Affine instance, optional
            Affine transformation mapping the pixel space to geographic
            space. Required in 'w' or 'w+' modes, it is ignored in 'r' or
            'r+' modes.
        dtype : str or numpy dtype
            The data type for bands. For example: 'uint8' or
            ``rasterio.uint16``. Required in 'w' or 'w+' modes, it is
            ignored in 'r' or 'r+' modes.
        nodata : int, float, or nan; optional
            Defines the pixel value to be interpreted as not valid data.
            Required in 'w' or 'w+' modes, it is ignored in 'r' or 'r+'
            modes.
        sharing : bool; optional
            To reduce overhead and prevent programs from running out of file
            descriptors, rasterio maintains a pool of shared low level
            dataset handles. When `True` this function will use a shared
            handle if one is available. Multithreaded programs must avoid
            sharing and should set *sharing* to `False`.
        kwargs : optional
            These are passed to format drivers as directives for creating or
            interpreting datasets. For example: in 'w' or 'w+' modes
            a `tiled=True` keyword argument will direct the GeoTIFF format
            driver to create a tiled, rather than striped, TIFF.
        
        Returns
        -------
        A ``DatasetReader`` or ``DatasetWriter`` object.
        
        Examples
        --------
        
        To open a GeoTIFF for reading using standard driver discovery and
        no directives:
        
        >>> import rasterio
        >>> with rasterio.open('example.tif') as dataset:
        ...     print(dataset.profile)
        
        To open a JPEG2000 using only the JP2OpenJPEG driver:
        
        >>> with rasterio.open(
        ...         'example.jp2', driver='JP2OpenJPEG') as dataset:
        ...     print(dataset.profile)
        
        To create a new 8-band, 16-bit unsigned, tiled, and LZW-compressed
        GeoTIFF with a global extent and 0.5 degree resolution:
        
        >>> from rasterio.transform import from_origin
        >>> with rasterio.open(
        ...         'example.tif', 'w', driver='GTiff', dtype='uint16',
        ...         width=720, height=360, count=8, crs='EPSG:4326',
        ...         transform=from_origin(-180.0, 90.0, 0.5, 0.5),
        ...         nodata=0, tiled=True, compress='lzw') as dataset:
        ...     dataset.write(...)
    
    


```python
#opening a raster data file with rasterio.open() method 
dem = rasterio.open(fp_dem)
```


```python
#open() method creates a DatasetReader object
type(dem)
```




    rasterio.io.DatasetReader




```python
#meta attribute of opened raster file gives its metadata
dem.meta
```




    {'driver': 'GTiff',
     'dtype': 'int16',
     'nodata': None,
     'width': 6711,
     'height': 5626,
     'count': 1,
     'crs': CRS.from_epsg(4326),
     'transform': Affine(0.0002694945852358564, 0.0, 73.34040191875982,
            0.0, -0.0002694945852358564, 19.410481428175615)}




```python
#driver attribute gives information about the format of the raster file
dem.driver
```




    'GTiff'




```python
#height attribute gives information about the no of rows
dem.height
```




    5626




```python
#width attribute gives information about the no of columns
dem.width
```




    6711




```python
#crs attribute gives information about coordinate reference system of the raster file
dem.crs
```




    CRS.from_epsg(4326)




```python
#bounds attribute gives the coordinates of the corners of bounding box containing the raster data file
dem.bounds
```




    BoundingBox(left=73.34040191875982, bottom=17.894304891638686, right=75.14898008027765, top=19.410481428175615)




```python
#reading the data of raster data file using read() method and passing the band no as parameter
elevations = dem.read(1)
```


```python
#read() method creates an numpy array
type(elevations)
```




    numpy.ndarray




```python
#shape attribute of numpy array containing raster data
elevations.shape
```




    (5626, 6711)




```python
# raster data in a single band is read as 2D numpy arrary
elevations.ndim
```




    2




```python
#max() method gives the maximum element of 2D numpy array
elevations.max()
```




    1483




```python
#mean() method gives the mean of all elements of 2D numpy array
elevations.mean()
```




    606.6124299536768




```python
#min() method gives the minimum element of 2D numpy array
elevations.min()
```




    -13




```python
#np.median() method with 2D numpy array passed as a parameter gives the median of all elements 
np.median(elevations)
```




    608.0




```python
#rasterio.plot.show() method for visualisation of raster data file
from rasterio.plot import show
```


```python
help(rasterio.plot.show)
```

    Help on function show in module rasterio.plot:
    
    show(source, with_bounds=True, contour=False, contour_label_kws=None, ax=None, title=None, transform=None, adjust='linear', **kwargs)
        Display a raster or raster band using matplotlib.
        
        Parameters
        ----------
        source : array or dataset object opened in 'r' mode or Band or tuple(dataset, bidx)
            If Band or tuple (dataset, bidx), display the selected band.
            If raster dataset display the rgb image
            as defined in the colorinterp metadata, or default to first band.
        with_bounds : bool (opt)
            Whether to change the image extent to the spatial bounds of the image,
            rather than pixel coordinates. Only works when source is
            (raster dataset, bidx) or raster dataset.
        contour : bool (opt)
            Whether to plot the raster data as contours
        contour_label_kws : dictionary (opt)
            Keyword arguments for labeling the contours,
            empty dictionary for no labels.
        ax : matplotlib axes (opt)
            Axes to plot on, otherwise uses current axes.
        title : str, optional
            Title for the figure.
        transform : Affine, optional
            Defines the affine transform if source is an array
        adjust : 'linear' | None
            If the plotted data is an RGB image, adjust the values of
            each band so that they fall between 0 and 1 before plotting. If
            'linear', values will be adjusted by the min / max of each band. If
            None, no adjustment will be applied.
        **kwargs : key, value pairings optional
            These will be passed to the matplotlib imshow or contour method
            depending on contour argument.
            See full lists at:
            http://matplotlib.org/api/axes_api.html?highlight=imshow#matplotlib.axes.Axes.imshow
            or
            http://matplotlib.org/api/axes_api.html?highlight=imshow#matplotlib.axes.Axes.contour
        
        Returns
        -------
        ax : matplotlib Axes
            Axes with plot.
    
    


```python
show(elevations)
```


    
![png](09_Working_with_Numpy_files/09_Working_with_Numpy_113_0.png)
    





    <AxesSubplot:>




```python
#rasterio.plot.show_hist() method for plotting of histogram of raster data file
from rasterio.plot import show_hist
```


```python
show_hist(elevations)
```


    
![png](09_Working_with_Numpy_files/09_Working_with_Numpy_115_0.png)
    



```python

```


<iframe width="560" height="315" src="https://www.youtube.com/embed/QMkQ_MgmkMw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Lecture Slides

[Download Session10_Working with Numpy.pdf](pdfs/Session10_Working with Numpy.pdf)

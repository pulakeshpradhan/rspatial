# Exercise on matplotlib

Let us start with some simple plots


```python
# import the required modules

# preamble
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import datetime
```


```python
# let us construct a sine curve
x = np.linspace(0, 2*np.pi, 50)
plt.plot(x, np.sin(x))
```


```python
# decorations

x = np.linspace(0, 2*np.pi, 50)
plt.plot(x, np.sin(x), label='sin(x)')

# let us add the axis labels
plt.xlabel('x')
plt.ylabel('sin(x)')

# let us add the plot title
plt.title('Sine of X')

# let us add the legend 
plt.legend()
plt.show()
```


```python
# double frequency plot

x = np.linspace(0, 2*np.pi, 50)
plt.plot(x, np.sin(2*x), label='sin(2x)')

# let us add the axis labels
plt.xlabel('x')
plt.ylabel('sin(2x)')

# let us add the plot title
plt.title('Sinusoids')

# let us add the legend 
plt.legend()

plt.show()
```

## Exercise

Modify the code above to plot the cosine of X


```python

```


```python
# setting color of the line
y = np.linspace(0, 2*np.pi, 50)
plt.plot(y, np.cos(y), 'r')
```


```python
# setting color and width of the line
y = np.linspace(0, 2*np.pi, 50)
plt.plot(y, np.sin(y), 'g', linewidth=5)
```

## Exercise

Replace 'g' by 'g.', 'go', 'g+' to see their effects


```python

```


```python
# printing text on the plot and saving the plot as a file
y = np.linspace(0, 2*np.pi, 50)
plt.plot(y, np.sin(y), 'g', linewidth=5)
plt.annotate('local max', xy=(1.5, 1))
plt.savefig('sin.png')
```


```python
# overlaid plots 
# by default, 2 plot statements, will lead to over-plotting
y = np.linspace(0, 2*np.pi, 50)
plt.plot(y, np.sin(y), label='sin(y)')
plt.plot(y, np.cos(y), label='cos(y)')
plt.xlabel('y')
plt.ylabel('f(y)')
plt.legend()

# setting axes limits
plt.xlim(0, 2*np.pi)
plt.ylim(-1, 1)
```

## Exercise

Review all the statements above and try to plot the plot given below:

<img src="data/exercise3.png" alt="exercise image" width="500"/>


```python

```


```python
# let us see some more interesting graphs
t = np.arange(0.0, 5.0, 0.2)
plt.plot(t, t**2,'x') # t2
plt.plot(t, t**3,'ro') # t3
```


```python
# subplots and effect of different marker symbols
mark = ['x','o','^','+','>']
plt.figure(figsize=(12,8))
NR = 2 # number of rows
NC = 3 # number of columns
pn = 1
for row in range(NR):
    for col in range(NC):
        plt.subplot(NR, NC, pn)
        a = np.random.rand(10) * pn
        plt.plot(a, marker = mark[(pn+1)%5])
        plt.xlabel('plot {}X'.format(pn))
        plt.ylabel('plot {}Y'.format(pn))
        pn = pn + 1
```


```python
# pie chart
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs = [25, 25, 30, 20]
plt.pie(fracs, labels=labels)
```


```python
# polar plot
k = 12
th = np.linspace(0, 10*np.pi,1000)
r = np.cos(k*th)
plt.polar(th,r)
```


```python
# fractal diagram
X = 200
Y = 200
MAXIT = 100
MAXABS = 2.0
c = 0.02 - 0.8j # The constant in equation z**2 + c
m = np.zeros([X,Y]) # A two dimensional array

def numit(x,y): # number of iterations to diverge
    z = complex(x,y)
    for k in range(MAXIT):
        if abs(z) <= MAXABS:
            z = z**2 + c
        else:
            return k # diverged after k trials
    return MAXIT # did not diverge,

for x in range(X):
    for y in range(Y):
        re = 0.01 * x - 1.0 # complex number for
        im = 0.01 * y - 1.0 # this (x,y) coordinate
        m[x][y] = numit(re,im) # get the color for (x,y)
        
plt.imshow(m) # Colored plot using the 2D matrix
```


```python
# 3D plot
from mpl_toolkits.mplot3d import Axes3D

# Create a figure and a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate some sample 3D data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Set labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Display the plot
plt.show()
```

# Some real world examples

First let us see how we can **plot rainfall and runoff  data**

Daily precipitation and discharge over the period of 2005 to 2014 (3653 days), from gauging stations near University of Illinois, USA. There are 2 variables of interest, 'q' which is runoff (units in cfs), and 'r' which is rainfall (units in inches).

Source: https://serc.carleton.edu/hydromodules/steps/153828.html


```python
f = scipy.io.loadmat('data/sample_rainfall-runoff_data.mat')
f.keys()
```


```python
# discharge data 
f['q'].shape
```


```python
base = datetime.datetime(2005,1,1)
date_list = [base + datetime.timedelta(days=x) for x in range(3653)]
print('{} days, starting from {} till {}'.format(len(date_list), date_list[0], date_list[-2]))
```


```python
# There are 2 variables of interest, 'q' which is runoff (units cfs), and 'r' which is rainfall (units inches)

plt.figure(figsize=(12,5))
plt.subplot(1, 2, 1)
plt.plot(date_list, f['r'])
plt.subplot(1, 2, 2)
plt.plot(date_list, f['q'])
```


```python
# making publication quality graphs
fig, ax1 = plt.subplots(figsize=(12,5))

ax2 = ax1.twinx()
ax1.plot(date_list, f['r'], 'g-')
ax2.plot(date_list, f['q'], 'b-')
ax2.invert_yaxis()

ax1.set_xlabel('Year')
ax1.set_ylabel('Daily precipitation (inch)', color='g')
ax2.set_ylabel('Discharge (cfs)', color='b')
```

## Exercise

Can you programmatically zoom in to inspect individual storm event? Try and examine the rising and falling limbs of the hydrograph. 


```python

```

Next let us make a **basic contour plot**

Read in the monthly mean surface/near-surface air temperature from the NCEP/NCAR Reanalysis 1 netCDF dataset provided. Also read in the latitude and longitude vectors from the dataset. Extract a single timeslice of the temperature and plot a contour map. 

Source: "A Hands-On Introduction to Using Python in the Atmospheric and Oceanic Sciences," by Johnny Wei-Bing Lin (2012). https://github.com/jwblin/course_files


```python
fileobj = scipy.io.netcdf_file('data/air.mon.mean.nc', 'r')
T_time0 = np.array(fileobj.variables['air'][0,:,:])
T_units = fileobj.variables['air'].units.decode('UTF-8')
lon = np.array(fileobj.variables['lon'][:])
lon_units = fileobj.variables['lon'].units.decode('UTF-8')
lat = np.array(fileobj.variables['lat'][:])
lat_units = fileobj.variables['lat'].units.decode('UTF-8')
fileobj.close()
```


```python
#- Make 2-D longitude and latitude arrays:
[lonall, latall] = np.meshgrid(lon, lat)

#- Make a contour plot of the temperature:
plt.figure(figsize=(12,8))
mymapf = plt.contourf(lonall, latall, T_time0, 10, cmap=plt.cm.Reds)
mymap = plt.contour(lonall, latall, T_time0, 10, colors='k')
plt.clabel(mymap, fontsize=12)
plt.axis([0, 360, -90, 90])
plt.xlabel('Longitude [{}]'.format(lon_units))
plt.ylabel('Latitude [{}]'.format(lat_units))
cbar = plt.colorbar(mymapf, orientation='horizontal')
cbar.set_label('Temperature in {}'.format(T_units))
```

Notebook created by Prasun Kumar Gupta, Geoinformatics Department, Indian Institute of Remote Sensing (ISRO), Dehradun. Contact: prasun@iirs.gov.in


<iframe width="560" height="315" src="https://www.youtube.com/embed/qXsdgTGwqZ0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

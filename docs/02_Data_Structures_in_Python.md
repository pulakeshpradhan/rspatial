# Data Structures

## Tuples


```python
#Creation of Tuple with Tuple Literal
t1 = (1,2,3,4)
t1
```




    (1, 2, 3, 4)




```python
type(t1)
```




    tuple




```python
#Creation of Tuple with builtin tuple() function
t2 = tuple()
```


```python
t2
```




    ()




```python
type(t2)
```




    tuple




```python
t3 = tuple("Hello World")
```


```python
t3
```




    ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')




```python
type(t3)
```




    tuple




```python
#integer can't be passed as an argument to tuple() method
t4 = tuple(1)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp/ipykernel_9284/3320543265.py in <module>
    ----> 1 t4 = tuple(1)
    

    TypeError: 'int' object is not iterable



```python
t5 = (1)
```


```python
type(t5)
```




    int




```python
t6 = ('a')
```


```python
type(t6)
```




    str




```python
t7 = (1,)
```


```python
t7
```




    (1,)




```python
type(t7)
```




    tuple




```python
#length of a Tuple
len(t1)
```




    4



#### Tuple Indexing and Slicing


```python
t8 = (1,2,3,4,'a','b',"Hello World", 2.6, True)
```


```python
type(t8)
```




    tuple




```python
t8[0]
```




    1




```python
t8[0:4]
```




    (1, 2, 3, 4)




```python
t8[-1]
```




    True



#### Tuple Packing & Unpacking


```python
series = 1,2,3,4,5
```


```python
series
```




    (1, 2, 3, 4, 5)




```python
type(series)
```




    tuple




```python
coordinates = 78.5,20.5
coordinates
```




    (78.5, 20.5)




```python
x = coordinates[0]
y = coordinates[1]
```


```python
x
```




    78.5




```python
y
```




    20.5




```python
x2, y2, location = 79.5 , 21.4 , 'XYZ'
```


```python
x2
```




    79.5




```python
y2
```




    21.4




```python
location
```




    'XYZ'




```python
#use of in keyword to check the presence of an element in a Tuple
"Hello World" in t8 
```




    True




```python
"hello world" in t8
```




    False



##### Tuples are immutable 


```python
t8[0]=5
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp/ipykernel_9284/3795153408.py in <module>
    ----> 1 t8[0]=5
    

    TypeError: 'tuple' object does not support item assignment


## Lists


```python
#creation of list with list literal
l1=[1,2,3,4,5]
```


```python
type(l1)
```




    list




```python
#creation of list with list() built in function
l2=list()
l2
```




    []




```python
type(l2)
```




    list




```python
l3=list("Hello World")
l3
```




    ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']




```python
# A Tuple can be passed as an argument in list() function
l4=list((1,2,3))
```


```python
l4
```




    [1, 2, 3]




```python
type(l4)
```




    list




```python
 strng1="Central Water Commission is a premier Technical Organization of India in the field of Water Resources\
and is presently functioning as an attached office of the Ministry of Jal Shakti, Department of\
Water Resources, River Development and Ganga Rejuvenation, Government of India."
```


```python
#creation of list of strings with split() function
strng1.split()
```




    ['Central',
     'Water',
     'Commission',
     'is',
     'a',
     'premier',
     'Technical',
     'Organization',
     'of',
     'India',
     'in',
     'the',
     'field',
     'of',
     'Water',
     'Resourcesand',
     'is',
     'presently',
     'functioning',
     'as',
     'an',
     'attached',
     'office',
     'of',
     'the',
     'Ministry',
     'of',
     'Jal',
     'Shakti,',
     'Department',
     'ofWater',
     'Resources,',
     'River',
     'Development',
     'and',
     'Ganga',
     'Rejuvenation,',
     'Government',
     'of',
     'India.']




```python
strng2 = "Pune,Nagpur,Hyderabad,Bangalore"
```


```python
l5= strng2.split(',')
l5
```




    ['Pune', 'Nagpur', 'Hyderabad', 'Bangalore']



#### List indexing and slicing


```python
l5[2]
```




    'Hyderabad'




```python
l5[0:2]
```




    ['Pune', 'Nagpur']




```python
l6=[1,2,3,4,5,6,7,8,9,10]
```


```python
l6[:]
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
l6[0:]
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
l6[:-1]
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
l6[::2]
```




    [1, 3, 5, 7, 9]




```python
l7=[[1,2],[3,4]] #nested list
l7
```




    [[1, 2], [3, 4]]




```python
l7[0]
```




    [1, 2]




```python
l7[0][0] # Double index notation
```




    1



#### List Mutability


```python
l6
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
l6[0]=0
```


```python
l6
```




    [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
l6[1:3]=[11,12]
l6
```




    [0, 11, 12, 4, 5, 6, 7, 8, 9, 10]




```python
l8=['a','b']
l9=['c','d']
```


```python
l8+l9
```




    ['a', 'b', 'c', 'd']




```python
l8*2
```




    ['a', 'b', 'a', 'b']



#### List Methods


```python
l5
```




    ['Pune', 'Nagpur', 'Hyderabad', 'Bangalore']




```python
l5.insert(0,'Chennai')
```


```python
l5
```




    ['Chennai', 'Pune', 'Nagpur', 'Hyderabad', 'Bangalore']




```python
#list methods alter lists in place and return None
l5=l5.insert(0,'Mumbai')
```


```python
l5
```


```python
type(l5)
```




    NoneType




```python
l10=['A', 'B', 'C','D','E']
```


```python
l10.insert(10,'F')
```


```python
l10
```




    ['A', 'B', 'C', 'D', 'E', 'F']




```python
l8
```




    ['a', 'b']




```python
l8.insert(-1,'c')
l8
```




    ['a', 'c', 'b']




```python
l9
```




    ['c', 'd']




```python
l9.append('e')
```


```python
l9
```




    ['c', 'd', 'e']




```python
l9.pop()
l9
```




    ['c', 'd']




```python
l9.pop(0)
l9
```




    ['d']




```python
type(l9)
```




    list




```python
l9.extend(['e',1,4.5]) #passing list as an argument to extend() function
l9
```




    ['d', 'e', 1, 4.5]




```python
l9.extend((5,6,7)) #passing tuple as an argument to extend() function
l9
```




    ['d', 'e', 1, 4.5, 5, 6, 7]




```python
l9.append('e')
l9
```




    ['d', 'e', 1, 4.5, 5, 6, 7, 'e']




```python
l9.count('e')
```




    2




```python
l9.index(1)
```




    2




```python
l9.reverse()
```


```python
l9
```




    ['e', 7, 6, 5, 4.5, 1, 'e', 'd']




```python
l11=['Mumbai', 'pune','ahmadabad','Hyderabad']
```


```python
l11.sort()
l11
```




    ['Hyderabad', 'Mumbai', 'ahmadabad', 'pune']




```python
l12=[0.5,3.9,12.7,2.3,7.0]

```


```python
l12.sort(reverse=True)
l12
```




    [12.7, 7.0, 3.9, 2.3, 0.5]




```python
0.5 in l12
```




    True



## Sets


```python
#creation of set with set literal
set1 = {1,2,3}
```


```python
type(set1)
```




    set




```python
list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
```


```python
list1.extend(list2)
```


```python
list1
```




    [1, 2, 3, 4, 5, 3, 4, 5, 6, 7]




```python
#creation of set from a list
set2 = set(list1)
```


```python
set2
```




    {1, 2, 3, 4, 5, 6, 7}




```python
#Index is not attached to an element of a set
set2[0]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp/ipykernel_9284/2138154667.py in <module>
          1 #Index is not attached to an element of a set
    ----> 2 set2[0]
    

    TypeError: 'set' object is not subscriptable



```python
#check presence of an element using in keyword
1 in set2
```




    True




```python
#Intersection of two sets
set2.intersection(set1)
```




    {1, 2, 3}




```python
#union of two sets
set2.union(set1)
```




    {1, 2, 3, 4, 5, 6, 7}



## Dictionary


```python
#creation of dictionary using dict() buil in function
dictionary1=dict()
```


```python
dictionary1
```




    {}




```python
type(dictionary1)
```




    dict




```python
#creation of dictionary with dictionary literal
car_details = {'name' : 'Fiat', 'color': 'Blue', 'engineSize': 1000, 'Dimensions':[4.5,2,1.5]}
```


```python
type(car_details)
```




    dict




```python
#accessing value associated with any key in the dictionary
car_details['color']
```




    'Blue'




```python
#dictionaries are mutable
car_details['year of manufacture']=2015
```


```python
car_details
```




    {'name': 'Fiat',
     'color': 'Blue',
     'engineSize': 1000,
     'Dimensions': [4.5, 2, 1.5],
     'year of manufacture': 2015}




```python
car_details['color'] = 'Grey'
```


```python
car_details
```




    {'name': 'Fiat',
     'color': 'Grey',
     'engineSize': 1000,
     'Dimensions': [4.5, 2, 1.5],
     'year of manufacture': 2015}




```python
Annual_rainfall_Cities = (('Delhi',800), ('Pune',850),('Mumbai',2400), ('Jodhpur',350))
```


```python
#creation of dictionary from a Tuple of Tuples
Rainfall_of_Cities = dict(Annual_rainfall_Cities)
```


```python
type(Rainfall_of_Cities)

```




    dict




```python
Rainfall_of_Cities
```




    {'Delhi': 800, 'Pune': 850, 'Mumbai': 2400, 'Jodhpur': 350}




```python
#deletion of any key:value pair from dictionary
del car_details['year of manufacture']
```


```python
car_details
```




    {'name': 'Fiat',
     'color': 'Grey',
     'engineSize': 1000,
     'Dimensions': [4.5, 2, 1.5]}




```python
#check presence of any key in a dictionary using in keyword.It is not possible to check value
'Delhi' in Rainfall_of_Cities
```




    True




```python
'Hyderabad' in Rainfall_of_Cities
```




    False




```python
#dictionary method items() creates a new data type of dict_item
Rainfall_of_Cities.items()
```




    dict_items([('Delhi', 800), ('Pune', 850), ('Mumbai', 2400), ('Jodhpur', 350)])




<iframe width="560" height="315" src="https://www.youtube.com/embed/XtHkTYjH27U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Lecture Visualization

<embed src="pdfs/Session3_Data Structures in Python.pdf" type="application/pdf" width="100%" height="600px" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />

<p align="center"><a href="pdfs/Session3_Data Structures in Python.pdf" class="md-button md-button--primary">Download Lecture Slides</a></p>

??? info "View Full Lecture Transcript"
    The following content is extracted from the lecture slides.

    Data Structures

    in Python

    Chaitanya K S

    Deputy Director

    National Water Academy

    Central Water Commission, Pune

    Data Structures in Python

    • Data Structures are meant to efficiently store, organize and access

    the data

    • Individual items of data stored in Data Structures are of basic Data

    Types

    • Built in Data Structures in Python

    ▪ Tuples

    ▪ Lists

    ▪ Sets

    ▪ Dictionaries

    • What Data Structure to chose for storing, organizing and accessing

    the data depends on the type of data and the problem at hand

    Thank you


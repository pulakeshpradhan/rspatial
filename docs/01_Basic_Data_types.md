# Basic Data Types

## Strings


```python
x = '2'
```


```python
type(x)
```




    str




```python
y ="Hello World"
```


```python
type(y)

```




    str




```python
z = 'They've come long way'
```


      File "C:\Users\COMP109\AppData\Local\Temp/ipykernel_8816/1277197612.py", line 1
        z = 'They've come long way'
                  ^
    SyntaxError: invalid syntax
    



```python
# Use double quotations if there is a single quotation within the string
zz = "They've come long way"
```


```python
# Descriptive variable names are prefered
Name_of_rainfall_station = 'Pune'
```


```python
# Multi line string
"Central Water Commission is a premier Technical Organization of India in the field of Water Resources
and is presently functioning as an attached office of the Ministry of Jal Shakti, Department of 
Water Resources, River Development and Ganga Rejuvenation, Government of India."
```


      File "C:\Users\COMP109\AppData\Local\Temp/ipykernel_8816/3541219196.py", line 2
        "Central Water Commission is a premier Technical Organization of India in the field of Water Resources
                                                                                                              ^
    SyntaxError: EOL while scanning string literal
    



```python
paragraph = '''Central Water Commission is a premier Technical Organization of India in the field of Water Resources
and is presently functioning as an attached office of the Ministry of Jal Shakti, Department of 
Water Resources, River Development and Ganga Rejuvenation, Government of India.'''
```


```python
paragraph
```




    'Central Water Commission is a premier Technical Organization of India in the field of Water Resources\nand is presently functioning as an attached office of the Ministry of Jal Shakti, Department of \nWater Resources, River Development and Ganga Rejuvenation, Government of India.'




```python
b = "Central Water Commission is a premier Technical Organization of India in the field of Water Resources\
and is presently functioning as an attached office of the Ministry of Jal Shakti, Department of\
Water Resources, River Development and Ganga Rejuvenation, Government of India."
```


```python
len("Hello World")
```




    11



#### String Indexing


```python
y
```




    'Hello World'




```python
y[0]
```




    'H'




```python
y[len(y)]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    ~\AppData\Local\Temp/ipykernel_8816/3552869512.py in <module>
    ----> 1 y[len(y)]
    

    IndexError: string index out of range



```python
y[len(y)-1]
```




    'd'




```python
y[-1]
```




    'd'



#### String Concatenation


```python
first_name = 'Madhya'
```


```python
last_name = 'Pradesh'
```


```python
full_name = first_name + last_name
```


```python
full_name
```




    'MadhyaPradesh'




```python
full_name = first_name + ' ' + last_name
```


```python
full_name
```




    'Madhya Pradesh'



#### String Slicing


```python
substrng1 = full_name[7] + full_name[8] + full_name[9]
```


```python
substrng1
```




    'Pra'




```python
print(full_name[7:9])
```

    Pr
    


```python
substrng2 = full_name[7:10]
```


```python
print(substrng2)
```

    Pra
    


```python
y[0:]
```




    'Hello World'




```python
y[:10]
```




    'Hello Worl'




```python
y[:]
```




    'Hello World'




```python
y[:-1]
```




    'Hello Worl'




```python
y[-5:]
```




    'World'




```python
a = 2
b ='2'
```


```python
print(a)
print(b)
```

    2
    2
    


```python
a == b
```




    False




```python
y
```




    'Hello World'




```python
#Strings are immutable and can't be altered
y[0]= 'h'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp/ipykernel_8816/532274940.py in <module>
          1 #Strings are immutable and can't be altered
    ----> 2 y[0]= 'h'
    

    TypeError: 'str' object does not support item assignment



```python
yy = 'h' + y[1:]
```


```python
yy
```




    'hello World'



#### String Methods

###### Use tab completion in notebook to explore more string methods


```python
yy.upper()
```




    'HELLO WORLD'




```python
full_name
```




    'Madhya Pradesh'




```python
full_name.lower()
```




    'madhya pradesh'




```python
c ='   Pune'
```


```python
c.lstrip()
```




    'Pune'




```python
'Pune   '.rstrip()
```




    'Pune'




```python
'   Pune   '.strip()
```




    'Pune'




```python
full_name.startswith('ma')
```




    False




```python
full_name.startswith("Ma")
```




    True




```python
full_name.endswith('sh')
```




    True




```python
help(len)
```

    Help on built-in function len in module builtins:
    
    len(obj, /)
        Return the number of items in a container.
    
    


```python
x = '2'
```


```python
#convert string to integer
int(x)
```




    2




```python
#convert integer to a string
str(2)
```




    '2'




```python
#convert float to a string
str(2.5)
```




    '2.5'




```python
float(x)
```




    2.0




```python
float(2)
```




    2.0




```python
int(2.56)
```




    2




```python
# + operation between two strings results in string concatenation 
x + x
```




    '22'




```python
int(x)+int(x)
```




    4




```python
x * 3
```




    '222'




```python
d = input('enter an integer : ')
```

    enter an integer : 
    


```python
d
```




    ''




```python
int(d)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp/ipykernel_8816/2949999978.py in <module>
    ----> 1 int(d)
    

    ValueError: invalid literal for int() with base 10: ''



```python
d = input('enter an integer : ')
e = input('enter second integer : ')
f = int(d)*int(e)
f
```

    enter an integer : 
    enter second integer : 
    


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp/ipykernel_8816/3165118068.py in <module>
          1 d = input('enter an integer : ')
          2 e = input('enter second integer : ')
    ----> 3 f = int(d)*int(e)
          4 f
    

    ValueError: invalid literal for int() with base 10: ''


#### f strings


```python
# It is possible to recall the value of any variable from a previous executed cell
d
```




    ''




```python
e
```




    ''




```python
# fstrings are used to insert value of any type of variable at places of choice within a string
f"{d} times {e} is {f}"
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp/ipykernel_8816/904092031.py in <module>
          1 # fstrings are used to insert value of any type of variable at places of choice within a string
    ----> 2 f"{d} times {e} is {f}"
    

    NameError: name 'f' is not defined



```python
paragraph
```




    'Central Water Commission is a premier Technical Organization of India in the field of Water Resources\nand is presently functioning as an attached office of the Ministry of Jal Shakti, Department of \nWater Resources, River Development and Ganga Rejuvenation, Government of India.'




```python
# string method 'find' returns the starting index of the substring in its first incidence
paragraph.find('Commission')
```




    14




```python
paragraph.replace("Jal Shakti","Jalshakti")
```




    'Central Water Commission is a premier Technical Organization of India in the field of Water Resources\nand is presently functioning as an attached office of the Ministry of Jalshakti, Department of \nWater Resources, River Development and Ganga Rejuvenation, Government of India.'



## Basic numerical data types - Integers & Floats 


```python
#Exponential notation of float with positive exponent

1e3
```




    1000.0




```python
#Exponential notation of float with negative exponent

1e-3
```




    0.001




```python
# Representation of large integers. Commas are not allowed

100_000_000
```




    100000000




```python
# any operation between an integer and float will yield a float

g = 5 + 2.0
g
```




    7.0




```python
type(g)
```




    float




```python
h = 5 + 2 
h
```




    7




```python
type(h)
```




    int




```python
5.0/2
```




    2.5




```python
#Integer Division

5.0//2
```




    2.0




```python
#Modulus operation 

5 % 3
```




    2




```python
#Exponential function
2 ** 2
```




    4



#### Boolean Data Type


```python
g == h
```




    True




```python
g != h
```




    False




<iframe width="560" height="315" src="https://www.youtube.com/embed/iDWyJcB1FMo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

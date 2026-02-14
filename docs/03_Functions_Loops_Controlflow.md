# Functions


```python
#User defined function
def sum_of_integers(x,y):
    return x+y
```


```python
#Calling of the user defined by passing arguments into the parenthesis
sum_of_integers(2,3)
```




    5




```python
z = sum_of_integers(3,4)
z
```




    7




```python
#passing of arguments less or greater than the number of parameters into a function 
sum_of_integers(2,3,4)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp/ipykernel_7880/2773305214.py in <module>
          1 #passing of arguments less or greater than the number of parameters into a function
    ----> 2 sum_of_integers(2,3,4)
    

    TypeError: sum_of_integers() takes 2 positional arguments but 3 were given



```python
#Arbritrary Arguments(*args)
#Used when it is not known in advance how many arguments will be passed in to the function

def func1 (*args):
    return(args)
```


```python
#arbritary postional arguments are collected as a tuple
func1(1,2,3,4,'a','b')
```




    (1, 2, 3, 4, 'a', 'b')




```python
def welcome_participant(first_name,last_name):
    full_name = first_name+' '+last_name
    print(f"Hello '{full_name}', How do you do?")
```


```python
#positional arguments has to follow the order of parameters
#keyword arguments can be passed in any order
welcome_participant(last_name = 'Kumar', first_name = 'Ashok')
```

    Hello 'Ashok Kumar', How do you do?
    


```python
# Arbitrary keyword arguments
def func2(**kwargs):
    return (kwargs)
```


```python
# Arbitrary keyword arguments are collected as a dictionary
func2(x=2,y=3,z=5)
```




    {'x': 2, 'y': 3, 'z': 5}




```python
list1=[67,12,89,32,97,9]
```


```python
list1.sort()
list1
```




    [9, 12, 32, 67, 89, 97]




```python
help(list1.sort)
```

    Help on built-in function sort:
    
    sort(*, key=None, reverse=False) method of builtins.list instance
        Sort the list in ascending order and return None.
        
        The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
        order of two equal elements is maintained).
        
        If a key function is given, apply it once to each list item and sort them,
        ascending or descending, according to their function values.
        
        The reverse flag can be set to sort in descending order.
    
    


```python
#overwriting the default parameter of the list method sort()
list1.sort(reverse=True)
```


```python
list1 #in descending order
```




    [97, 89, 67, 32, 12, 9]




```python
#lambda functions have a format lambda parameter1, parameter2... : expression
#lambda functions act as anonymous functions(undefined) 
#lambda function can be passed as an argument to any function
c = lambda a,b : a+b
c(1,2)
```




    3




```python
#error in trying to call a function from math module
sqrt(16)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp/ipykernel_7880/2843140530.py in <module>
          1 #error in trying to call a function from math module
    ----> 2 sqrt(16)
    

    NameError: name 'sqrt' is not defined



```python
import math
math.sqrt(16)
```




    4.0




```python
math.sin(1)
```




    0.8414709848078965




```python
#A constant defined in math module
math.pi
```




    3.141592653589793




```python
print(dir(math))
```

    ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
    


```python
#scope of variables
x = 5.0

def doubling_of_number(a):
    x=2.0
    print(f"Inside the function, value of x is {x}")
    return a*x
          
doubling_of_number(3)
print(f"Outside the function, value of x is {x}")
```

    Inside the function, value of x is 2.0
    Outside the function, value of x is 5.0
    


```python
x = 5.0

def doubling_of_number(a):
    print(f"Inside the function, value of x is {x}")
    return a*x
          
doubling_of_number(3)
print(f"Outside the function, value of x is {x}")
```

    Inside the function, value of x is 5.0
    Outside the function, value of x is 5.0
    


```python
help(len)
```

    Help on built-in function len in module builtins:
    
    len(obj, /)
        Return the number of items in a container.
    
    


```python
# Including a docstring inside a user defined function
def product(a,b):
    '''
    Return the product of two numbers which are either integers or floats
    '''
    return a*b
```


```python
help(product)
```

    Help on function product in module __main__:
    
    product(a, b)
        Return the product of two numbers which are either integers or floats
    
    

# Loops

#### while loops


```python
i = 0

while i <=5 :
    print(i)
    i += 1 # same as i=i+1
```

    0
    1
    2
    3
    4
    5
    

#### For loops


```python
#iterating over a list of elements
for i in [1,2,3,4,5]:
    print(i)
```

    1
    2
    3
    4
    5
    


```python
#iterating over a tuple
for i in ('a','b','c','d','e'):
    print(i)
```

    a
    b
    c
    d
    e
    


```python
#iterating over a string
for i in 'Hello World':
    print(i)
```

    H
    e
    l
    l
    o
     
    W
    o
    r
    l
    d
    


```python
help(enumerate)
```

    Help on class enumerate in module builtins:
    
    class enumerate(object)
     |  enumerate(iterable, start=0)
     |  
     |  Return an enumerate object.
     |  
     |    iterable
     |      an object supporting iteration
     |  
     |  The enumerate object yields pairs containing a count (from start, which
     |  defaults to zero) and a value yielded by the iterable argument.
     |  
     |  enumerate is useful for obtaining an indexed list:
     |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
     |  
     |  Methods defined here:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __next__(self, /)
     |      Implement next(self).
     |  
     |  __reduce__(...)
     |      Return state information for pickling.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  __class_getitem__(...) from builtins.type
     |      See PEP 585
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
    
    


```python
index_value = enumerate([1,2,3,4,5])
```


```python
#iterating over enumerate object
for index, value in enumerate([1,2,3,4,5]):
    print(index, value)
```

    0 1
    1 2
    2 3
    3 4
    4 5
    


```python
help(range)
```

    Help on class range in module builtins:
    
    class range(object)
     |  range(stop) -> range object
     |  range(start, stop[, step]) -> range object
     |  
     |  Return an object that produces a sequence of integers from start (inclusive)
     |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
     |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
     |  These are exactly the valid indices for a list of 4 elements.
     |  When step is given, it specifies the increment (or decrement).
     |  
     |  Methods defined here:
     |  
     |  __bool__(self, /)
     |      self != 0
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __reversed__(...)
     |      Return a reverse iterator.
     |  
     |  count(...)
     |      rangeobject.count(value) -> integer -- return number of occurrences of value
     |  
     |  index(...)
     |      rangeobject.index(value) -> integer -- return index of value.
     |      Raise ValueError if the value is not present.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  start
     |  
     |  step
     |  
     |  stop
    
    


```python
#iterating over a range object
for j in range(5):
    print(j)
```

    0
    1
    2
    3
    4
    


```python
#Overwriting the default argument for start in range() function
for k in range(1,5):
    print(k)
```

    1
    2
    3
    4
    

# Conditional Logic and Control Flow


```python
type(False)
```




    bool




```python
not True
```




    False




```python
#comparison of strings 
'abc' < 'cde'
```




    True




```python
'a' == "A"
```




    False




```python
'a' != 'A'
```




    True




```python
#logical operators are used to compound boolean expressions
(3<5)and(5<7)
```




    True




```python
#nested if statement
x = 7

if x>0 :
    if x%2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
```

    7 is odd
    


```python
#combination of for loop and if-else statements
for i in range(100):
    if i>0 :
        if i%2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")
```

    1 is odd
    2 is even
    3 is odd
    4 is even
    5 is odd
    6 is even
    7 is odd
    8 is even
    9 is odd
    10 is even
    11 is odd
    12 is even
    13 is odd
    14 is even
    15 is odd
    16 is even
    17 is odd
    18 is even
    19 is odd
    20 is even
    21 is odd
    22 is even
    23 is odd
    24 is even
    25 is odd
    26 is even
    27 is odd
    28 is even
    29 is odd
    30 is even
    31 is odd
    32 is even
    33 is odd
    34 is even
    35 is odd
    36 is even
    37 is odd
    38 is even
    39 is odd
    40 is even
    41 is odd
    42 is even
    43 is odd
    44 is even
    45 is odd
    46 is even
    47 is odd
    48 is even
    49 is odd
    50 is even
    51 is odd
    52 is even
    53 is odd
    54 is even
    55 is odd
    56 is even
    57 is odd
    58 is even
    59 is odd
    60 is even
    61 is odd
    62 is even
    63 is odd
    64 is even
    65 is odd
    66 is even
    67 is odd
    68 is even
    69 is odd
    70 is even
    71 is odd
    72 is even
    73 is odd
    74 is even
    75 is odd
    76 is even
    77 is odd
    78 is even
    79 is odd
    80 is even
    81 is odd
    82 is even
    83 is odd
    84 is even
    85 is odd
    86 is even
    87 is odd
    88 is even
    89 is odd
    90 is even
    91 is odd
    92 is even
    93 is odd
    94 is even
    95 is odd
    96 is even
    97 is odd
    98 is even
    99 is odd
    


```python
elevation_of_cities = (('Pune',560),('Delhi',200), ('Kolkata',10), ('Mumbai',15),('Darjeeling',2000))
```


```python
type(elevation_of_cities)
```




    tuple




```python
elevation_cities_dictionary = dict(elevation_of_cities)
elevation_cities_dictionary
```




    {'Pune': 560, 'Delhi': 200, 'Kolkata': 10, 'Mumbai': 15, 'Darjeeling': 2000}




```python
#iterating over keys of a dictionary and combination with if-elif-else statements
for city in elevation_cities_dictionary:
    if elevation_cities_dictionary[city] > 1000:
        print(f"{city} is located at higher elevation")
    elif 1000 > elevation_cities_dictionary[city] > 100:
        print(f"{city} is located at moderate elevation")
    else:
        print(f"{city} is located at lower elevation")
```

    Pune is located at moderate elevation
    Delhi is located at moderate elevation
    Kolkata is located at lower elevation
    Mumbai is located at lower elevation
    Darjeeling is located at higher elevation
    


```python

```


<iframe width="560" height="315" src="https://www.youtube.com/embed/_fbx9BH7qHQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

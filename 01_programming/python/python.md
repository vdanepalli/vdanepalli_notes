# 


- type() -- type of the object
- isinstance() -- 
- len() -- length of the object
- enumerate() -- for index, value in enumerate(say_list_object);produces sequence of pairs
- range() -- from, to, step ; [from, to)

<br/>
<br/>

---- 

<br/>
<br/>



- list -- close to an array: hybrid version of array and linkedList
elements need not be of same type


# Educative : Python for Multithreaded Applications

## Intro 

### Intro to Python 

-  1990, general purpose programming language, high level interpreted language
-  compilation -- python does it for us behind the scenes
-  readability 
-  applications 
   -  web, AI, Data Science, Image Processing, Operating System
-  `print("a", 1, True, end='')`
-  #Comments and """Doc Strings"""

### Data Types and Variables 

- data type: defines type and range of values 
- Numbers
  - Integers 
    - Amount of memory integer occupies depends on its value; 0 -- 24 bytes and 1 -- 28 bytes
    - Negative numbers start with - 
  - Floating Point Numbers
    - occupies 24 bytes memory
    - 5 is int while 5.0 is float
  - Complex Numbers
    - `complex(real, imaginary)`
    - `complex(3,9) #3+9j`
    - python follows electrical engineering convention which uses j instead of i
    - usually takes 32 bytes of memory
-  Strings -- collection of characters enclosed in ''  | "" | """ """ | ''' '''
   -  `len(random_string)` 
   -  indexing starts from 0
   -  `012345` -- forward indexing
   -  `-6-5-4-3-2-1` -- reverse indexing
   -  `random_string[0] | random_string[-1]` -- character at that index
   -  Strings are immutable: 'str' object does not support item assignment: TypeError;
   -  ```python
        str1 = "hello"
        print(id(str1)) # say id30252
        str1 = "bye"
        print(id(str1)) # say id02344
        # "hello" and "bye" are two different strings and hence different ids
        ```
    - All strings are unicode in python 3.x; 
    - python 2.x support only ASCII -- to use unicode `string = u"This is unicode. Preceding string with u is must`
-  Booleans --  `True or False`
-  NoneType -- value is None
   -  `val = None; type(val) --> <class 'NoneType'>`
   -  None is not default value for unassigned variable, not same as False, not an empty string, not 0
- Variable: name to which a value can be assigned; variable=value; Mutable; Case Sensitive; can start with _ or lower case or upper case letter but not a digit; snake_case, camelCase, PascalCase


<br/>
<br/>


- Slicing - obtaining substring using indices 
  - `string[start:end:step]` -- end is not included
  - `[:]    [start:]    [:end]  [::-1]`

### Operators in Python 

- arithmetic and logical operations; Pythons operators follow in-fix (appear between two operands and are also known as binary operators) or prefix notations (works on one operand and are also known as unary operators)
- arithmetic operators -- `| () |  ** | %, *, /, // | +, - |` -- left to right precedence when tie.
  - division operation always results in floating-point number
  - `print(5.5//4.5) # 1.0`
  - `print(-28 % 10) # 2` -- remainder is positive if right hand operand is positive
  - `print(28 % -10) # -2` -- remainder is negative if right hand operand is negative
  - remainder can be a float
- comparision operators -- `>, <, >=, <=, ==, !=, is (equal to identity), is not`
  - ```python
    n1 = 39
    n2 = 39
    l1 = [5, 3, 9]
    l2 = [5, 3, 9]
    print(n1 is n2) # true
    print(l1 is l2) # false
    ```
- assignment operators -- `=, +=, -=, *=, /=, //=, **=, %=, |=, &=, ^=(XOR and assign), >>=, <<=`
- logical operators -- `and, or, not`
- bitwise operators -- `&, |, ^(XOR), ~, <<, >>`
- string operations 
  - strings are compatible with comparision operators. each char has unicode value
  - `+ operator` -- concatenate or merge strings
  - `* operator` -- repeat string by specified number of times
  - `in operator` -- `'checkifIamIn in "will print true if checkifIamIn is present"`
- Gravitational force is the attractive force that exists between two masses and is calculated as  ( G * M * m ) / (r ** 2)


## Working with Data -4h

- DataStructure - a way of storing and organizing data according to certain format or structure.
- list 
  - `list1 = []`; lists are ordered similar to strings; heterogenous; mutable
  - `range(start, end, step)`
  - `list(range(0, 3)) -> [0, 1, 2]`
  - allows nested lists. follow sequential indexing to get data
  - `list1 + list2` -- produces merged list
  - `list1.extend(list2)` -- adds list2 at end of list1
  - `list1.append(new_element)` -- adds element at end of list1
  - `list1.insert(index, new_element)` -- inserts elment new_element at index index; if index > len then inserts at end of list1
  - `list1.pop()` -- removes last element of the list
  - `list1.remove(element_to_delete)` -- deletes particular value; if not present -- error -- elemnt_to_delete not in list -- ValueError
  - `list1.index(elment)` -- index of first occurence of element; Throws ValueError if not in list.
  - `list1.sort()` -- sort in ascending order. Throws TypeError is int and str are present in list. <br><br>

  - Listcomprehension -- technique that uses a for loop and a condition to create new list from existing one; result is always a new list
    - `[expression(creates elements) for_loop(iterate existing list) if_condition(decides if element should be added to new list)]`
    - `sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]`
    - 

- tuple -- immutable; can contain mutable elements which can be altered; ordered.  `()`
- dictionary -- stores key:value pairs where each unique key is an index which holds the value associated with it; unordered -- entries are not stored in a linear structure. `{}`
  - key value pairs are accessed in a random or unordered manner
  - `d = {"ash":539, "win":512}`
  - `phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)` -- keys will be automatically converted to strings and keys shouldn't contain special chars.
  - `dict_name[key_name]` -- will get the value associated with the key; KeyError if key not present.
  - `dict_name.get("key")` -- returns None if key not present.
  - `del dict_name[key_name]` -- deletes associated pair. KeyError if not exists
  - `dict_name.pop(key_name)` -- pops and returns the value. KeyError if not exists
  - `dict_name.popitem()` -- removes and returns last inserted pair as a tuple. Prior to python 3.7, removes and returns random item
  - `dict1.update(dict2)` -- adds dict2 key:value pairs to dict1
  - Dictionary Comprehension -- use dict.items() to iterate; -- turns a dictionary into a list of (key,value) tuples. 
    ```python
    houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
    new_houses = {n**2: house + "!" for (n, house) in houses.items()}
    print(houses)
    print(new_houses)
    ```
- set -- unordered collection of data items
  - cannot add mutable data structures like lists or dictionaries to sets; if included -- TypeError: unhashable type 'list'
  - `{1, 2, 3}`
  - `set()` 
  - `set1.add(element)` or `set1.update(container)` -- container can be set, list, tuple or string
  - `set1.discard(element)` -- ignores if element not found or `set1.remove(element)` -- throws keyError if element not found
  - Union -- `setA | setB` or `setA.union(setB)`
  - Intersection -- `setA & setB` or `setA.intersection(setB)`
  - Difference -- `setA - setB` != `setB.difference(setA)`
- Explicit type conversion `destination_structure_name(source_structure_object)`
- list(tuple | set | dict) --gives list; in case of dictionary, only keys will be converted to list.
- `dict.items() -- (key, value) tuples -- dict_items([(), (), (), ...])`
- tuple(list | dict | set)
- `my_tuple = (my_list[0], my_list[len(my_list) - 1], len(my_list))`
- set( list | dict | tuple)
- dict(list_of_lists | list_of_tuples | tuple_of_tuples | set_of_tuples)
- Shallow copy: Objects can contain references to other objects. If we copy the object, the references in the object are copied but not the referenced objects themselves. 
- ```python 
    grades = [["Mary", "A+"], ["Don", "C-"]] # original grades 2D list
    print("Original Grades:", grades)

    grades2 = grades[:] # setting up grades2 list
    grades2[0] = ["Bob", "B"] # changing the list itself, so no effect on grades
    grades2[1][1] = "F" # modifying cuntent of the referenced object, so affects both grades and grades2
    print("New Grades:", grades) # prints [["Mary", "A+"], ["Don", "F"]]
    ```
- Deep copy `import copy` -- `copy.deepcopy(grades_list_of_lists)
- Callee -- function called by another; Caller -- function that calls another function (callee)
- Actual Parameters -- passed during function call
- Formal Parameters -- values received by the function (when it is called)
- Pass by value -- copy of the data is sent to the callee
  - multi-threaded application - no worry of objects getting modified
  - distributed application - saves network overhead to keep the objects in sync
- Pass by reference -- pass by address -- copy of address of actual parameter is sent to callee
  - overhead of copying is saved
- Kth Max integer in a list `test_list.sort(); kth_max = test_list[-k]`
- Highs and Lows 
  ```python 
    def count_low_high(num_list):
    high_list = list(filter(lambda n: n > 50 or n % 3 == 0, num_list))
    low_list = list(filter(lambda n: n <= 50 and not n % 3 == 0, num_list))
    return [len(low_list), len(high_list)]

    ----------------------------------------------------------------

    def count_low_high(num_list):
        if (len(num_list)==0):
            return None
        high_list = len([n for n in num_list if n > 50 or n % 3 == 0])
        low_list = len([n for n in num_list if n <= 50 and not n % 3 == 0])
        return [low_list, high_list]


    num_list = [20, 9, 51, 81, 50, 42, 77]

    print(count_low_high(num_list))
  ``` 


## Program Structure -4h

- 4 spaces indentation; can not mix spaces with tabs
- can separate two statements on the same line with a semicolon ; 
- Assignment Statements
  - Walrus Operator (:=) -- allows you to assign a value to a variable and return its value with an expression `n = 10; x = (n := 3 * n) + 1` -- python versions >=3.8
- Conditional Statements -- control structures
  ```python
  if
  if-else
  if-elif-else  # can use \ as line continuation character
  output_value_1 if condition else output_value_2 # conditional expression

  ----------------------------------------------------------------

    if price >= 300:
        price *= 0.7  # (1 - 0.3)
    elif price >= 200:
        price *= 0.8  # (1 - 0.2)
    elif price >= 100:
        price *= 0.9  # (1 - 0.1)
    elif price < 100 and price >= 0:
        price *= 0.95  # (1 - 0.05)
  ```
- Loops - While, For
  - iterator is a variable that goes through the sequence
  - `for num in float_lists: num = 10; # here num is an iterator and is a copy. So doesn't modify original values`
  - `break`
  - `continue`
  -  `pass`
  -  balanced paranthesis 
        ```python 
        def check_balance(brackets):
        check = 0
        for bracket in brackets:
            if bracket == '[':
                check += 1

            elif bracket == ']':
                check -= 1

            if check < 0:
                break

        return check == 0
        ```
  - a sum of zero
    ```python
    def check_sum(num_list):
    for first_num in range(len(num_list)):
        for second_num in range(first_num, len(num_list)):
            if num_list[first_num] + num_list[second_num] == 0:
                return True
    return False


    ----------------------------------------------------------------

    def fib(n):
    first = 0
    second = 1

    if n < 1:
        return -1

    if n == 1:
        return first

    if n == 2:
        return second

    count = 3
    while count <= n:
        fib_n = first + second
        first = second
        second = fib_n
        count += 1
    return fib_n
    ```

## Functions -4h

- function -- reusable set of operations; reusability and simplicity
- `min(); max()`
- built-in functions or user-defined functions
- `def function_name( params ):  pass ;`
- actual values/variables passed into parameters are known as arguments
- positional arguments `min(a, b)`
- keyword arguments `min(first = a, second = b)`
- `min(a = 1, b = 2)` -- default arguments
- `def many(*args, **kwargs)` -- args is tuple, kwargs is dictionary
- functions scope is functions body
- methods -- functions that are properties of a particular entity
- String functions
  - `a_string.find(substring, start, end)` -- returns -1 if substring is not found; index of first occurrence if found
  - `a_string.replace(substring_to_be_replaced, new_string)` -- original string is not altered. new string is returned.
  - `a_string.upper()` -- original string is not altered
  - `a_string.lower()` -- original string is not altered
  - `', '.join(list1)` -- a, b, c -- joins strings with comma and space
  - `string1 = "Learn Python {version} at {cname}".format(version = 3, cname = "Educative")`
  - `string2 = "Learn Python {0} at {1}".format(3, "Educative")`
  - `string3 = "Learn Python {} at {}".format(3, "Educative")`
- Type conversions
  - `int()`
  - `ord()` -- char to unicode value
  - `float()`
  - `str()`
  - `bool()`
  - `comlex()`
  - `hex()`
- `input('prompt or message for the user')` -- stored as string
- lambda -- an anonymous function that returns some form of data; cannot have multiline expression
- `lambda parameters : expression` -- parameters are separated by commas, expression is an operation that returns something.
- `triple = lambda num : num * 3  # Assigning the lambda to a variable`
- `concat_strings = lambda a, b, c: a[0] + b[0] + c[0]`
- `my_func = lambda num: "High" if num > 50` -- throws error. if-else pair is necessary when using conditional statements in lambdas
- functions as arguments
  - `calculator(operation, n1, n2): return operation(n1, n2); calculator(lambda n1, n2 : n1 * n2, 10, 20)`
  - `map(function, list)` -- function will be applied or mapped to all elements of list
  - `double_list = map(lambda n : n * 2, num_list)` -- creates a map object which can be converted into a list
  - `filter(condition_function, list)` -- filters elements if elements satisfy condition specified by `condition_function
  - `list(filter(lambda n : n > 2, num_list))`
- Recursion: function calls itself during its execution
  ```python
    def rec_count(number):
        print(number)
        # Base case
        if number == 0:
            return 0
        rec_count(number - 1)  # A recursive call with a different argument
        print(number)


    rec_count(5)

    ----------------------------------------------------------------

    def fib(n):
        # The base cases
        if n <= 1:  # First number in the sequence
            return 0
        elif n == 2:  # Second number in the sequence
            return 1
        else:
            # Recursive call
            return fib(n - 1) + fib(n - 2)


    print(fib(6))

    ------------------------------------------------------------------

    def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    if n < 0:
        return -1
    # Recursive call
    return n * factorial(n - 1)

  ```
  - makes life easy to solve graphs and trees; Important in search algorithms

- Scopes 
  - Local scope
    ```python 
    # UnboundLocalError: local variable 'x' referenced before assignment
    def my_func(a, b):
        print(x)
        x = 5
        print(x)

    if __name__ == '__main__':
        x = 10
        my_func(1, 2)
        print(x)
    ```
  - Global scope
    ```python
    def my_func(a, b):
        global c
        # swap a and b
        b, a = a, b
        d = 'Mike'
        print(a, b, c, d)

    a, b, c, d = 1, 2, 'c is global', 4
    my_func(1, 2)
    print(a, b, c, d)
    ```
  - Nonlocal scope 
    ```python
    # PEP 3104
    # This type of function is called as closure. A closure is bascically a block of code that closes nonlocal variables. We can reference variables that are defined outside of our function.
    def counter():
        num = 0
        def incrementer():
            nonlocal num
            num += 1
            return num
        return incrementer
    c = counter()

    print (c)


    print (c())


    print (c())


    print (c())
    ```
  - nonlocal will allow us to assign to variables in an outerscope but not in global scope.


print(string1)
print(string2)
print(string3)

## Modules -3h

- module - a python file imported into another python file. 
  ```python
  mymodule.py ---------------------------------------------------------
  def test():
    print("Hello, ASH!")
  
  test() ## will be run when this module is imported even without calling

  main.py -------------------------------------------------------------

  import mymodule # this import causes to execute test() 

  ```
- popular modules `math`, `csv`, `sys`, `os`, `urllib`
- package contains one or more modules
- to create a package, we make a directory with the same name as the package and create empty `__init__.py` inside the directory. 
- `import package.module.function` or `from package.module import function`
- `import os`
  - `os.getcwd()`
  - `os.chdir(some_path)`
  - `os.listdir(path= ".")` -- list containing names of entries in directory `"."` 
  - `os.mkdir(some_path, mode=0o777, dir_fd = None)` -- mode -- unix style three-digit octal code. Three bits of each digit specify read, write, and execute permissions for owner, group, and world
  - `os.remove(path_to_file, dir_fd = None)` -- removes single file
  - `os.rmdir(path_to_dir, dir_fd = None)` -- removes empty directory
  - `os.rename(src, dst)` -- rename file or directory
  - `os.walk(top, topdown=True, onerror=None, followlinks=False)` -- generate file names in directory tree by walking the tree either top-down or bottom-up. For each directory rooted at the top directory (including `top`) it yields a 3-tuple `(dirpath, dirnames, filenames)`
    - say something like `("root", [dir_name for dir_name in root_dir], [file_name for file_name in root])`
    - `('root', [dir_names], [file_names])`
- `import statistics` 
  - `mean(data)`
  - `median(data)` -- middle value in sorted data. m0 -- or ( m1 + m2 ) / 2
  - `mode(data)` -- occurs most often in data ( if tie -- first such number)
  - `stdev(data)` -- sample standard deviation
  - `variance(data)` -- sample variance
  - `from statistics import *; a = [1, 2, 3, 4, 5, 5, 78]; print(f"{stdev(a)=:6.23f}, {variance(a)=:6.2f}")`
  - `nd = statistics.NormalDist(); print(nd)` -- NormalDist(mu=0.0, sigma=1.0) 
- `import math`; use `cmath` to get all math methods for complex numbers
  - `math.factorial(5)` -- 120
  - `math.gcd(300, 90)` -- 30
  - `math.log(10, 100)` -- 0.5 -- log 10 to the base 100
- `import heapq` -- allows us to create heap data structure. heap is a binary tree which always stores a special value at the top(root). minheap (created by default )stores smallest value and maxheap stores largest value; `pop()` method returns value at top
  - `import heapq; heap = []; heapq.headpush(heap, 39); heapq.headpush(heap, 12); print(heapq.headpop(heap))` -- 12
- `import random` 
  - `random.random()` -- random floating point numbers between 0 and 1
  - 

## Object Oriented Programming -3h

## Exceptional handling -1h

## Functional Programming -6h

## Persistence and Databases -1h

## Threads and Concurrency -5h


# ZTM Python

<details open>
    <summary> Python </summary>

## Contents
1. Python Basics
2. Python Basics 2
3. Developer Environment
4. Advanced Python
5. Careers
6. Scripting
7. Data Scraping
8. Automation
9. Web Development
10. Data Science + Artificial Intelligence


## Python Basics
- Programming Language : Set of instructions
- Translator : Interpreter (line by line) | Compiler (all at once)
- Python as a language : Specification
- Python as a implementation : CPython, Jython, PyPy, IronPython
- Python -> Interpreted -> Bytecode -> CPython VM -> Machine
- REPL : Read Evaluate Print Loop
- `repl.it` | `glot.io` -- Online Python Interpreter
- > Guido Van Rossum -- 1991 -- Monty Python -- Britis Comedy Show
- [py3readiness]
- Every programming language has its own pros and cons


## Advanced Python : Object Oriented Programming
- Everything in Python is Object
- `type()`
- `NoneType, int, bool, float, str, list, tuple, dict`
- OOP is a paradigm, a way to structure our code around real world objects
- Assembly Language -- Low Level Language
- Procedural Code -- Top to Bottom Line, Do this and Do that
- OOP -- Model our code in a way that it represents real world objects. Blueprints. 
- > Class Names are CamelCase -- Standard
- Class is a blueprint. Class can be instantiated to create instances | objects. 
- Dunder methods | Magic Methods `__init__` -- constructor method
- DRY -- Do Not Repeat Yourself
- `help(list)`
- Test your assumptions -- don't just believe what someone says
- 4 Pillars of OOP 
  - Encapsulation -- binding of data and functions that manipulate data; functions/methods and attributes
  - Abstraction -- hiding information and giving access to only what is necessary; everything else is hidden
    - Private vs Public
      -  There is no true privacy. 
      -  We sort of agree that variables that start with _ are private. But it doesn't give any special powers. It is accessible as all other variables. It's just a convention we use to say that this is a private variable
   -  Inheritance -- allows new objects to take on properties of exisiting objects
       -  Parent Class and Child Class (Sub Classes | Derived Class)
        -   ```python 
            class Parent:
                pass
            
            class Child(Parent): # Child inherits from Parent
                pass

            instanceVariableName = Child()
            ```
      - `isinstance(instanceVariableName, Child)`
      - `isinstance(instanceVariableName, Parent)`
      - `isinstance(instanceVariableName, object)`

    - Polymorphism -- Many Forms
- Introspection -- ability to determine type of object at runtime
  - `dir(instanceVariableName)` -- gives all the variables and methods of the instance variable; what it has access to
- Dunder Methods | Magic Methods
  - `__str__(self)` --- str(object)
  - `__len__(self)` --- len(object)
  - `__del__(self)` --- del object 
  - `__call__(self)` --- instanceVariableName() 
  - `__getitem__(self, key)` --- instanceVariableName[key]
- `issubclass(list, object)` --- is list a subclass of object
- Multiple Inheritance -- allowed in Python
- MRO -- Method Resolution Order -- in the order they appear
  - This algorithm uses depth first search
  - [MRO Blog](http://www.srikanthtechnologies.com/blog/python/mro.aspx)
  
    ```python
    class A():
        num = 39
    
    class B(A):
        pass

    class C(A):
        num = 12

    class D(B, C):
        pass
    
    print(D.num) # prints 12 ; Checks D, B, C, A 
    print(D.mro()) # shows the order in which it checks
    print(D.__mro__) # same as above
    ```
  - 

```python
class PlayerCharacter:
    membership = True # CLass Object Attribute; This is not dynamic, static; Doesn't change across instances

    # can be accessed by self.membership | PlayerCharacter.membership
    def __init__(self, name = 'anonymous', age = 0):
        if age > 18:
            self.name = name
            self.age = age

    def run(self):
        print('run')
        return 'done' # by default returns None

    @classmethod # this is a decorator
    def add_things(cls, num1, num2): # cls refers to class, similar to self
        return cls('Teddy', num1 + num2)
        return num1 + num2

    @staticmethod
    def add_things2(num1, num2): # we do not have access to cls
        return num1 + num2 

player1 = PlayerCharacter('Cindy', 33)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1.attack) # throws error
print(player2.attack) # prints 50

player1.add_things(2,3) # retunrs  5
PlayerCharacter.add_things(2,3) # retunrs 5

player3 = PlayerCharacter.add_things(2,3) # returns instance


```

```python
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

#Answers:
# 1 Instantiate the Cat object with 3 cats.
cat1 = Cat('cat1', 5)
cat2 = Cat('Cat2', 7)
cat3 = Cat('Cat3', 3)


# 2 Create a function that finds the oldest cat.
def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')
```

```python
class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


#1 Add another Cat

class Tikachu(Cat):
    def sing(self,sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = []
cat1 = Simon('Simon', 10)
cat2 = Sally('Sally', 15)
cat3 = Tikachu('Tikachu', 5)

my_cats.append(cat1)
my_cats.append(cat2)
my_cats.append(cat3)

#OR my_cats = [Simon('Simon', 10), Sally('Sally', 15), Tikachu('Tikachu', 5)]

#3 Instantiate the Pet class with all your cats use variable my_pets

my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance

my_pets.walk()

```

```python
class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email) # super().__init__(email) -- no need to pass self with super() -- this refers to parent class
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
```

```python
#By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class. 
class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
        'name':'Yoyo',
        'has_pets': False,
    }

  def __str__(self):
    return f"{self.color}"

  def __len__(self):
    return 5

  def __del__(self):
    return "deleted"

  def __call__(self):
      return('yes??')

  def __getitem__(self,i):
      return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
```

```python
# Exercise Extending List

class SuperList(list):

    def __len__(self):
        return 1000


super_list1 = SuperList()
print(len(super_list1))

super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))
print(issubclass(list, object))

```

```python
class User():
    def sign_in(self):
        print('signed_in')
    
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print('ran really fast')

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)
```


## Advanced Python : Functional Programming

- Functional Programming -- all about seperation of concerns -- each part concerns itself with one thing that its good at
- Separate data and functions / behavior 
- Goals
  - Clear and Understandable
  - Easy to Extend
  - Easy to Maintain
  - Memory Efficient
  - DRY
- Pure Functions -- less buggy code; more of a guideline
  - rule1 : given same input, will result in same output
  - rule2 : a function should not produce a side effect; does/should not interact with the outside world
- map, filter, zip, reduce
- `map(action, data_we_want_to_take_action_upon)` | `map(func, iterable)`
- `filter(func, iterable)` 
- `zip(iterable1, iterable2, ....)` --> gives you tupes. say `zip(a, b, c)` --> (a1, b1, c1), (a2, b2, c2) .... (am, bm, cm) where m = min(lengths of a, b, c)
- `reduce(func, sequence, init_value)` --- `from functools import reduce`
- Lambda expressions -- one time anonymous functions
  - `lambda param : param * 2`
- 


```python 
from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(string):
    return string.upper()

print(list(map(capitalize, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def is_smart_student(score):
    return score > 50

print(list(filter(is_smart_student, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))
```

```python 
# Square
my_list = [5, 4, 3]

print(list(map(lambda item: item*item, my_list)))

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -2)]

a.sort(key=lambda x: x[1])
print(a)

```

```python

```


</details>


# Python

## Basics

## Dev Env, OOPS, Functional Programming

- NoneType, bool, int, float, str, list, tuple, dict

#### OOP

- paradigm
- class -- blueprint : attributes, properties, methods
- instances -- classes are used to instantiate objects 

```python
class PlayerCharacter:
    def __init__(self, name):
        

```


<br/><br/>


- [Objects Repl](https://replit.com/@aneagoie/Python-Objects#main.py)
- [Course Exercises](https://github.com/aneagoie/ztm-python-course-exercises)
- [History of Programming Languages](https://en.wikipedia.org/wiki/History_of_programming_languages)
- [Objects 1](https://replit.com/@aneagoie/Python-Objects-1)



## Decorators, Error Handling

## Generators

## Modules, Debugging, File IO 

## Reg Exp, Testing

## Scripting, Scraping

## Web Dev

## Automation

## ML, DS

----------------------------------------------------------------

# Data Camp : Data Analyst with Python

## Intro to Python


## Intermediate Python

- plt.plot(x, y)
- plt.scatter(x, y)
- plt.xscale('log')
- 

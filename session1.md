---
marp: true
theme: gaia
class: |
    - invert

math: mathjax
size: 16:9
footer: "Session 1: CPU 5006 Welcome and Overview 25-26"
paginate: true



---
<!-- _class: lead -->
![bg](https://ichef.bbci.co.uk/news/1024/cpsprodpb/14202/production/_108243428_gettyimages-871148930.jpg)

<span style="color:white; text-shadow: black 1px 2px 10px">

# CPU5006-20: Artificial Intelligence

## Session 1: CPU 5006 Welcome and Overview 25-26
</span>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500&display=swap');

:root {
    font-family: 'Roboto', sans-serif;
    color: white;
    background-color: black;
    background-size: 100%;
}
</style>

<!-- _footer: "![]()" -->

---

## Course Overview

<style scoped>
table {
    height: 15%;
    width: 100%;
    font-size: 20px;
}
th {
    color: black;
}
</style>

<!-- _footer: "![]()" -->

Week | Session | |
-----|------|---|
1 | Welcome Session & Intro to Python |
2 | The history of AI & Conducting Liturature Review |
3 | Rule-Based AI Systems |
4 | S1 Assessment Workshop |
5 | Supervised Learning |
RW | Reading Week |
6 | Unsupervised Learning |  S1
7 | Artificial Neural Networks |  
8 | Convolutional NN & Computer Vision |
9 | Recurrent NN & NLP |
10 | S2 Assessment Workshop |
WB | Winter Break |
11 | Generative AI | S2
12 | Building AI Agents |

---

# Overview

- Overview of the Module
- Expectations of you
- Introduction to Python
<!-- - History of AI
- Introduction to scientific writing using LaTex -->

---

# Assignment Deadlines

- S1: Week 6 - $4^{th}$ November 2025
- S2: Week 11 - $13^{th}$ January 2026

---

# Resources Required

- VS Code
- Python
- GitHub Desktop

<style>
    img[alt~="bottom-left"] {
    position: absolute;
    bottom: 50px;
    left: 75px;
    }

    img[alt~="bottom-centre"] {
    position: absolute;
    bottom: 50px;
    left: 520px;
    width: 200px;
    }

    img[alt~="bottom-right"] {
    position: absolute;
    bottom: 50px;
    right: 75px;
    width: 250px
    }
</style>

![bottom-left](image-5.png)
![bottom-centre](image-6.png)
![bottom-right](image-7.png)

---

# Expectations

- Be professional
- Be respectful
- Be inquisitive

---


# Be Curious

- We’re not going to cover every detail of every area of AI (that would be death by PowerPoint!)
- So, it comes down to you to learn new things! We don’t really mind.
- what, so follow your interest!
- We’ll gloss over some things in class – maybe there’s more to uncover?..

---

# Be Diligant

- We learn by doing – so you’ve got to be self-motivated to do it!
- Use independent study time to learn new things and/or consolidate things covered in class.
- Independent Study ≠ Studying Alone

---

# Not a course on how to Code in Python
<style>
img[alt~="right-side"] {
    position: absolute;
    top: 110px;
    right: 5px;
    width: 600px
    }
</style>

- 3 optional Workshops are available:
    1) Date
    2) Date
    3) Date

![right-side](ghost_python.png)

---

# History of Python

<span style="font-size: 0.6em;">

<ul>
    <li> <b>Origins</b>: Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands.</li>
    <li> <b>Early Development</b>: In February 1991, Guido van Rossum published the code (labeled version 0.9.0) to alt.sources.</li>
    <li> <b>Python 2.0 Release</b>: Python 2.0 was released on October 16, 2000, with many major new features.</li>
    <li> <b>Python 3.0 Release</b>: Python 3.0, a major, backwards-incompatible release, was released on December 3, 2008.</li>
    <li> <b>Python’s Philosophy</b>: The philosophy of Python is summarized in “The Zen of Python,” which states the 19 guiding principles for writing computer programs that have influenced the design of the Python language. </li>
<ul>

</span>

![bg right:40% 80%](image-13.png)

---

# Why Python?

- Simplicity and Readability
- Extensive Libraries and Frameworks
- Dynamic Nature
- Platform Indipendance
- Community Support
- Readability

---

# 🧪 Using Jupyter in VS Code

- Install the **Python** and **Jupyter** extensions from the VS Code marketplace.
- Open or create a `.ipynb` file to start coding interactively.
- Use **Markdown**, **code cells**, and **interactive outputs**.
- Great for **data science**, **machine learning**, and **exploratory analysis**.

---

![bg](1.png)

---

![bg](2.png)

---

![bg](3.png)

---

![bg](4.png)

---

![bg](5.png)

---

![bg](6.png)

---

# Python Syntax



```python
name = "Andy"

if name == "Andy":
    print("Hello Class!")
else:
    print("Wrong lecturer")

for i in range(10, 0, -1):
    print(i)

print("BLAST OFF!")
```

![bg right:40% 80%](image-12.png)


---

# Important Notes

![bg right:20% 80%](image-11.png)

<span style="font-size: 0.9em">

- Python is case sensitive
    - Code will not work without correct case

- “Text” values need to be in “” double quotations
    - Numbers do not

- Variables cannot be any Python reserved keywords
    - Print, input, etc

- Files cannot be saved using Python reserved keywords
</span>

---

# Variables and Data Types

A variable is a value that can change, depending on conditions or on information passed to the program.

<style>

img[alt~="bottom-centre2"] {
  position: absolute;
  bottom: 150px;
  left: 450px;
  width: 450px;
  margin: auto;
}
</style>

![bottom-centre2](image-8.png)

---

# Variables and Data Types

<style>
    pre {
    background-color: lightgray;
    border: none;
    border-radius: 20px;
    box-shadow:  13px 13px 31px #595b5cff,
             -13px -13px 31px #4c4e50ff;
    min-height: 20px;
    /* text-align: center; */
    padding-left: 30px;
}

.hljs-comment,
.hljs-quote {
  color: #2b50b0ff;
}

.hljs-variable,
.hljs-template-variable,
.hljs-tag,
.hljs-name,
.hljs-selector-id,
.hljs-selector-class,
.hljs-regexp,
.hljs-deletion {
  color: #fa2230ff;
}

.hljs-number,
.hljs-built_in,
.hljs-builtin-name,
.hljs-literal,
.hljs-type,
.hljs-params,
.hljs-meta,
.hljs-link {
  color: #fc7d06ff;
}

.hljs-attribute {
  color: #f4c60eff;
}

.hljs-string,
.hljs-symbol,
.hljs-bullet,
.hljs-addition {
  color: #28ab00ff;
}

.hljs-title,
.hljs-section {
  color: #358cf7ff;
}

.hljs-keyword,
.hljs-selector-tag {
  color: #ce5bfeff;
}

.hljs {
  display: block;
  overflow-x: auto;
  background: #002451;
  color: white;
  padding: 0.5em;
}

.hljs-emphasis {
  font-style: italic;
}

.hljs-strong {
  font-weight: bold;
}

</style>

```python 
my_variable = Value
```

How we handle that value depends on the data type that we want to use.



---

# Variables and Data Types

- Strings

```python 
"Hello class"
```

- Integers 

```python
1, 2, 3, ...
```


---
# Variables and Data Types

- Float 

```python
1.0, 1.1, 1.3, ...
```

- Boolean

```python
True or False
```

---

# Basic Operators

- \+ - Addition
- \- - Subtraction
- / - Divide
- // - Interger Divide
- % - Modulus
- ** - Power of

---

# Task (20 Mins)

- On Ultra there are Variables and Operator tasks to complete.

<!-- 

See worksheet: python_datatypes_worksheet

-->

---

# Data Structures - Lists

- creating

```python
my_list = [1, 2, 3, 4, 5]
```

```python
my_list = [1, "2", 3, "4", 5]
```

```python
my_2d_list = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]
```

---

# Data Structures - Lists

Indexing 1D lists:

```python
my_list[0]
```
```python
my_list[3]
```

Indexing 2D lists:
```python
my_list[0][1]
```

---

# Data Structures - Lists
<!-- - methods -->

<style scoped>
table {
    height: 15%;
    width: 100%;
    font-size: 20px;
}
th {
    color: black;
}
</style>

| Method Name | Description |
| --- | --- |
| append() | Adds an element at the end of the list |
| clear()  | Removes all the elements from the list  |
| copy() | Returns a copy of the list |
| count() | Returns the number of elements with the specified value |
| extend() | Add the elements of a list (or any iterable), to the end of the current list |
| index() | Returns the index of the first element with the specified value |
| insert() | Adds an element at the specified position |
| pop() | Removes the element at the specified position |
| remove() | Removes the first item with the specified value |
| reverse() | Reverses the order of the list |
| sort() | Sorts the list |

</span>

---

# Data Structures - Tuples

```python
my_tuple = (1, 2, 3, 4)
```

```python
my_tuple_be_careful = (1, 2, 3, 4, [])
```

---

# Data Structures - Dictionaries

```python
my_dict = {
    "name": "Andy",
    "age": 36,
    "Position": "Lecturer"
    "Subjects": [
        "AI",
        "Innovation Labs",
        "Web Dev I"
    ] 
}
```

---

# Data Structures - Dictionaries

- Key-value pairs

```python
my_dict["name"]

>>> "Andy"
```

```python
my_dict["subjects"][0]

>>> "AI"
```

---

## Data Structures - Dictionaries

<style scoped>
table {
    height: 15%;
    width: 100%;
    font-size: 20px;
}
th {
    color: black;
}
</style>

<!-- - methods -->

| Method Name | Description |
| --- | --- |
| clear()| Removes all the elements from the dictionary |
| copy() | Returns a copy of the dictionary |
| fromkeys() | Returns a dictionary with the specified keys and value|
| get() | Returns the value of the specified key|
| items()| Returns a list containing a tuple for each key value pair|
| keys()| Returns a list containing the dictionary's keys|
| pop() | Removes the element with the specified key|
| popitem() | Removes the last inserted key-value pair|
| setdefault()| Returns the value of the specified key. If the key does not exist: insert the key, with the specified value|
| update()| Updates the dictionary with the specified key-value pairs|
| values()| Returns a list of all the values in the dictionary|

---

# Task

See ultra task 2 and worksheet: python_data_structures_worksheet.pdf

---

# Control Flow - If

```python
number_1 = 5
number_2 = 10

if number_1 > number_2:
    print(f"number 1: {number_1} is greater than number 2: {number_2}")
```

---

# Control Flow - Else If

```python
number_1 = 5
number_2 = 10

if number_1 > number_2:
    print(f"number 1: {number_1} is greater than number 2: {number_2}")
elif number_1 < number_2:
    print(f"number 1: {number_1} is less than number 2: {number_2}")
```

---

# Control Flow - Else

```python
number_1 = 5
number_2 = 5

if number_1 > number_2:
    print(f"number 1: {number_1} is greater than number 2: {number_2}")
elif number_1 < number_2:
    print(f"number 1: {number_1} is less than number 2: {number_2}")
else:
    print(f"number 1 and number 2 are both the same")
```

---

# Control Flow - Case

```python
lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")
    case "Python":
        print("You can become a Data Scientist")
    case "PHP":
        print("You can become a backend developer")
    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")
```

---

# Control Flow - For

```python
for i in range(10):
    print(f"i = {i}")
```

---

# Control Flow - While

```python
i = 0

while i < 10:
    print(f"i = {i}")
    i += 1
```

---

# Functions

- Defining and calling them

```python
def function_name():
    ...

function_name()
```

---

# Functions with Parameters

- arguments and return values

```python
def function_name(params1, params2):
    ...
    return output

function_name(1, 2)
```

---

# Task

Worksheet python_control_flow_worksheet.pdf

---

# Comprehensions

- list
- dict

---

# Comprehensions - List

```python
my_list = [i for i in range(10)]
```

---

# Comprehensions - Dictionary

```python
details = [
    ["Andy", 36, "Lecturer"],
    ["Ed", 21, "Lecturer"],
    ["Dave", 22, "Senior Lecturer"],
]

my_dict = {id: values for id, values in enumerate(details)}
```

---

# Python Libraries

<span style="font-size: 0.6em;">

Python libraries are collections of modules that offer a wide range of functionalities. They simplify complex tasks by providing a set of pre-written functions that can be used in the development process.

![bg right:50% 90%](image-14.png)

<!-- <span style="font-size: 0.75em;"> -->
<ul style="padding-left: 7.5%">
    <li>Numpy</li>
    <li>Pandas</li>
    <li>SciPy</li>
    <li>Matplotlin</li>
    <li>Scikit-Learn</li>
    <li>Seaborn</li>
    <li>TensorFlow/PyTorch</li>
</ul>
</span>

<!-- _footer: "Access to the [PyPI](https://pypi.org/)" -->


---

# Importing Libraries

``` python
import pandas as pd
from x import y
```

``` python
df = pd.dataframe()
```

---

# PIP

![bg right:30% 90%](image-15.png)


<span style="font-size:0.7em">
<ul>
    <li>pip is the standard package manager for Python. </li>
    <li>It allows you to install and manage additional packages that are not part of the Python standard library. </li>
    <li>The name pip is a recursive acronym for 'Pip Installs Packages’.</li>
    <li>pip is a package-management system written in Python and is used to install and manage software packages. </li>
    <li>The Python Software Foundation recommends using pip for installing Python applications and its dependencies during deployment.</li>
<ul>
</span>

---

# Task

Complete the tasks in the Jupyter Notebook called ``Session2 - Introduction to Python tasks.ipynb``, this can be found on Minerva.

<!-- - String Reversal: Write a function reverse_string(s) that takes a string s as input and returns the reversed string.
 ``` python
def reverse_string(s):
    # Your code here
    pass
``` 

- Fibonacci Sequence: Write a function fibonacci(n) that returns the nth number in the Fibonacci sequence.
<!-- ```python
def fibonacci(n):
    # Your code here
    pass
``` 
- Prime Numbers: Write a function is_prime(n) that takes an integer n as input and returns True if n is a prime number and False otherwise.
<!-- ```python
def is_prime(n):
    # Your code here
    pass

``` 

- Palindrome Check: Write a function is_palindrome(s) that takes a string s as input and returns True if s is a palindrome and False otherwise. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalisation.
<!-- ```python
def is_palindrome(s):
    # Your code here
    pass
``` 

- List Comprehensions: Write a function squares(n) that uses a list comprehension to return a list of the squares of all numbers from 1 to n.
<!-- ```python
def squares(n):
    # Your code here
    pass

``` -->

---

# Next Session

- History of AI
- S1 Introduction
- Introduction to Overleaf
- How to write a liturature Review

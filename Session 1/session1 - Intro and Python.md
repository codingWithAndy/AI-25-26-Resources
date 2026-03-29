---
marp: true
theme: gaia
class: |
    - invert

math: mathjax
size: 16:9
paginate: true

style: |
    /* @theme ai-fun-level5 */

    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Share+Tech+Mono&display=swap');

    :root {
    font-family: 'Roboto', sans-serif;
    color: #f2f7ff;

    /* AI colour palette */
    --bg-dark: #0b1020;
    --bg-mid: #11182e;
    --grid: rgba(0, 224, 255, 0.08);
    --dot: rgba(255, 0, 212, 0.10);
    --text-main: #f2f7ff;
    --text-soft: #c9d4e8;
    --highlight: #00e0ff;
    --highlight-2: #ff00d4;
    --highlight-3: #8aff00;
    --panel: rgba(255, 255, 255, 0.08);
    --panel-strong: rgba(255, 255, 255, 0.12);
    --ai-accent: linear-gradient(90deg, #00e0ff, #7a5cff, #ff00d4);

    background:
        linear-gradient(90deg, var(--grid) 1px, transparent 1px),
        linear-gradient(180deg, var(--grid) 1px, transparent 1px),
        radial-gradient(circle, var(--dot) 1px, transparent 1px),
        radial-gradient(circle at top left, #16213f 0%, var(--bg-dark) 55%, #05070d 100%);
    background-size:
        60px 60px,
        60px 60px,
        28px 28px,
        cover;
    background-position:
        0 0,
        0 0,
        14px 14px,
        center;
    }

    /* Base slide styling */
    section {
    padding: 55px 70px;
    font-size: 30px;
    line-height: 1.35;
    color: var(--text-main);
    position: relative;
    }

    /* Decorative glow strip */
    section::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    height: 8px;
    width: 100%;
    background: var(--ai-accent);
    box-shadow: 0 0 18px rgba(0, 224, 255, 0.45);
    }

    /* Optional subtle badge */
    section::after {
    content: "AI • Level 5";
    position: absolute;
    top: 18px;
    right: 28px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.45em;
    letter-spacing: 0.08em;
    color: rgba(255,255,255,0.55);
    border: 1px solid rgba(255,255,255,0.18);
    padding: 6px 12px;
    border-radius: 999px;
    background: rgba(255,255,255,0.04);
    }

    /* Headings */
    h1, h2, h3 {
    font-family: 'Share Tech Mono', monospace;
    margin-top: 0;
    margin-bottom: 0.45em;
    line-height: 1.1;
    }

    h1 {
    font-size: 1.95em;
    background: var(--ai-accent);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow:
        0 0 12px rgba(0, 224, 255, 0.35),
        0 0 22px rgba(255, 0, 212, 0.18);
    }

    h2 {
    font-size: 1.45em;
    color: #8defff;
    text-shadow: 0 0 10px rgba(0, 224, 255, 0.2);
    }

    h3 {
    font-size: 1.1em;
    color: #ffd6fb;
    }

    /* Lead slides */
    section.lead {
    text-align: center;
    justify-content: center;
    background:
        radial-gradient(circle at centre, rgba(0,224,255,0.08) 0%, rgba(0,0,0,0) 45%),
        radial-gradient(circle at 30% 20%, rgba(255,0,212,0.14) 0%, rgba(0,0,0,0) 30%),
        linear-gradient(135deg, #11182e 0%, #05070d 100%);
    }

    section.lead h1,
    section.lead h2,
    section.lead h3 {
    background: none;
    -webkit-background-clip: initial;
    -webkit-text-fill-color: initial;
    color: white;
    text-shadow: 0 2px 18px rgba(0, 0, 0, 0.7);
    }

    section.lead::after {
    content: "Artificial Intelligence";
    top: auto;
    bottom: 24px;
    right: 24px;
    }

    /* Paragraphs */
    p, li {
    color: var(--text-soft);
    }

    /* Strong text */
    strong {
    color: #ffffff;
    background: linear-gradient(90deg, rgba(0,224,255,0.22), rgba(255,0,212,0.16));
    padding: 0.04em 0.2em;
    border-radius: 6px;
    }

    /* Lists */
    ul, ol {
    font-size: 1em;
    line-height: 1.5;
    padding-left: 1.1em;
    }

    ul li::marker,
    ol li::marker {
    color: var(--highlight);
    font-weight: 700;
    }

    /* Blockquotes / callouts */
    blockquote {
    border-left: 6px solid var(--highlight);
    background: rgba(255,255,255,0.06);
    padding: 18px 22px;
    border-radius: 14px;
    color: #ffffff;
    }

    /* Code */
    code {
    font-family: 'Share Tech Mono', monospace;
    background: rgba(255, 255, 255, 0.08);
    color: #8defff;
    padding: 0.2em 0.4em;
    border-radius: 6px;
    font-size: 0.9em;
    }

    pre {
    font-family: 'Share Tech Mono', monospace;
    background: rgba(10, 15, 28, 0.95);
    color: #8defff;
    border: 1px solid rgba(0, 224, 255, 0.25);
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.35);
    }

    /* Tables */
    table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.75em;
    background: rgba(255,255,255,0.05);
    border-radius: 14px;
    overflow: hidden;
    }

    th {
    background: linear-gradient(90deg, rgba(0,224,255,0.85), rgba(122,92,255,0.85));
    color: #08101f;
    padding: 12px;
    text-align: left;
    }

    td {
    padding: 12px;
    border-top: 1px solid rgba(255,255,255,0.08);
    }

    tr:nth-child(even) td {
    background: rgba(255,255,255,0.03);
    }

    /* Links */
    a {
    color: #8defff;
    text-decoration: none;
    border-bottom: 1px solid rgba(141,239,255,0.4);
    }

    /* Horizontal rule */
    hr {
    border: none;
    height: 2px;
    background: var(--ai-accent);
    opacity: 0.45;
    margin: 24px 0;
    }

    /* Small highlight box */
    .note {
    background: rgba(138, 255, 0, 0.12);
    border-left: 6px solid var(--highlight-3);
    padding: 16px 20px;
    border-radius: 14px;
    }

    /* Image placement helpers */
    img {
    border-radius: 20px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.35);
    }

    img[alt~="right-centre"] {
    position: absolute;
    bottom: 140px;
    right: 70px;
    width: 350px;
    }

    img[alt~="right-centre-pip"] {
    position: absolute;
    bottom: 145px;
    right: 75px;
    width: 320px;
    }

    img[alt~="right-side"] {
    position: absolute;
    top: 170px;
    right: 10px;
    width: 470px;
    }

    img[alt~="bottom-left"] {
    position: absolute;
    bottom: 40px;
    left: 75px;
    width: 220px;
    }

    img[alt~="bottom-centre"] {
    position: absolute;
    bottom: 40px;
    left: 50%;
    transform: translateX(-50%);
    width: 200px;
    }

    img[alt~="bottom-right"] {
    position: absolute;
    bottom: 40px;
    right: 75px;
    width: 240px;
    }

    img[alt~="right-centre-lib"] {
    position: absolute;
    bottom: 60px;
    right: 90px;
    width: 520px;
    }

    /* Two-column utility */
    .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
    }

    /* Panel/card utility */
    .panel {
    background: var(--panel);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 20px 24px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.22);
    }

    /* Task slides */
    section.task {
    background:
        linear-gradient(135deg, rgba(255,140,0,0.18), rgba(255,0,90,0.18)),
        radial-gradient(circle at top right, rgba(255,255,255,0.08), transparent 30%),
        linear-gradient(135deg, #2b0f0f 0%, #140707 100%);
    color: #fff4e8;
    border: 4px solid #ff8c00;
    }

    section.task::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    height: 10px;
    width: 100%;
    background: linear-gradient(90deg, #ffcc00, #ff8c00, #ff2d55);
    box-shadow: 0 0 22px rgba(255, 140, 0, 0.6);
    }

    section.task::after {
    content: "TASK";
    position: absolute;
    top: 18px;
    right: 24px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.8em;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: #1a0a00;
    background: linear-gradient(90deg, #ffcc00, #ff8c00);
    padding: 8px 16px;
    border-radius: 999px;
    box-shadow: 0 0 18px rgba(255, 140, 0, 0.45);
    }

    section.task h1,
    section.task h2,
    section.task h3 {
    background: none;
    -webkit-background-clip: initial;
    -webkit-text-fill-color: initial;
    color: #ffd6a5;
    text-shadow: 0 0 16px rgba(255, 140, 0, 0.35);
    }

    section.task h1 {
    font-size: 2.1em;
    }

    section.task p,
    section.task li {
    color: #fff4e8;
    font-size: 1.02em;
    }

    section.task strong {
    color: #1a0a00;
    background: linear-gradient(90deg, #ffcc00, #ff8c00);
    padding: 0.08em 0.28em;
    border-radius: 6px;
    }

    section.task code {
    background: rgba(255,255,255,0.1);
    color: #ffd6a5;
    border: 1px solid rgba(255,255,255,0.12);
    }

    section.task ul li::marker,
    section.task ol li::marker {
    color: #ffcc00;
    }

footer: "Session 1: CPU 5006 Welcome and Overview 25-26"

---

<!-- _class: lead -->

# <span style="color:white;"> CPU5006-20: Artificial Intelligence </span>

## Session 1: CPU 5006 Welcome & 
## Overview 25-26

![bg](https://ichef.bbci.co.uk/news/1024/cpsprodpb/14202/production/_108243428_gettyimages-871148930.jpg)

<!-- _footer: "![]()" -->

---

## Course Overview

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
11 | Generative AI | S2
12 | Building AI Agents |

---

## Overview

- Overview of the Module
- Expectations of you
- Introduction to Python

---

## Assignment Deadlines

- S1: Week 6 - $^{th}$ November 2026
- S2: Week 11 - $^{th}$ December 2026

---

## Resources Required

- VS Code
- Python
- GitHub Desktop

![bottom-left](../assets/image-5.png)
![bottom-centre](../assets/image-6.png)
![bottom-right](../assets/image-7.png)

---

## Expectations

- Be professional
- Be respectful
- Be inquisitive

---


## Be Curious

- We’re not going to cover every detail of every area of AI (that would be death by PowerPoint!)
- So, it comes down to you to learn new things! We don’t really mind.
- what, so follow your interest!
- We’ll gloss over some things in class – maybe there’s more to uncover?..

---

## Be Diligant

- We learn by doing – so you’ve got to be self-motivated to do it!
- Use independent study time to learn new things and/or consolidate things covered in class.
- Independent Study ≠ Studying Alone

---

## This module is not a course on how to Code in Python!

- 3 optional Workshops are available:
    1) $X^{nd}$ October 2026
    2) $X^{th}$ October 2026
    3) $X^{th}$ October 2026

Time: 1:30pm - 2:30 pm
Room: TBC

![right-side](../assets/ghost_python.png)

---

#  History of Python

<div style="display: flex; justify-content: space-between;">
<div style="width: 60%;">

<ul style="font-size: 0.6em">
    <li> <b>Origins</b>: Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands.</li>
    <li> <b>Early Development</b>: In February 1991, Guido van Rossum published the code (labeled version 0.9.0) to alt.sources.</li>
    <li> <b>Python 2.0 Release</b>: Python 2.0 was released on October 16, 2000, with many major new features.</li>
    <li> <b>Python 3.0 Release</b>: Python 3.0, a major, backwards-incompatible release, was released on December 3, 2008.</li>
    <li> <b>Python’s Philosophy</b>: The philosophy of Python is summarized in “The Zen of Python,” which states the 19 guiding principles for writing computer programs that have influenced the design of the Python language. </li>
<ul>

</div>
<div style="width: 40%;">

![right-centre](../assets/image-13.png)

</div>
</div>

---

## Why Python?

- Simplicity and Readability
- Extensive Libraries and Frameworks
- Dynamic Nature
- Platform Indipendance
- Community Support
- Readability

---

## 🧪 Using Jupyter in VS Code

- Install the [**Python**](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-python-envs) and [**Jupyter**](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extensions from the VS Code marketplace.
- Open or create a `<filename>.ipynb` file to start coding interactively.
- Within Jupyter you can use: **Markdown**, **code cells**, and **interactive outputs**.
- Great for **data science**, **machine learning**, and **exploratory analysis**.
- When creating for production, create and use a `<filename>.py` file instead of a`.ipynb`.

---

![bg](../assets/1.png)

<!-- 
When opening VS Code you should be greeted with this screen. Ensure extensions are installed before continuing at this point.
-->

---

![bg](../assets/2.png)

<!-- 
If students do not do this but create a new file another way. Just ensure that they just give it any name and then use the .ipynb extension and it will save the file as a Jupyter Notebook.
 -->

---

![bg](../assets/3.png)

---

![bg](../assets/4.png)

---

![bg](../assets/5.png)

<!-- 
This list will differ based on the listen of Python Eviroments that are listed on the machine. So don't expect to see exactly the same list. 
If a conda virtual enviroment has been installed, then you will see the base.
 -->
---

![bg](../assets/6.png)

<!-- 
When running for the first time, a pop up box in the bottom left will appear asking to install ipykernel. Accept and install. This is required to run the notebook.
 -->

---

## Python Syntax

<div style="display: flex; justify-content: space-between;">
<div style="width: 60%;">

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
</div>
<div style="width: 40%;">

![right-centre](../assets/image-12.png)
</div>
</div>

<!-- 
Further details will be explained later on, this is a visual representation of example code. 
-->

---

## Important Notes

![bg right:20% 80%](../assets/image-11.png)

<span style="font-size: 0.8em">

- Python is case sensitive
    - Code will not work without correct case

- “Text” values need to be in “” double quotations or '' single quotation
    - Numbers do not

- Variables cannot be any Python reserved keywords
    - Print, input, etc

- Files cannot be saved using Python reserved keywords

</span>

<!-- 
While either quotation can be used, the recommeneded way is using a double.
-->

---

## Variables and Data Types

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

![bottom-centre2](../assets/image-8.png)

---

## Variables and Data Types

```python 
my_variable = Value
```

How we handle that value depends on the data type that we want to use.

---

## Variables and Data Types

- Strings

```python 
"Hello class"
```

- Integers 

```python
1, 2, 3, ...
```


---

## Variables and Data Types

- Float 

```python
1.0, 1.1, 1.3, ...
```

- Boolean

```python
True or False
```

---

## Basic Operators

```python
+  # Addition: sums two values (e.g. 3 + 2 = 5)

-  # Subtraction: difference between two values (e.g. 5 - 2 = 3)

/  # Division: divides and returns a float (e.g. 5 / 2 = 2.5)

// # Integer Division: divides and truncates to an integer (e.g. 5 // 2 = 2)

%  # Modulus: returns the remainder of a division (e.g. 5 % 2 = 1)

** # Exponentiation: raises a number to a power (e.g. 2 ** 3 = 8)
```

---

<!-- _class: task -->

## Task 
<!-- (15 Mins) -->

- On Ultra there are Variables and Operator tasks to complete.
- answer in the Jupyter Notebook provided.
- complete tasks **0-4** in the worksheet `CPU5006_Session1_Introduction_to_Python_Tasks.ipynb`.

### Stretch:
See worksheet: ``python_datatypes_worksheet.pdf``

---

## Data Structures - Lists

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

## Data Structures - Lists

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

## Data Structures - Lists
<!-- - methods -->

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

---

# Data Structures - Tuples

```python
my_tuple = (1, 2, 3, 4)
```

```python
my_tuple_be_careful = (1, 2, 3, 4, [])
```

---

## Data Structures - Dictionaries

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

## Data Structures - Dictionaries

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

<!-- _class: task -->

## Task

- complete tasks **5-7** in the worksheet `CPU5006_Session1_Introduction_to_Python_Tasks.ipynb`.

### Stretch:
worksheet: ``python_data_structures_worksheet.pdf``

---

## Control Flow - If

```python
number_1 = 5
number_2 = 10

if number_1 > number_2:
    print(f"number 1: {number_1} is greater than number 2: {number_2}")
```

---

## Control Flow - Else If

```python
number_1 = 5
number_2 = 10

if number_1 > number_2:
    print(f"number 1: {number_1} is greater than number 2: {number_2}")
elif number_1 < number_2:
    print(f"number 1: {number_1} is less than number 2: {number_2}")
```

---

## Control Flow - Else

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

## Control Flow - Case

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

## Control Flow - For

```python
for i in range(10):
    print(f"i = {i}")
```

---

## Control Flow - While

```python
i = 0

while i < 10:
    print(f"i = {i}")
    i += 1
```

---

## Functions

- Defining and calling them

```python
def function_name():
    ...

function_name()
```

---

## Functions with Parameters

- arguments and return values

```python
def function_name(params1, params2):
    ...
    return output

function_name(1, 2)
```

---

<!-- _class: task -->

## Task

- complete tasks **8-13** in the worksheet `CPU5006_Session1_Introduction_to_Python_Tasks.ipynb`.

### Stretch:
Worksheet ``python_control_flow_worksheet.pdf``

---

## Comprehensions

- list
- dict

---

## Comprehensions - List

```python
my_list = [i for i in range(10)]
```

---

## Comprehensions - Dictionary

```python
details = [
    ["Andy", 36, "Senior Lecturer"],
    ["Ed", 21, "Lecturer"],
    ["Dave", 22, "Senior Lecturer"],
]

my_dict = {id: values for id, values in enumerate(details)}
```

---

## Python Libraries

<span style="font-size: 0.6em;">

Python libraries are collections of modules that offer a wide range of functionalities. They simplify complex tasks by providing a set of pre-written functions that can be used in the development process.


<div style="display: flex; justify-content: space-between;">
<div style="width: 60%;">

- Numpy
- Pandas
- SciPy
- Matplotlin
- Scikit-Learn
- Seaborn
- TensorFlow/PyTorch

</span>

</div>
<div style="width: 40%;">

![right-centre-lib](../assets/image-14.png)

</div>
</div>

<!-- _footer: "Access to the [PyPI](https://pypi.org/)" -->

---

## Importing Libraries

``` python
import pandas as pd
from x import y
```

``` python
df = pd.dataframe()
```

---

## PIP

<style scoped>

</style>

<div style="display: flex; justify-content: space-between;">
<div style="width: 60%;">

<span style="font-size:0.65em">
<ul>
    <li>pip is the standard package manager for Python. </li>
    <li>It allows you to install and manage additional packages that are not part of the Python standard library. </li>
    <li>The name pip is a recursive acronym for 'Pip Installs Packages’.</li>
    <li>pip is a package-management system written in Python and is used to install and manage software packages. </li>
    <li>The Python Software Foundation recommends using pip for installing Python applications and its dependencies during deployment.</li>
<ul>
</span>

</div>
<div style="width: 40%;">

![right-centre-pip](../assets/image-15.png)

</div>
</div>

---

<!-- _class: task -->

## Task

- complete tasks remaining tasks in the worksheet `CPU5006_Session1_Introduction_to_Python_Tasks.ipynb`.

### Stretch:
worksheet: ``python_datatypes_worksheet.pdf``
worksheet: ``python_control_flow_worksheet.pdf``
worksheet: ``python_data_structures_worksheet.pdf``

---

## Next Session

- History of AI
- S1 Introduction
- Introduction to Overleaf
- How to write a liturature Review

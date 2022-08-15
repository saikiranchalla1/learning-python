# Python Programming
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Python Programming](#python-programming)
  - [Course Overview and Installs](#course-overview-and-installs)
    - [Python 2 vs Python 3](#python-2-vs-python-3)
    - [Python Overview](#python-overview)
    - [Command Line Crash Course](#command-line-crash-course)
      - [Windows Command Line](#windows-command-line)
      - [macOS Command Line](#macos-command-line)
    - [Installing Python](#installing-python)
    - [Test driving Anaconda](#test-driving-anaconda)
    - [Running Python Code](#running-python-code)
  - [Python Object and Data Structure Basics](#python-object-and-data-structure-basics)
    - [Basic Data Types](#basic-data-types)
    - [Numbers](#numbers)
      - [Numbers - FAQ](#numbers---faq)
    - [Variable Assignments](#variable-assignments)
    - [Strings](#strings)
      - [String Formatting for Printing](#string-formatting-for-printing)
      - [Strings FAQ](#strings-faq)
      - [Print Formatting FAQS](#print-formatting-faqs)
    - [Lists](#lists)
    - [Dictionaries](#dictionaries)
    - [Tuples](#tuples)
    - [Sets](#sets)
    - [Booleans](#booleans)
    - [Files](#files)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->



## Course Overview and Installations

### Python 2 vs Python 3

- Choosing between Python 2 vs 3 used to be a very difficult decision for
  newcomers to the Python programming language.
- Many companies still had legacy Python 2 code to be maintained.
- Now every major external python package has been updated to support Python 3!
- Python 3 is the future of Python.
- We use Python 3 for this course.
- Old notebooks are available in case you need Python 2 information.
- Let’s get started by installing Python 3!

### Python Overview

- Brief History of Python
  - Created in 1990 by Guido van Rossum
  - Python 3 released in 2008
  - Specifically designed as an easy to use language
  - High focus on readability of code

- Why Choose Python?
  - Designed for clear, logical code that is easy to read and learn.
- Lots of existing libraries and frameworks written in Python allowing users to
  apply Python to a wide variety of tasks.
  - Focuses on optimizing developer time, rather than a computer’s processing
    time.
  - Great documentation online: [here](docs.python.org/3)

- What can you do with Python?
  - Automate simple tasks
  - Searching for files and editing them
  - Scraping information from a website
  - Reading and editing excel files
  - Work with PDFs
  - Automate emails and text messages
  - Fill out forms
  - Data Science and Machine Learning
    - Analyze large data files
    - Create visualizations
    - Perform machine learning tasks
    - Create and run predictive algorithms
  - Create websites
    - Use web frameworks such as Django and Flask to handle the backend of a
      website and user data
    - Create interactive dashboards for users

### Command Line Crash Course

- Before we install anything, its important to have a very quick overview of how
  to work at the command line.
- This allows you to programmatically move through your computer’s directories.
- We will cover:
  - Find your current directory
  - Listing all files in a directory
  - How to change directory
  - How to clear the command line screen

#### Windows Command Line

- Search for "cmd" in your search bar to open Command Prompt
- To find the current directory: `cd`
- To list all files in a directory: `dir`
- To change directory i.e. move to a different
  directory: `cd <Name of the directory>` e.g `cd Desktop`
- To clear the command line: `cls`

#### macOS Command Line

- Using the keys `CMD+Space` launch Spotlight and search for `Terminal` and
  launch it.
- To find current directory: `pwd`
- To list all files in a directory: `ls` (or `ls -a` to show all files including
  hidden files)
- To change directory: `cd <Name of the directory>` e.g `cd Desktop`
- To clear the command line: `clear`

__Note: You can use the `tab` key on your keyboard to autocomplete the file
names. After partially typing the file name hit the `tab` key to finish the rest
of the name. This is case insensitive in Windows, where as in Mac this is case
sensitive.__

### Installing Python

- There are many ways to run Python!
- Later on we’ll explore the difference between running a Python .py script or
  running Python code in a notebook environment.
  - Either way, we will still want to install Python!
- Installation Lecture:
  - Install Anaconda Distribution for Python.
  - Anaconda installs Python and an easy to use development environment and
    navigator launch tool.
  - Briefly run Jupyter Notebook.
    - Explore “no install” online options.

- Quick Note:
  - There are now many online “no install” Python environments that can run in
    the browser (as long as you have an internet connection).
  - While not officially part of the course, we will give you a brief tour of
    these online “no install” options at the end.

- To install Python we will use the free Individual Anaconda distribution.
- This distribution includes Python as well as many other useful libraries,
  including Jupyter Notebook environment.
- Anaconda can also easily be installed on to any major OS, Windows, MacOS, or
  Linux.
- Navigate to [Anaconda](https://www.anaconda.com/products/individual) download
  page and look for the `Download` button to download Anaconda.
  __Note: Please download the Graphical installer only__

- Free “No Install” Options:
  - jupyter.org/try
  - Google Collab Online Notebooks
  - Repl.it
- Google Search:
  - “Python Interpreter Online”
- Disadvantages of "No Install" options:
  - Hard to upload your own code,data, or notebooks!
  - May not save your code in the free version!
  - Not officially part of this course or supported by this course!

### Test driving Anaconda

- Launch Anaconda Navigator and click on `Launch` under `Jupyter Notebook` (not
  Jupyter Lab)
  ![img.png](img.png)

- This wll launch Jupyter Notebook editor in your Browser at
  location http://localhost:8888/tree

![img_1.png](img_1.png)

- This shows your directory structure of your user directory. Navigate to the
  desired folder where you'd like to store your Jupyter files and click on
  the `New` dropdown to select `Folder`.
- By default, the folder is created with name `Untitled Folder`. Click on the
  checkbox next to it and click on the `Rename` button to rename it.
  ![img_2.png](img_2.png)
- Now, click on the new folder you've created and from the `New` dropdown,
  select `Python 3` to create and launch a new Jupyter Notebook that uses Python
  3.
- In the cell which starts with `In [ ] :` enter `1 + 1` and click on
  the `Cells` option on the top and select `Run Cells`:
  ![img_3.png](img_3.png)

- You can also use the shortcut `Shift + Enter` to run the cell and create a new
  cell. Try it!
- Once you're done with your practice, you can shutdown the notebook by
  selecting it in the folder view and clicking on the `Shutdown` button. This
  will not delete the notebook.
  ![img_4.png](img_4.png)

### Running Python Code

- There are several ways to run Python code.
- First let’s discuss the various options for development environments
- There are 3 main types of environments:
  - Text Editors
  - Full IDEs
  - Notebook Environments


- Text Editors
  - General editors for any text file
  - Work with a variety of file types
  - Can be customized with plugins and add-ons
  - Keep in mind, most are not designed with only Python in mind.
  - Most popular: Sublime Text and Atom

- Full IDEs
  - Development Environments designed specifically for Python.
  - Larger programs.
  - Only community editions are free.
  - Designed specifically for Python, lots of extra functionality.
  - Most popular: PyCharm and Spyder

- Notebook Environments
  - Great for learning.
  - See input and output next to each other.
  - Support in-line markdown notes, visualizations, videos, and more.
  - Special file formats that are not .py
  - Most popular is Jupyter Notebook.

- Most important note:
  - Development Environments are a personal choice highly dependent on personal
    preference.
  - Choose whichever development environment you prefer!

- Let’s now explore how to run Python code:
  - First with an editor to create a .py script and run the file at your command
    line.
  - Then with a Jupyter Notebook.
  - First let’s download sublime text editor: www.sublimetext.com
  - Open Sublime and create a new folder with the following content:
  ```
    print('hello world!')
  ```
  - Save this file as `myexample.py`
  - Open Command prompt or Terminal and navigate to the folder where you stored
    the above file.
  - Now execute the file using the command `python myexample.py`.
  - You can also launch Python interpreter from command line using the
    command `python`. To quit the interpreter use the command `quit()`.

## Python Object and Data Structure Basics

### Basic Data Types

- In this section of the course we will cover the key data types in Python.
- These are your basic building blocks when constructing larger pieces of code.
- Let’s quickly discuss all of the possible data types, then we’ll have lectures
  that go into more detail about each one!

![img_5.png](img_5.png)

### Numbers

- There are two main number types we will work with:
  - Integers which are whole numbers.
- Floating Point numbers which are numbers with a decimal.
- Let’s explore basic math with Python!
- We will also discuss how to create variables and assign them values.
- Refer to the Notebook
  name: `code/00-Python Object and Data Structure Basics/01-Numbers.ipynb`

#### Numbers - FAQ

1. What's the difference between floating point and an integer? An integer has
   no decimals in it, a floating point number can display digits past the
   decimal point.

2. Why doesn't 0.1+0.2-0.3 equal 0.0 ? This has to do with floating point
   accuracy and computer's abilities to represent numbers in memory. For a full
   breakdown, check out: https://docs.python.org/2/tutorial/floatingpoint.html

### Variable Assignments

- We just saw how to work with numbers, but what do these numbers represent?
- It would be nice to assign these data types a variable name to easily
  reference them later on in our code!
- For example:

```python
  my_dogs = 2
```

- Rules for variable names
  - Names can not start with a number.
  - There can be no spaces in the name, use _ instead.
  - Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
  - It's considered best practice (PEP8) that names are lowercase.
  - Avoid using words that have special meaning in Python like "list" and "str"

- Python uses Dynamic Typing
- This means you can reassign variables to different data types.
- This makes Python very flexible in assigning data types, this is different
  than other languages that are “Statically-Typed”
  ![img_6.png](img_6.png)

- Pros of Dynamic Typing:
  - Very easy to work with
  - Faster development time
- Cons of Dynamic Typing:
  - May result in bugs for unexpected data types!
  - You need to be aware of type()

- Refer to the
  notebook: `code/00-Python Object and Data Structure Basics/01-Variable Assignment.ipynb`

### Strings

- Strings are sequences of characters, using the syntax of either single quotes
  or double quotes:
  - 'hello'
  - "Hello"
  - " I don't do that "

- Because strings are ordered sequences it means we can using indexing and
  slicing to grab sub-sections of the string.
- Indexing notation uses [ ] notation after the string (or variable assigned the
  string).
- Indexing allows you to grab a single character from the string... These
  actions use [ ] square brackets and a number index to indicate positions of
  what you wish to grab.
  - Character :    h e l l o
  - Index :     0 1 2 3 4

- These actions use [ ] square brackets and a number index to indicate positions
  of what you wish to grab.
  - Character :    h e l l o
  - Index :     0 1 2 3 4
  - Reverse Index:    0 -4 -3 -2 -1
- Slicing allows you to grab a subsection of multiple characters, a “slice” of
  the string.
- This has the following syntax: [start:stop:step]
- start is a numerical index for the slice start
- stop is the index you will go up to (but not include)
- step is the size of the “jump” you take.

- Refer to the
  notebook: `code/00-Python Object and Data Structure Basics/02-Strings.ipynb`

#### String Formatting for Printing

- Often you will want to “inject” a variable into your string for printing. For
  example:

```python
my_name = “Jose”
print(“Hello ” + my_name)
```

- There are multiple ways to format strings for printing variables in them.
- This is known as string interpolation.
- Let’s explore two methods for this:
  - `.format()` method
  - `f-strings` (formatted string literals)

- Refer to the
  notebook: `code/00-Python Object and Data Structure Basics/03-Print Formatting with Strings.ipynb`

#### Strings FAQ

1. Are strings mutable? Strings are not mutable! (meaning you can't use indexing
   to change individual elements of a string)

2. How do I create comments in my code? You can use the hashtag # to create
   comments in your code

#### Print Formatting FAQS

1.) I imported print from the __future__ module, now print isn't working. What
happened?

This is because once you import from the __future__ module in Python 2.7, a
print statement will no longer work, and print must then use a print() function.
Meaning that you must use

print('Whatever you were going to print')

or if you are using some formatting:

print('This is a string with an {p}'.format(p='insert'))

The __future__ module allows you to use Python3 functionality in a Python2
environment, but some functionality is overwritten (such as the print statement,
or classic division when you import division).

Since we are using Jupyter Notebooks, once you so the import, all cells will
require the use if the print() function. You will have to restart Python or
start a new notebook to regain the old functionality back.

[HERE](https://pyformat.info/) IS AN AWESOME SOURCE FOR PRINT FORMATTING:

#### Exercises
1. Write a string index that returns just the letter 'r'  from 'Hello World' .

For example, 'Hello World'[0]  returns 'H'

2. Use string slicing to grab the word 'ink'  from inside 'tinker'

For example, 'education'[3:6]  returns 'cat'

Remember that when slicing you only go up to but not including the end index.

3. Write an expression using any of the string formatting methods we have learned (except f-strings, see note below) to return the phrase 'Python rules!'

For example, these phrases both return 'I like apples' :

```
'I like %s' %'apples'
'I like {}'.format('apples')
```



### Lists

- Lists are ordered sequences that can hold a variety of object types.
- They use [] brackets and commas to separate objects in the list.
  - [1,2,3,4,5]
- Lists support indexing and slicing. Lists can be nested and also have a
  variety of useful methods that can be called off of them.

- Refer to the
  notebook: `code/00-Python Object and Data Structure Basics/04-Lists.ipynb`

#### Exercises
1. Create a list that contains at least one string, one integer and one float.

For example:

[1, 'two', 3.14159]

Note that the order and number of items doesn't matter.

### Dictionaries

- Dictionaries are unordered mappings for storing objects.
- Previously we saw how lists store objects in an ordered sequence, dictionaries
  use a key-value pairing instead.
- This key-value pair allows users to quickly grab objects without needing to
  know an index location.
- Dictionaries use curly braces and colons to signify the keys and their
  associated values.
  ```python
    {'key1':'value1','key2':'value2'}
  ```

__So when to choose a list and when to choose a dictionary?__

- Dictionaries:  Objects retrieved by key name.
  - Unordered and can not be sorted.
- Lists:  Objects retrieved by location.
  - Ordered Sequence can be indexed or sliced.

- Refer to the notebook
  at: `code/00-Python Object and Data Structure Basics/05-Dictionaries.ipynb`

#### Exercises
1. Create a dictionary where all the keys are strings, and all the values are integers.

For example:

{'Monday':19, 'Tuesday':20}


### Tuples

- Tuples are very similar to lists. However they have one key difference -
  immutability.
- Once an element is inside a tuple, it can not be reassigned.
- Tuples use parenthesis:  (1,2,3)

- Refer to the notebook
  at: `code/00-Python Object and Data Structure Basics/06-Tuples.ipynb`

### Sets

- Sets are unordered collections of unique elements.
- Meaning there can only be one representative of the same object.
- Refer to the notebook
  at: `code/00-Python Object and Data Structure Basics/07-Sets and Booleans.ipynb`

#### Exercises
1. Write an expression that would turn the string 'Mississippi'  into a set of unique letters.

For example:

set('Parallel')

would return the set {'P', 'a', 'e', 'l', 'r'}

### Booleans

- Booleans are operators that allow you to convey True or False statements.
- These are very important later on when we deal with control flow and logic!
- Refer to the notebook
  at: `code/00-Python Object and Data Structure Basics/07-Sets and Booleans.ipynb`

### Files

- Before we finish this section, let’s quickly go over how to perform simple I/O
  with basic .txt files.
- We’ll also discuss file paths on your computer
- Refer to the notebook
  at: `code/00-Python Object and Data Structure Basics/08-Files.ipynb`

#### Exercises
1. This exercise will require several lines of code.

Write a script that opens a file named 'test.txt' , writes 'Hello World'  to the file, then closes it.

For example, the following code opens a file called 'myfile.txt' , writes 'This is my file' , and closes it:

```
x = open('myfile.txt', 'w')
x.write('This is my file')
x.close()
```

## Python Comparison Operators
Refer to the notebooks at: `code/01-Python Comparison Operators`

## Python Statements
### If, elif , else Statements

- Let’s begin to learn about __control flow__.
- We often only want certain code to execute when a particular condition has been met.
- For example, `if`  my dog is hungry (some condition), then I will feed the dog (some action).
- To control this flow of logic we use some keywords:
  - if
  - elif
  - else

- Control Flow syntax makes use of colons and indentation (whitespace).

- This indentation system is crucial to Python and is what sets it apart from other programming languages.

- Syntax of an if statement

```
if some_condition:
  # execute some code
```

- Syntax of an if/else statement
```
if some_condition:
  # execute some code
else:
  # do something else

```


- Syntax of an if/else statement

```
if some_condition:
  # execute some code
elif some_other_condition:
  # do something different
else:
  # do something else
```

- Refer to the Notebook:
  - `code/02-Python Statements/01-Introduction to Python Statements.ipynb`
  - `code/02-Python Statements/02-if, elif, and else Statements.ipynb`

### For Loops
- Many objects in Python are “iterable”, meaning we can iterate over every element in the object.
- Such as every element in a list or every character in a string.
- We can use for loops to execute a block of code for every iteration.
- The term iterable means you can “iterate” over the object.
- For example you can iterate over every character in a string, iterate over every item in a list, iterate over every key in a dictionary.
- Syntax of a for loop
```
my_iterable = [1,2,3]
for item_name in my_iterable:
  print(item_name)
```
Outputs:
```
>> 1
>> 2
>> 3
```

- Refer to the Notebook: `code/02-Python Statements/03-for Loops.ipynb`

### While Loops
- While loops will continue to execute a block of code `while` some condition remains True.
- For example, `while` my pool is not full, keep filling my pool with water.
- Or `while` my dogs are still hungry, keep feeding my dogs.
- Syntax of a while loop
```
while some_boolean_condition:
  #do something
```

- You can combine with an else if you want
```
while some_boolean_condition:
  #do something
else:
	#do something different
```

- Refer to the Notebook: `code/02-Python Statements/04-while Loops.ipynb`

### Useful Operators
- Refer to the Notebook: `code/02-Python Statements/05-Useful-Operators.ipynb`

### List Comprehensions
- List Comprehensions are a unique way of quickly creating a list with Python.
- If you find yourself using a for loop along with .append() to create a list, List Comprehensions are a good alternative!
- Refer to the Notebook: `code/02-Python Statements/06-List Comprehensions.ipynb`

### Assessment
- Refer to the Notebook `code/02-Python Statements/07-Statements Assessment Test.ipynb` for the test.
- The solutions for the assessment is in the Notebook `08-Statements Assessment Test - Solutions.ipynb`. Before you refer to the solutions, take some time to answer the questions.
- Only refer to the solutions if you're blocked or have completed the assessment.

## Methods and Functions
- Built-in objects in Python have a variety of methods you can use!
- Let’s explore in a bit more detail how to find methods and how to get information about them.

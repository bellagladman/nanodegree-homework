# THEORY QUESTIONS ASSIGNMENT 
CFG NANODEGREE 2021 / SOFTWARE 3

ISOBEL GLADMAN

## PYTHON THEORY QUESTIONS (30 POINTS)

### 1. What is Python and what are its main features?

Python is a programming language. 

Key features:
* It’s easy to code - the syntax is quite like written English
* It’s open source - source code is free to download and there is an active community sharing knowledge
* Allows for object-oriented programming - Python allows OOP, which is a programming model that is centred around creating objects, rather than by creating functions/logic
* It’s a high-level language - Python is a high-level language which means we can write it out in words and mathematical language, as opposed to a low-level language in which you have to spell out the machine operations needed to run a program e.g. binary code
* It’s extensible - Python code can also be written in C and C++
a portable language - Python code for Windows can also be run on other operating systems e.g. Linux, Unix and Mac
* It’s an interpreted language - Python code is run line by line, and doesn’t need to be compiled (i.e. translated into a low-level language to be understood by a computer)
* It’s a dynamically typed language - the type of a variable is decided when it is run, rather than having to decide it in advance.

### Discuss the difference between Python 2 and Python 3
Python 3 supports ‘typing’—characteristics that relate to a piece of data’s type—whereas Python 2 doesn’t.

Python 2 and Python 3 have different syntaxes, i.e. in Python 3 you have to put brackets around a print statement e.g. print(“string”), but in Python 2 you could just write print “string”.

Python 2 is no longer supported, whereas Python 3 is. This also means that Python 2 is not forward-compatible, whereas Python 3 is. 

Python 2 uses ASCII which is 7-bit, whereas Python 3 uses Unicode, which is 8-bit. This means it can represent a larger variety of characters i.e. characters in alphabets other than the Western alphabet, emojis.

In mathematical operations, specifically division, Python 2 would round down to the nearest integer, but Python 3 would give an accurate answer. e.g. 5/2 in Python 2 would give 2, but in Python 3 it would be 2.5.

###What is PEP 8?
PEP 8 is a set of guidelines for writing beautiful, readable Python code. It was written in 2001 by Guido van Rossum (the founder of Python), Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code. PEP stands for Python Enhancement Proposal.

Key features:
* naming variables and objects - be specific and descriptive. This helps you remember what your code means. For most things, use snake case when naming, apart from Classes, where camel case is recommended, and packages, where all lower case is recommended. Avoid using single letter names containing capital O and capital I because these can be easily mistaken for zero (0) and one (1).
* whitespace - two lines between top-level functions and classes, one line between methods, and one line between steps in functions
* maximum line length and line breaking - suggested max line length of 79 characters. If you have a longer line, you can move it onto a new one if it is in parentheses/square brackets/braces. Or you can use backslashes \. Break before a binary operator like + or * so it’s easier to read.
* indentation - Important so you can see which actions relate to each other. PEP 8 recommends using 4 spaces rather than a tab. For readability, keep indented text to the same indent. When closing a list/set/tuple/dict etc. it’s best to keep the closing bracket on a new line, either at the same level of indentation as the contents, or at the level of the variable name. 
* commenting - comment in full sentences, for each section of your code. Separate paragraphs with an empty single line comment. Use inline comments sparingly, and try to put any information from an inline comment in the code itself, e.g. by naming a variable descriptively so you don’t have to comment to show what the variable contains.
* docstrings - similar to a paragraph comment, but enclosed in three speech marks “”” either side of the multi-line string. Use a docstring to explain the purpose of a top-level function/class/module.
* whitespace around operators - in general, surround operators like =, *, <= etc with a space on each side, except if you are assigning a default value to a function argument, e.g. def function(default_parameter=5):
* avoid trailing whitespace i.e. before a comma, inside a bracket etc.
* programming recommendations: you don’t need to check a Boolean value against whether it’s true or not, you can just say if my_bool: to mean true and if not my_bool: to mean false.
use starts.with() and endswith() rather than string slicing

### In computing / computer science, what is a program?
In computing, a program is a specific set of ordered operations for a computer to perform.

###In computing / computer science, what is a process?
A process is a program that is running on your computer. All processes are composed of one or more threads. The threads of a computer program allow the program to execute sequential actions or many actions at once. Each thread in a program identifies a process that runs when the program asks it to. 

###In computing / computer science, what is cache?
Cache is a small amount of memory which is a part of the CPU (Core Processing Unit). It’s closer to the CPU than RAM. It is used to temporarily hold instructions and data that the CPU is likely to reuse. 

CPU stands for central processing unit, which is also sometimes called a central processor, main processor or just processor. It is the electronic circuitry that executes instructions comprising a computer program. The CPU performs basic arithmetic, logic, controlling, and input/output operations specified by the instructions in the program.

RAM is short for random access memory. It is the super-fast and temporary data storage space that a computer needs to access right now or in the next few moments.

###In computing / computer science, what is a thread and what do we mean by multithreading?
In computer science, a thread of execution is the smallest sequence of programmed instructions that can be managed independently by a scheduler, which is typically a part of the operating system.

A thread is an execution context, which is all the information a CPU needs to execute a stream of instructions. It works a little like a bookmark, in the sense that it allows a processor to stop a process and then return to it exactly where it left off. It’s a self-contained sequence of instructions that can execute in parallel with other threads that are part of the same root process.

Whereas a thread is an execution context, a process is a collection of resources associated with a computation, such as memory pages (all the threads in a process have the same view of the memory), file descriptors (e.g., open sockets), and security credentials (e.g., the ID of the user who started the process). A process can have one or many threads. On a more technical level, a thread consists of the values of the CPU's registers.

Multithreading is a CPU (central processing unit) feature that allows two or more instruction threads to execute independently while sharing the same process resources. Multithreading allows multiple concurrent tasks to be performed within a single process. When data scientists are training machine learning algorithms, a multithreaded approach to programming can improve speed when compared to traditional parallel multiprocessing programs.

Even though it’s faster for an operating system to switch between threads than it is to switch between different processes, multithreading requires careful programming in order to avoid conflicts caused by race conditions and deadlocks. A race condition is when a device or system attempts to perform two or more operations at the same time, but because of the nature of the device or system, the operations must be done in the proper sequence to be done correctly. To prevent race conditions and deadlocks, programmers use locks that prevent multiple threads from modifying the value of the same variable at the same time.

###In computing / computer science what is concurrency and parallelism and what are the differences?
Concurrency is when two or more tasks can start, run, and complete in overlapping time periods. It doesn't necessarily mean they'll ever both be running at the same instant. For example, multitasking on a single-core machine.
However, parallelism is when tasks literally run at the same time, e.g., on a multicore processor.
The difference is that in parallelism, tasks actually run at the exact same time, however in concurrency, the tasks might overlap but it doesn’t mean that they will actually be both running simultaneously.

###What is GIL in Python and how does it work?
The Python Global Interpreter Lock or GIL is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter.

This means that only one thread can be in a state of execution at any point in time. The impact of the GIL isn’t visible to developers who execute single-threaded programs, but it can be a performance bottleneck in CPU-bound and multi-threaded code.

Since the GIL allows only one thread to execute at a time even in a multi-threaded architecture with more than one CPU core, the GIL has gained a reputation as an “infamous” feature of Python.

###What do these software development principles mean: DRY, KISS, BDUF
The DRY or Don’t Repeat Yourself principle is a software development practice aimed at reducing repetition of information.

KISS is an acronym which means Keep It Simple, Stupid. It means avoiding complexity and effort in computer programming where possible. 

Big Design Up Front (BDUF) is a software development approach in which the program's design is to be completed and perfected before that program's implementation is started. 

###What is a Garbage Collector in Python and how does it work?
Garbage collection releases memory when an object is no longer in use. The garbage collection system destroys the unused object and reuses its memory slot for new objects. 
Python has an automated garbage collection system which deallocates objects that are no longer needed. 

To explain the ways Python garbage collection works, we have to start by outlining the differences between objects, names and references. 

A Python object is stored in memory with names and references. A name is just a label for an object, so one object can have many names. A reference is a name(pointer) that refers to an object. Every Python object has three things: type, value, and reference count. When we assign a name to a variable, its type is automatically detected by Python. Value is declared while defining the object. Reference count is the number of names pointing to that object.

Python has two ways to delete the unused objects from the memory through its garbage collection system:
* Reference counting: if an object has no reference, it gets deleted by the garbage collection. One big problem in reference counting garbage collection is that it doesn’t work with cyclical references e.g. when an object refers to itself, such as when you append a list to itself. In this situation the reference count will never be 0, so the object won’t get deleted.
* Generational garbage collection: The garbage collector keeps track of all objects in memory. A new object starts its life in the first generation of the garbage collector. If Python executes a garbage collection process on a generation and an object survives, it moves up into a second, older generation.

###How is memory managed in Python?
Memory is managed in Python through its memory manager. The Python memory manager  manages Python’s memory allocations. There is a private heap that contains all Python objects and data structures. The Python memory manager manages the Python heap on demand. The Python memory manager has object-specific allocators to allocate memory distinctly for specific objects such as int, string, etc. Below that, the raw memory allocator interacts with the memory manager of the operating system to ensure that there’s space on the private heap.
The Python memory manager manages chunks of memory called blocks. A collection of blocks of the same size makes up a pool. Pools are created on arenas, chunks of 256kB memory allocated on heap=64 pools. If the objects get destroyed, the memory manager fills this space with a new object of the same size.

###What is a Python module?
In Python, modules are files with the .py extension containing Python code that can be imported inside another Python program, similar to a code library, or a file that contains a set of functions that you want to include in your application.

###What is docstring in Python?
Python docstrings are the string literals that appear right after the definition of a function, method, class, or module. They are used to document code.

```
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2
```
Here, the string literal:
```
'''Takes in a number n, returns the square of n'''
```
Inside the triple quotation marks is the docstring of the function square() as it appears right after its definition. We can access these docstrings using the __doc__ attribute. There are conventions around how to write docstrings for various objects, and these conventions are compiled in a document called PEP 257.

###What is pickling and unpickling in Python? Example usage.
“Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.

The Python module pickle is used for serialising and deserialising a Python object structure. Any object in Python can be pickled so that it can be saved on disk. What pickle does is that it “serialises” the object first before writing it to file. Pickling is a way to convert a python object (list, dict, etc.) into a character stream. The idea is that this character stream contains all the information necessary to reconstruct the object in another Python script.
```
def storeData():
    # initializing data to be stored in db
    Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak',
    'age' : 21, 'pay' : 40000}
    Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
    'age' : 50, 'pay' : 50000}
  
    # database
    db = {}
    db['Omkar'] = Omkar
    db['Jagdish'] = Jagdish
      
    # Its important to use binary mode
    dbfile = open('examplePickle', 'ab')
      
    # source, destination
    pickle.dump(db, dbfile)                     
    dbfile.close()
  
def loadData():
    # for reading also binary mode is important
    dbfile = open('examplePickle', 'rb')     
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()
  
if __name__ == '__main__':
    storeData()
    loadData()
```
###What are the tools that help to find bugs or perform static analysis?
Pychecker and Pylint are the static analysis tools that help to find bugs in python. 

Pychecker is an open-source tool for static analysis that detects bugs from source code and warns about the style and complexity of the bug.

Pylint is also an open-source tool for static code analysis. It looks for programming errors and is used for coding standards, e.g. checking the length of each programming line; checking the variable names according to the project style. Pylint is highly configurable and it acts like a special program to control warnings and errors. It can also be used as a standalone program, and it also integrates with Python IDEs such as Pycharm, Spyder, Eclipse, and Jupyter.

###How are arguments passed in Python by value or by reference? Give an example
In Python, variables and the objects they store are not considered the same thing. 
```
def set_list(list):
    list = ["A", "B", "C"]
    return list
  
def add(list):
    list.append("D")
    return list
  
my_list = ["E"]
  
print(set_list(my_list))
  
print(add(my_list))

---Output---

['A', 'B', 'C']
['E', 'D']
```
In the above functions, the variable my_list is transformed by the function def set_list to give ['A', 'B', 'C']. The same variable is transformed by the program def add_list to give ['E', 'D']. Basically this shows that in Python, functions can take in a variable, and are able to reassign it to point to a different object - they pass values by the reference (i.e. the variable/name of the object) rather than the value of the object itself. This means that if a function redefines a variable, it affects the variable.

Pass by value, on the other hand, would mean that when a function takes in a variable containing an object, the original object is unchanged and is stored somewhere different in the memory than the new object that the function supplies after being carried out.

However, for some Python programmers like Robert Heaton https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/, ​​Python’s argument passing model is neither pass-by-value, nor pass-by-reference, but pass-by-object-reference.

Heaton’s specification explains that in Python, when arguments are passed, hallmarks of both pass-by-value and pass-by-reference are true; when a function takes in a variable containing an object, Python creates a new reference to that object, allowing it to both stay the same and be saved as is in memory, but also be updated. 

###What are Dictionary and List comprehensions in Python? Provide examples.
List Comprehension is a way to create lists in Python in just a single line of code through easy-to-read for loops.

An example of list comprehension syntax:
```
x = [i for i in range(10)]
```

Dictionary comprehension is a method for transforming one dictionary into another dictionary, following similar conventions to the list comprehension syntax. During a dictionary comprehension, items within the original dictionary can be conditionally included in the new dictionary, and each item can be transformed as needed.

An example of dictionary comprehension syntax:
```	
dict([(i, i+10) for i in range(4)])
```

###What is namespace in Python?
A namespace is a collection of currently defined symbolic names along with information about the object that each name references. You can think of a namespace as a dictionary in which the keys are the object names and the values are the objects themselves. Each key-value pair maps a name to its corresponding object.
In a Python program, there are four types of namespaces:
* Built-In
* Global
* Enclosing
* Local

These have differing lifetimes. As Python executes a program, it creates namespaces as necessary and deletes them when they’re no longer needed. Typically, many namespaces will exist at any given time.

###What is pass in Python?
The pass statement is a null statement. But the difference between pass and comment is that comment is ignored by the interpreter whereas pass is not ignored. 
It is generally used as a placeholder i.e. when the user does not know what code to write, so the user simply places the pass statement at that line. Sometimes, pass is used when the user doesn’t want any code to execute, so the user can simply place the pass statement where empty code is not allowed, like in loops, function definitions, class definitions, or in if statements. 

Example:
```
def geekFunction:
  pass
```

###What is a unit test in Python?
Unit testing is a software testing method by which individual units of source code are put under various tests to determine whether they are fit for use. It determines and ascertains the quality of your code. Unit tests are carried out using the unittest module. A unit test takes each little part of your code and tests that that section works. While manually running a series of print statements to check each stage in a program might be a feasible way to check code when you’re working on a very small program, when it comes to working on a sprawling piece of code, unit testing is much preferred because you can automate the tests and therefore save yourself time. 

###In Python what is slicing?
Slicing in Python is a feature that enables accessing parts of sequences like strings, tuples, and lists. You can also use slices to modify or delete the items of mutable sequences such as lists. Slices can also be applied on third-party objects like NumPy arrays, as well as Pandas series and data frames.

Slicing enables writing clean, concise, and readable code. It’s similar to indexing but returns a sequence of items instead of a single item. The indices used for slicing are also zero-based.

There are two variants of the slicing syntax: 
* sequence[start:stop]
* sequence[start:stop:step].

###What is a negative index in Python?
Python programming language supports negative indexing of arrays, something which is not available in arrays in most other programming languages. This means that the index value of -1 gives the last element, and -2 gives the second last element of an array. The negative indexing starts from where the array ends. This means that the last element of the array is the first element in the negative indexing which is -1.

###How can the ternary operators be used in python? Give an example.
The ternary operator is a type of conditional expression in Python that evaluates a statement. Ternary operators perform an action based on whether that statement is true or false. They are more concise than a traditional if…else statement. It’s a bit like how a list comprehension condenses a list.

The syntax for the Python ternary statement is as follows:
```[if_true] if [expression] else [if_false]```

The ternary conditional operator in Python gets its name from the fact it takes in three parameters: if_true, expression, and if_false.

Ternary operators are usually used to determine the value of a variable. The variable takes on the value of if_true if the statement evaluates to True, or if_false if the statement evaluates to false.

An example:
```
age = 48
discount = True if age >= 65 else False
print(discount)
```

###What does this mean: *args, **kwargs? And why would we use it?
*args and **kwargs are mostly used in function definitions. *args and **kwargs allow you to pass an unspecified number of arguments to a function, so when writing the function definition, you do not need to know how many arguments will be passed to your function. *args is used to send a non-keyworded variable length argument list to the function, while **kwargs allows you to pass keyworded variable length of arguments to a function. You should use **kwargs if you want to handle named arguments in a function.

###How are range and xrange different from one another?
Range and xrange are both functions for creating lists, or a range of integers that assist in making for loops. They are the same in terms of functionality. The only difference is that range returns a Python list object, and xrange returns an xrange object. Xrange doesn't actually generate a static list at run-time like range does. It creates the values as you need them with a special technique called yielding. This technique is used with a type of object known as generators.

Xrange is needed when you have a really gigantic range for which you'd like to generate a list. Range uses a lot of memory and will use memory until it runs out and crashes your system. Xrange doesn’t use memory in this way, so you can work with bigger ranges of numbers with more security. 

###What is Flask and what can we use it for?
Flask is a web framework written in Python, i.e. a collection of libraries and modules that enable web application developers to write applications without worrying about low-level details such as protocol, thread management. It has a small and easy-to-extend core, and is a microframework which doesn’t include an ORM (Object Relational Manager) or such features. It was developed by Armin Ronacher, who led a team of international Python enthusiasts called Pocco. Flask is based on the Werkzeg WSGI toolkit and the Jinja2 template engine. Both are Pocco projects.

###What are clustered and non-clustered indexes in a relational database?
An index is a way of speeding up queries against a table. Because tables are often filled with data in an ad hoc manner, it means that the data in them is often not ordered in an easily parsable way. If you query against a table for, say, lastName = ‘Smith’, the processor has to check each and every record’s lastName value against ‘Smith’. This could take a long time if you have millions of rows of data! An index works as a ‘support’ table to your main table, by going through the table and recording references to where particular bits of data sit in a table. 

Take the real-life example of a biology textbook. Let’s say you wanted to look up the topic of cell division. Now you could read every page in the textbook until you get to the pages regarding cell division, but this might take a long time. Instead, textbooks usually have an index in the back, which is indexed by topics. So each topic is ordered alphabetically, with the relevant page numbers next to them. This is an example of a non-clustered index, because the data is not ‘clustered’ next to the index - the data (i.e. the actual textbook pages) is separate from the index (at the back of the book, in a separate section).

Contrast that with the real-life example of a phone book. Phone books are already organised alphabetically by last name, starting with surnames beginning with A and going through the alphabet. Each name has a phone number attached to them. Let’s say you wanted to look up the number for your friend Charlie, last name Jones. This time, you would just head to the part of the book where you thought the Js would be (J for Jones), flipping forward if you had landed on a page before the Js, or backwards if you had landed on a page after the Js. There’s no need for a separate index, because the phonebook is already indexed (by last name, alphabetically). This is an example of a clustered index. 

In database terms, a clustered index describes when a table is already ordered by a set of unique values, such as by a primary key. Practical DB examples of this might include columns that have ID numbers in them, as every record should have its own unique ID number. Essentially, in MySQL, when you set a column as a primary key, you are by default creating a clustered index on that primary key. 

A non-clustered index would be where you are creating an index on a column that is not the primary key. For example, if you created an index on lastNames, ordering them in ascending order, that would mean the index creates a record of all of the lastName values in ascending order, and then a corresponding reference back to the original table, to show where that value can be found. When querying an attribute that has been indexed e.g. querying lastName = ‘Smith’ when lastName has been indexed, the processor heads to the index, and is able to find ‘Smith’ much more easily, as the index has stored the data in ascending order. When it finds ‘Smith’, it can then look at the corresponding reference back to the original table, and then go to the original table and find the entry for ‘Smith’ there at the point referenced. 

###What is a ‘deadlock’ in a relational database?
A deadlock happens when two concurrent transactions cannot progress because each one waits for the other to release a lock.

###What is a ‘livelock’ in a relational database?
A livelock is where a request for exclusive lock is denied continuously because a series of overlapping shared locks keeps on interfering with each other, and to adapt to each other, they keep on changing the status which further prevents them from completing the task. 

This is similar to but different from deadlock. In a livelock, both processes keep changing to adapt to one another, but end up blocking each other. However, in deadlock, neither of the processes move and still block each other. A real-life example of livelock would be like two people going opposite directions down a narrow corridor, and they both keep stepping to the side to let the other go past, but they keep both stepping to the same side at the same time, so neither of them can pass.

## PYTHON STRING METHODS

| METHOD       | Description                                                                                                                                                                                             | Example                                                                                                                                                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| capitalize() | converts the first character of a string to a capital letter                                                                                                                                            | string = 'the quick brown fox'<br>print(string.capitalize())<br><br>The quick brown fox                                                                                                                                             |
| casefold()   | (same as lower()) converts a string to lowercase                                                                                                                                                        | string = 'the QUICK brown fox'<br>print(string.casefold())<br><br>the quick brown fox                                                                                                                                               |
| center()     | returns a centred string                                                                                                                                                                                | txt = "banana"<br><br>x = txt.center(20)<br><br>print(x)<br><br>banana                                                                                                                                                              |
| count()      | counts how many times a designated character/phrase occurs in a string                                                                                                                                  | string = 'the QUICK brown fox'<br>print(string.count('Q'))<br><br>1                                                                                                                                                                 |
| endswith()   | checks whether a string ends with (a) designated character(s)                                                                                                                                           | string = 'the QUICK brown fox'<br>print(string.endswith('Q'))<br><br>False                                                                                                                                                          |
| find()       | (same as index()) searches a string for designated character(s) and returns the position of where it is found                                                                                           | string = 'the QUICK brown fox'<br>print(string.find('x'))<br><br>18                                                                                                                                                                 |
| format()     | allows a string to be formatted                                                                                                                                                                         | string = 'The quick brown fox'<br>print('A common sentence to practise handwriting starts with: {}'.format(string))<br><br>A common sentence to practise handwriting starts with: The quick brown fox                               |
| index()      | (same as find())searches a string for designated character(s) and returns the position of where it is found                                                                                             | string = 'the QUICK brown fox'<br>print(string.index('h'))<br><br>1                                                                                                                                                                 |
| isalnum()    | returns True if all characters in the string are alphanumeric (letters and numbers, not spaces/symbols)                                                                                                 | string = 'the quick brown fox'<br>print(string.isalnum())<br><br>False                                                                                                                                                              |
| isalpha()    | returns True if all characters in the string are in the alphabet                                                                                                                                        | string = 'aardvark'<br>print(string.isalpha())<br><br>True                                                                                                                                                                          |
| isdigit()    | returns True if all characters in the string are digits (0-9)                                                                                                                                           | string = 'aardvark'<br>print(string.isdigit())<br><br>False                                                                                                                                                                         |
| islower()    | checks whether (a) character(s) is lowercase or not                                                                                                                                                     | string = 'aardvark'<br>print(string.islower())<br><br>True                                                                                                                                                                          |
| isnumeric()  | returns True if all characters are numeric (including any character in another language that is used in place of digits)                                                                                | \>>> '一二三四五'.isnumeric()<br><br>True                                                                                                                                                                                                |
| isspace()    | returns True if all characters in a string are whitespace                                                                                                                                               | string = ' '<br>print(string.isspace())<br><br>True                                                                                                                                                                                 |
| istitle()    | returns True if the string follows the rules of a title                                                                                                                                                 | string = 'The Quick Brown Fox'<br>print(string.istitle())<br><br>True                                                                                                                                                               |
| isupper()    | checks whether a string is entirely uppercase                                                                                                                                                           | string = 'The Quick Brown Fox'<br>print(string.isupper())<br><br>False                                                                                                                                                              |
| join()       | converts the elements of an iterable into a string i.e. converts a list into a string                                                                                                                   | myTuple = ("The", "quick", "brown", “fox”)<br>x = "#".join(myTuple)<br>print(x)<br><br>The#quick#brown#fox                                                                                                                          |
| lower()      | put a string into all lower case                                                                                                                                                                        | string = 'The Quick Brown Fox'<br>print(string.lower())<br><br>the quick brown fox                                                                                                                                                  |
| lstrip()     | returns a left trim version of the string                                                                                                                                                               | string = ' The Quick Brown Fox'<br>print(string.lstrip())<br><br>The Quick Brown Fox                                                                                                                                                |
| replace()    | replace (a) designated character(s)                                                                                                                                                                     | txt = "I like dogs"<br>x = txt.replace("dogs", "aardvarks")<br>print(x)<br><br>I like aardvarks                                                                                                                                     |
| rsplit()     | splits the string at the specified separator, and returns a list. If you specify a max, the list will return the specified number of elements plus one. (If you don’t, rsplit() is the same as split()) | txt = "giraffe, parrot, rhino"<br>x = txt.rsplit(", ")<br>print(x)<br><br>\['giraffe', 'parrot', 'rhino'\]<br>\-----<br>txt = "giraffe, parrot, rhino"<br>x = txt.rsplit(", ", 1)<br>print(x)<br><br>\['giraffe, parrot', 'rhino'\] |
| rstrip()     | returns a right trim version of the string                                                                                                                                                              | string = 'The Quick Brown Fox '<br>print(string.rstrip())<br><br>The Quick Brown Fox                                                                                                                                                |
| split()      | splits the string at the specified separator, and returns a list                                                                                                                                        | txt = "giraffe, parrot, rhino"<br>x = txt.split(", ")<br>print(x)<br><br>\['giraffe', 'parrot', 'rhino'\]                                                                                                                           |
| splitlines() | splits the string at line breaks and returns a list                                                                                                                                                     | txt = "Thank you for the music\\nWelcome to the jungle"<br>x = txt.splitlines()<br>print(x)<br><br>\['The quick brown fox', 'jumps over the lazy dog'\]                                                                             |
| startswith() | starts with (a) designated character(s)                                                                                                                                                                 | string = 'The quick brown fox'<br>print(string.startswith('T'))<br><br>True                                                                                                                                                         |
| strip()      | returns a trimmed version of the string                                                                                                                                                                 | txt = " parrots "<br>x = txt.strip()<br>print("of all birds", x, "are my favourite")<br><br>of all birds parrots are my favourite                                                                                                   |
| swapcase()   | change uppercase to lowercase and vice versa                                                                                                                                                            | txt = "I LiKe parrOTS"<br>x = txt.swapcase()<br>print(x)<br><br>i lIkE PARRots                                                                                                                                                      |
| title()      | put a string into title case i.e. a capital letter at the beginning of each word, the rest of the word in lower case                                                                                    | txt = "I LiKe parrOTS"<br>x = txt.title()<br>print(x)<br><br>I Like Parrots                                                                                                                                                         |
| upper()      | put a string into all uppercase letters                                                                                                                                                                 | txt = "I LiKe parrOTS"<br>x = txt.upper()<br>print(x)<br><br>I LIKE PARROTS                                                                                                                                                         |

## PYTHON LIST METHODS

| Method    | Description                                                                                                 | Example                                                                                                                                                                                                                                                                                                                                 |
| --------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| append()  | adds a new item to the end of a list                                                                        | fruits = \['apple', 'banana', 'cherry'\]<br>fruits.append("pear")<br>print(fruits)<br><br>\['apple', 'banana', 'cherry', 'pear'\]                                                                                                                                                                                                       |
| clear()   | empties a list                                                                                              | fruits = \['apple', 'banana', 'cherry'\]<br>fruits.clear()<br>print(fruits)<br><br>\[\]                                                                                                                                                                                                                                                 |
| copy()    | copies the list                                                                                             | fruits = \['apple', 'banana', 'cherry'\]<br>more\_fruits = fruits.copy()<br>print(more\_fruits)<br><br>\['apple', 'banana', 'cherry'\]                                                                                                                                                                                                  |
| count()   | counts the number of items with the designated value                                                        | animals = \['rabbit', 'monkey', 'horse'\]<br>how\_many\_rabbits = animals.count('rabbit')<br>print(how\_many\_rabbits)<br><br>1                                                                                                                                                                                                         |
| extend()  | joins one list to another                                                                                   | animals = \['rabbit', 'monkey', 'horse'\]<br>more\_animals = \['rat', 'dragon'\]<br>animals.extend(more\_animals)<br>print(animals)<br><br>\['rabbit', 'monkey', 'horse', 'rat', 'dragon'\]                                                                                                                                             |
| index()   | returns the index of the first instance of the designated value                                             | animals = \['rabbit', 'monkey', 'rabbit', 'horse','rat', 'dragon'\]<br>print(animals.index('rabbit'))<br><br>0                                                                                                                                                                                                                          |
| insert()  | allows an item to be inserted into a list at a designated index                                             | animals = \['rabbit', 'monkey', 'rabbit', 'horse','rat', 'dragon'\]<br>animals.insert(2, 'ox')<br>print(animals)<br><br>\['rabbit', 'monkey', 'ox', 'rabbit', 'horse', 'rat', 'dragon'\]                                                                                                                                                |
| pop()     | removes the last item from a list. You can also specify an index and pop will remove the item at that index | animals = \['rabbit', 'monkey', 'rabbit', 'horse', 'rat', 'dragon'\]<br>animals.pop()<br>print(animals)<br><br>\['rabbit', 'monkey', 'rabbit', 'horse', 'rat'\]<br><br>animals = \['rabbit', 'monkey', 'rabbit', 'horse', 'rat', 'dragon'\]<br>animals.pop(2)<br>print(animals)<br><br>\['rabbit', 'monkey', 'horse', 'rat', 'dragon'\] |
| remove()  | removes the first instance of the designated value                                                          | animals = \['rabbit', 'monkey', 'rabbit', 'horse', 'rat', 'dragon'\]<br>animals.remove('rabbit')<br>print(animals)<br><br>\['monkey', 'rabbit', 'horse', 'rat', 'dragon'\]                                                                                                                                                              |
| reverse() | reverses the order of the list                                                                              | animals = \['rabbit', 'monkey', 'rabbit', 'horse', 'rat', 'dragon'\]<br>animals.reverse()<br>print(animals)<br><br>\['dragon', 'rat', 'horse', 'rabbit', 'monkey', 'rabbit'\]                                                                                                                                                           |
| sort()    | sorts the list in ascending order                                                                           | animals = \['rabbit', 'monkey', 'rabbit', 'horse', 'rat', 'dragon'\]<br>animals.sort()<br>print(animals)<br><br>\['dragon', 'horse', 'monkey', 'rabbit', 'rabbit', 'rat'\]                                                                                                                                                              |

## PYTHON TUPLE METHODS

| Method  | Description                                                                             | Example                                                                                   |
| ------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| count() | Returns the number of times a specified value occurs in a tuple                         | my\_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)<br>x = my\_tuple.count(5)<br>print(x)<br><br>2 |
| index() | Searches the tuple for a specified value and returns the position of where it was found | my\_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)<br>x = my\_tuple.index(8)<br>print(x)<br><br>3 |

## PYTHON DICTIONARY METHODS

| Method       | Description                                                                                                 | Example                                                                                                                                                                                              |
| ------------ | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| clear()      | Removes all the elements from the dictionary                                                                | car = {<br>"brand": "Ford",<br>"model": "Mustang",<br>"year": 1964<br>}<br>car.clear()<br>print(car)<br><br>{}                                                                                       |
| copy()       | Returns a copy of the dictionary                                                                            | car = {<br>"brand": "Ford",<br>"model": "Mustang",<br>"year": 1964<br>}<br>x = car.copy()<br>print(x)<br><br>{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}                                     |
| fromkeys()   | Returns a dictionary with the specified keys and value                                                      | x = ('key1', 'key2', 'key3')<br>y = 0<br>thisdict = dict.fromkeys(x, y)<br>print(thisdict)<br><br>{'key1': 0, 'key2': 0, 'key3': 0}                                                                  |
| get()        | Returns the value of the specified key                                                                      | car = {<br>"brand": "Ford",<br>"model": "Mustang",<br>"year": 1964<br>}<br>x = car.get("model")<br>print(x)<br><br>Mustang                                                                           |
| items()      | Returns a list containing a tuple for each key value pair                                                   | car = {<br>"brand": "Ford",<br>"model": "Mustang",<br>"year": 1964<br>}<br>x = car.items()<br>print(x)<br><br>dict\_items(\[('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)\])               |
| keys()       | Returns a list containing the dictionary's keys                                                             | car = {<br>"brand": "Ford",<br>"model": "Mustang",<br>"year": 1964<br>}<br>x = car.keys()<br>print(x)<br><br>dict\_keys(\['brand', 'model', 'year'\])                                                |
| pop()        | Removes the element with the specified key                                                                  | car = {<br>"brand": "Ford",<br>"model": "Mustang",<br>"year": 1964<br>}<br>car.pop("model")<br>print(car)<br><br>{'brand': 'Ford', 'year': 1964}                                                     |
| popitem()    | Removes the last inserted key-value pair                                                                    | car = {<br>"brand": "Ford",<br>"model": "Mustang",<br>"year": 1964<br>}<br>car.popitem()<br>print(car)<br><br>{'brand': 'Ford', 'model': 'Mustang'}                                                  |
| setdefault() | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value | car = {<br>"brand": "Ford",<br>"model": "Mustang",<br>"year": 1964<br>}<br>x = car.setdefault("model", "Bronco")<br>print(x)<br><br>Mustang                                                          |
| update()     | allows new key-value pairs to be added to a dictionary                                                      | car = {<br>"brand": "Ford",<br>"model": "Mustang",<br>"year": 1964<br>}<br>car.update({"color": "White"})<br>print(car)<br><br>{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'} |
| values()     | Returns a list of all the values in the dictionary                                                          | car = {<br>"brand": "Ford",<br>"model": "Mustang",<br>"year": 1964<br>}<br>x = car.values()<br>print(x)<br><br>dict\_values(\['Ford', 'Mustang', 1964\])                                             |

### PYTHON SET METHODS

| Method                  | Description                                                      | Example                                                                                                                                                                    |
| ----------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| add()                   | Adds an element to the set                                       | fruits = {"apple", "banana", "cherry"}<br>fruits.add("orange")<br>print(fruits)<br><br>{'orange', 'apple', 'cherry', 'banana'}                                             |
| clear()                 | Removes all the elements from the set                            | fruits = {"apple", "banana", "cherry"}<br>fruits.clear()<br>print(fruits)<br><br>set()                                                                                     |
| copy()                  | Returns a copy of the set                                        | fruits = {"apple", "banana", "cherry"}<br>x = fruits.copy()<br>print(x)<br><br>{'cherry', 'banana', 'apple'}                                                               |
| difference()            | Returns a set containing the difference between two or more sets | x = {"apple", "banana", "cherry"}<br>y = {"google", "microsoft", "apple"}<br>z = x.difference(y)<br>print(z)<br><br>{'banana', 'cherry'}                                   |
| intersection()          | Returns a set that is the intersection of two or more sets       | x = {"apple", "banana", "cherry"}<br>y = {"google", "microsoft", "apple"}<br>z = x.intersection(y)<br>print(z)<br><br>{'cherry', 'banana'}                                 |
| issubset()              | Returns whether another set contains this set or not             | x = {"a", "b", "c"}<br>y = {"f", "e", "d", "c", "b", "a"}<br>z = x.issubset(y)<br>print(z)<br><br>True                                                                     |
| issuperset()            | Returns whether this set contains another set or not             | x = {"f", "e", "d", "c", "b", "a"}<br>y = {"a", "b", "c"}<br>z = x.issuperset(y)<br>print(z)<br><br>True                                                                   |
| pop()                   | Removes an element from the set                                  | fruits = {"apple", "banana", "cherry"}<br>fruits.pop()<br>print(fruits)<br><br>{'banana', 'cherry'}                                                                        |
| remove()                | Removes the specified element                                    | fruits = {"apple", "banana", "cherry"}<br>fruits.remove("banana")<br>print(fruits)<br><br>{'apple', 'cherry'}                                                              |
| symmetric\_difference() | Returns a set with the symmetric differences of two sets         | x = {"apple", "banana", "cherry"}<br>y = {"google", "microsoft", "apple"}<br>z = x.symmetric\_difference(y)<br>print(z)<br><br>{'cherry', 'google', 'banana', 'microsoft'} |
| union()                 | Return a set containing the union of sets                        | x = {"apple", "banana", "cherry"}<br>y = {"google", "microsoft", "apple"}<br>z = x.union(y)<br>print(z)<br><br>{'banana', 'google', 'cherry', 'microsoft', 'apple'}        |
| update()                | Update the set with another set, or any other iterable           | x = {"apple", "banana", "cherry"}<br>y = {"google", "microsoft", "apple"}<br>x.update(y)<br>print(x)<br><br>{'microsoft', 'cherry', 'banana', 'apple', 'google'}           |

## PYTHON FILE METHODS

| Method       | Description                             | Example                                                                                                                                                                                                    |
| ------------ | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| read()       | Returns the file content                | f = open("demofile.txt", "r")<br>print(f.read())                                                                                                                                                           |
| readline()   | Returns one line from the file          | f = open("demofile.txt", "r")<br>print(f.readline())                                                                                                                                                       |
| readlines()  | Returns a list of lines from the file   | f = open("demofile.txt", "r")<br>print(f.readlines())                                                                                                                                                      |
| write()      | Writes the specified string to the file | f = open("demofile2.txt", "a")<br>f.write("See you soon!")<br>f.close()<br><br>#open and read the file after the appending:<br>f = open("demofile2.txt", "r")<br>print(f.read())                           |
| writelines() | Writes a list of strings to the file    | f = open("demofile3.txt", "a")<br>f.writelines(\["See you soon!", "Over and out."\])<br>f.close()<br><br>#open and read the file after the appending:<br>f = open("demofile3.txt", "r")<br>print(f.read()) |

## REFERENCES
CFG Nanodegree slides
https://careerkarma.com/blog/python-2-vs-python-3/
https://realpython.com/python-pep8/
https://searchsoftwarequality.techtarget.com/definition/program
https://techterms.com/definition/process
https://techterms.com/definition/thread
https://www.bbc.co.uk/bitesize/guides/zmb9mp3/revision/3
https://stackoverflow.com/questions/5201852/what-is-a-thread-really
https://en.wikipedia.org/wiki/Multithreading_(computer_architecture)
https://www.techopedia.com/definition/24297/multithreading-computer-architecture
https://stackoverflow.com/questions/1050222/what-is-the-difference-between-concurrency-and-parallelism
https://www.geeksforgeeks.org/difference-between-concurrency-and-parallelism/
https://medium.com/@itIsMadhavan/concurrency-vs-parallelism-a-brief-review-b337c8dac350
https://www.bbc.co.uk/bitesize/guides/z2342hv/revision/1
https://searchstorage.techtarget.com/definition/race-condition
https://realpython.com/python-gil/
https://realpython.com/lessons/dry-principle/
https://dev.to/kwereutosu/the-k-i-s-s-principle-in-programming-1jfg
https://en.wikipedia.org/wiki/Big_Design_Up_Front
https://www.analyticsvidhya.com/blog/2021/07/working-with-modules-in-python-must-known-fundamentals-for-data-scientists/
https://towardsdatascience.com/memory-management-and-garbage-collection-in-python-c1cb51d1612c
https://towardsdatascience.com/memory-management-in-python-6bea0c8aecc9
https://www.programiz.com/python-programming/docstrings
https://www.tutorialspoint.com/what-are-the-tools-that-help-to-find-bugs-or-perform-static-analysis-in-python
https://help.hcltechsw.com/dom_designer/10.0.1/basic/LSAZ_PASSING_ARGUMENTS_BY_REFERENCE_AND_BY_VALUE.html
https://www.tutorialspoint.com/how-are-arguments-passed-by-value-or-by-reference-in-python
https://www.geeksforgeeks.org/understanding-python-pickling-example/
https://realpython.com/python-pass-by-reference/
https://cmdlinetips.com/2018/01/5-examples-using-dict-comprehension/
https://www.datacamp.com/community/tutorials/python-dictionary-comprehension
https://www.netguru.com/blog/python-list-comprehension-dictionary
https://realpython.com/python-namespaces-scope/
https://www.geeksforgeeks.org/python-pass-statement/
https://www.datacamp.com/community/tutorials/unit-testing-python
https://www.blog.duomly.com/slicing-in-python-what-is-it/
https://www.i2tutorials.com/what-are-negative-indexes-and-why-are-they-used/
https://careerkarma.com/blog/python-ternary-operator/
https://book.pythontips.com/en/latest/args_and_kwargs.html
https://www.pythoncentral.io/how-to-use-pythons-xrange-and-range/
https://www.w3schools.com/python/python_strings_methods.asp
https://www.w3schools.com/python/python_ref_list.asp
https://www.w3schools.com/python/python_ref_dictionary.asp
https://www.w3schools.com/python/python_ref_tuple.asp
https://www.w3schools.com/python/python_ref_set.asp
https://www.w3schools.com/python/python_ref_file.asp


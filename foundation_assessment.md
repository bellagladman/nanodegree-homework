# FOUNDATION ASSESSMENT
Student: Isobel Gladman

## 1. THEORY QUESTIONS (20 marks)

**1. What is the program?**
A set of ordered operations that the computer performs.

**2. What is the process?**
A process is a program running on your computer, i.e. an active program.

**3. What is Cache?**
Cache is part of the CPU, and is a small amount of memory; it's closer to the CPU than RAM, 
and is used for temporarily holding information that the CPU is probably going to reuse.

**4. What is Thread and Multithreading?**
A thread is an execution context, and the smallest sequence of instructions that can be executed.
Multithreading is something the CPU can do, and it allows more than one thread to be executed at the same time.
i.e. it lets more than one task happen at the same time within a process.

**5. What is GIL in Python and how does it work?**
GIL stands for Global Interpreter Lock. It allows only one thread 
to hold the control of the Python interpreter.

**6. What is Concurrency and Parallelism and what are the differences?**
Parallelism means that two tasks are running at the same time. 
Concurrency means that the tasks might overlap but might not ever run at the same time.

**7. What do these stand for in programming: DRY, KISS, BDUF**

DRY - Don't Repeat Yourself

KISS - Keep It Simple, Stupid

BDUF - Big Design Up Front

**8. What is Garbage collector? How does it work?**
Garbage collection releases memory when an object is no longer being used. 
The garbage collector destroys the unused object and reuses its memory slot for new objects. 
Python has an automated garbage collection system which decommissions
objects that are no longer needed. It does this through both reference counting 
(i.e. if something hasn't got any references to it, its reference count is 0. 
When it's 0, the object will be deleted.) and also a generational process whereby
each time the garbage collector runs a garbage collection, an item that survives that
collection gets moved into a second, older generation.

**9. What are ‘deadlock’ and ‘livelock’ in a relational database?**
A deadlock happens when two concurrent transactions cannot progress 
because each one waits for the other to release a lock. 
A livelock is where a request for exclusive lock is denied continuously 
because some overlapping shared locks keep on interfering with each other, 
and so to adapt to each other, they keep changing their status
which keeps them both in stalemate.

**10. What is Flask and what can we use it for?**
Flask is a web framework in Python; it contains libraries and modules that allow developers
to develop web applications easily.

##2. DIFFERENCES BETWEEN PYTHON 2 AND PYTHON 3(8 marks)

The differences between Python 2 and Python 3 are:
- support - Python 2 is no longer supported, and Python 3 is
- mathematical - Python 2 would round down in division, and Python 3 is more accurate
- syntax - different syntax between Python 2 and Python 3 e.g. in Python 3 you use brackets around a print statement and in Python 2 you don't
- typing - Python 3 supports 'typing' and Python 2 doesn't
- Unicode/ASCII - Python 3 uses Unicode which is 8-bit, and Python 2 uses ASCII which is 7-bit

## 3. CODING QUESTION (8 marks)
see related Python file

## 4. CODING QUESTION (8 marks)
see related Python file

## 5. AGILE/SCRUM METHODOLOGY QUESTION (8 marks)
Agile and Scrum methodology
1. Scrum planning - a session before the scrum starts, where the scrum master, team and project owner come together to design the strategy for the scrum e.g. objectives, priorities, internal deadlines, assigning tasks
2. Scrum review - a session where the team gets together to present completed work and see whether anything else needs to be done
3. Scrum retrospective - a session after the scrum has finished and the product has been delivered, reviewing how the scrum worked (what went well and what could be done better)

## 6.  EXCEPTION HANDLING Q (8 marks)
Exception handling in python:
- Try - the try block denotes the code that you would like the function to try using
- Except - the except block is there to catch exceptions. You write an except block when you know that your try block could potentially raise errors. In an except block, you raise exceptions based on the specific error that you think you might catch, e.g. in a function that divides one number by another, you can raise a ValueError or a ZeroDivisionError to catch if someone tries to divide by 0 (mathematically impossible)
- Else - this code runs if the try block runs without throwing an exception
- Finally - this code runs no matter what (both if the try block runs without a hitch, or if an exception is thrown)

## 7. CONCEPT QUESTION (8 marks)
To connect Python with a MySQL database, you need to import the MySQL Connector module into Python.
With the MySQL Connector module comes a number of methods, including connect_to_db().
With connect_to_db(), you apply it to your database name to establish a connection, and then save it into a variable, so you can perform actions on it later.

You also need to set up a cursor to execute your queries, which you can do with .cursor(). You use the cursor to execute your Python query onto the MySQL database.
If you're retrieving things from the database, you use the .fetchall() method on your cursor and save it into a variable.
If you're adding things to the database/updating data, you might use the .commit() method on your database connection.
When you've finished doing things with the cursor, you have to close it, by using the .close() method on it.

When you've finished, you also need to make sure you close your database connection (by using the .close() method on the database connection variable).

## 8. SQL PRACTICAL QUESTION (10 marks)
```
SELECT authors.author_name, SUM(books.sold_copies)
FROM authors 
INNER JOIN books ON authors.book_name = books.book_name 
GROUP BY author_name 
ORDER BY SUM(books.sold_copes) DESC LIMIT 3;
```

# 9. CODING QUESTION (22 marks)
see related python file
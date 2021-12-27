#SPECIALISATION THEORY QUESTIONS ASSIGNMENT
##Software Stream
### Student: Isobel Gladman

## How does Object-Oriented Programming differ from Process-Oriented Programming?
Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields (also known as attributes or properties), and code, in the form of procedures (often known as methods).
In OOP, computer programs are designed by making them out of objects that interact with one another. There are many OOP computer languages, but the most popular ones (e.g. Python) are class-based, meaning that objects are instances of classes.

In object-oriented programming, the static structure of data and functions is the primary concern, i.e. asking which methods are required to manipulate enclosed data, and what the connections between objects or classes should be.

Process-oriented programming (POP) is another programming paradigm, but where OOP is primarily concerned with the static structure of data and functions, POP is primarily concerned with how the processes in a system are structured, and how they communicate with each other. POP permits the design of large-scale applications that partially share common data sets. If OOP is more concerned with how objects relate to one another, POP is about how processes relate to one another. 

To design a system in a process-oriented way means thinking first about what processes will exist and how they will communicate. Considerations of whether processes are static or dynamic; whether processes are produced on request or serve a long-running purpose; and whether processes hold (or hold part of) shared state or are inherently concurrent should be taken into account. 

##What's polymorphism in OOP?
Polymorphism is a feature of Object-Oriented Programming. In Python, polymorphism describes how we can define methods in a child class that have the same name as the methods in the parent class. Essentially, a child class inherits all the attributes and methods of its parent class(es). In a child class, we can overwrite an inherited method to give different results; the method's name will remain the same, but what it does is different. This means the method is polymorphic i.e. it appears in more than one shape. 

A common example of polymorphism:

For integers, the + operator is used to perform arithmetic addition.
```
num1 = 1
num2 = 2
print(num1+num2)
```
Hence, the above program outputs 3.

Similarly, for string data types, + operator is used to perform concatenation.
```
str1 = "Python"
str2 = "Programming"
print(str1+" "+str2)
```
As a result, the above program outputs Python Programming.

##What's inheritance in OOP?
Inheritance is another key feature of Object-Oriented Programming, which helps with organisation and to avoid duplicate code. Inheritance describes how a child class automatically inherits the attributes and methods when it descends from a parent class.

Example syntax: 

```
class BaseClass:
    [Body of base class]

class DerivedClass(BaseClass):
    [Body of derived class]
```

The Derived class inherits features from the Base class, and new features can be added to it. This means code can be reused rather than repeated.

##If you had to make a program that could vote for the top three funniest people in the office, how would you do that? How would you make it possible to vote on those people?
There is some ambiguity in the question wording, so I have included a number of solutions.

The way the question is written sounds like the program itself would need to cast votes:

**AI**

For this, you'd need AI to create a program that would vote for the three funniest people.
The AI would have to take in a data set of things that you could ascertain funniness from, e.g. emails, Tweets, text messages. 
Funniness being a category that one cannot ascribe to oneself, and only exists in other people's opinions, you'd need to take a set of texts created by each office worker, and then analyse the reactions to said texts to ascertain funniness. You would then have to create a system that weighted certain features as comparatively funny or not, e.g. lots of reactions containing the crying-laughing emoji might suggest funniness, something with no reactions at all might be considered 'unfunny'.
For a program that could vote i.e. choose the three funniest people, ultimately it would select the three people who scored the highest on the funniness matrix.

If the question is to be interpreted as: how would you write a program that would enable a group to vote on the three funniest people in the office? There are a number of solutions. 

The complexity of these solutions, to some extent, depends on how you define the candidates that can be voted upon. Will the voter be presented with choices i.e. here are three (or more) people, vote between them? Or will the voter be writing in their own choice(s)? If so, would the voter be writing in just one name, or three names whose sequential order would be weighted?

**IF/ELIF STATEMENTS**

You'd have to start by working out who the candidates are.
You could do this by automatically entering the entire office as candidates, in which you'd need a collection containing each office worker's name/ID.
Each worker would have a vote counter, set at 0.

You could then allow people to vote by asking for user input, i.e. Enter the name of the person you think is funniest.
You could then write a series of if statements along the lines of:
```
if answer == 'Anna';
    anna_votes += 1
elif answer == 'Bill';
    bill_votes += 1
```
and so on.

**FOR LOOPS**

You could also start by asking people to nominate three people who they think are the funniest, and use the compiled list of names as your candidates and also your votes.
You could, presumably, do this by asking for user input, and then appending each name to a list e.g. votes_list.

e.g. 
```
votes_list = []
new_vote = input('Who do you think is the funniest? ')
votes_list.append(new_vote)
```

You could find out a selection of distinct candidate names by transforming the list into a set, which would remove duplicates. This set could be called candidate_names.

Then you could loop through the set, and for each element, you could count the instances of it in the original list votes_list. You could save these results in a dictionary, with the candidate name as the key, and then the count, a.k.a. the votes, as the value. You could then ascertain the three names with the highest values, who would, therefore, be the three funniest people in the office. 

**CLASSES**

You could define a class that, when instantiated, acts like a voting system. 
It would contain methods, which would allow a voter to cast a vote, have that vote recorded, and tally the total votes. Both if/elif statements and for loops could be used 
within these class methods. The class could be instantiated, then the methods for casting a vote and having that vote recorded would be called. Once everyone who needs to has cast their vote, then the vote tally method could be called, which would then supply the vote tally for each candidate and thus reveal the winner.

##What's the software development cycle?
The Software Development Life Cycle (also known as SDLC) is a set of steps used to create software applications. Each step is a specific development process, and the idea is that, by naming and organising these crucial parts of developing and making software, the process can be made more organised, efficient and easily monitored. 

The SDLC simply outlines each task required to put together a software application. This helps to reduce waste and increase the efficiency of the development process. Monitoring also ensures the project stays on track, and continues to be a feasible investment for the company.


The SDLC is typically divided into six to eight steps, as outlined below: 

1. **Planning**
* Evaluating the terms of the project e.g. calculating labour and material costs, timetable and target goals, creating the project’s teams and leadership structure.
* Stakeholder feedback
* Clearly defining scope and purpose

2. **Define Requirements**
* Part of the planning process
* Identifying and delimiting what the finished product must be able to do (and what is an optional extra)
* Defining any resource requirements e.g. specific tools/software/expertise needed

3. **Design and Prototyping**
* Modelling the way the application should work e.g. through:
* User interface
* The platforms on which the software will run, e.g. Apple, Android
* What language/programming paradigms it will be written in 
* Security
* Prototyping can be involved

4. **Software Development**
* Actually writing the code
* Writing documentation/FAQs/user manuals

5. **Testing**
* Unit tests
* Integration tests
* Functional tests
* End-to-end tests
* Acceptance testing
* Performance testing
* Smoke testing

6. **Deployment**
* Releasing software and updates to users
* Can be manual or automated

7. **Operations and Maintenance**
* Operating production software applications
* Monitoring system performance, 
* Making repairs and testing the application after any changes are made

Some project managers will combine, split, or omit steps, depending on the project’s scope. 

##What's the difference between agile and waterfall?
Agile and waterfall are two methodologies for completing projects. Agile is an iterative methodology that is cyclic and collaborative. Waterfall is also collaborative, but instead of being iterative, it is sequential: tasks are handled in a more linear process. 

Waterfall project management is a traditional model for developing engineering systems and is originally based on manufacturing and construction industry projects. When applied to software development, specialized tasks completed in one phase need to be reviewed and verified before moving to the next phase. It is a linear and sequential approach, where phases flow downward (waterfalls) to the next; the next only starting once the previous phase is complete. Waterfall is useful for well-defined projects: if the design work is done up front, then potential pitfalls and tangents can be identified early. However, Waterfall structures are fairly rigid, and do not necessarily reflect the ever-morphing shape of a collaborative tech project. Within a Waterfall planning structure, it’s hard to change direction halfway through.

Agile, on the other hand, includes all SDLC phases into each iteration. After several iterations, a new or updated product is released. Agile was established in 2001, created by 17 technology leaders. Encompassed within Agile are a range of frameworks and product delivery methods, such as Scrum, Lean, Six Sigma, and Kanban.
One of the great advantages of Agile is that it allows flexibility, with stakeholders able to observe and test the product in development very early on, rather than having to wait until a product is finished before being able to say that changes are required. This flexibility can be a double-edged sword, however, as shifting priorities may cause confusion if not communicated effectively.
In summary, Agile is a mindset to approaching projects which provides flexibility, while Waterfall is a predefined, sequential framework to follow.

##What is a reduced function used for?
A reduced function is used for reducing a list of items to a single cumulative value - this process is also known in mathematics as folding or reduction. It is useful for processing iterables without having to write out for loop(s). To reduce a function in Python, you use the `reduce()` function.

Python’s `reduce()` can be used on all iterables, and works as follows:
* Apply a function (or callable) to the first two items in an iterable and generate a partial result.
* Use that partial result, together with the third item in the iterable, to generate another partial result.
* Repeat the process until the iterable is exhausted and then return a single cumulative value.

`Reduce()` was originally built-in as a function, but for Python 3.0 it was moved to `functools.reduce()`. The introduction of built-in functions like `sum()`, `any()`, `all()`, `max()`, `min()`, and `len()` replace some of the need for `reduce()`, as they are more efficient, readable, and Python-appropriate ways of approaching common use cases, such as:
* Summing numeric values
* Multiplying numeric values
* Finding minimum/maximum value
* Checking if all values are true/a specific value is true

Because Python’s `reduce()` is written in C, its internal loop can be faster than an explicit Python for loop. Having said that, as Guido van Rossum—the inventor of Python—himself stated, a clean loop is often easier to follow as a coder. This is explicit in the Python documentation, which states: ‘Use functools.reduce() if you really need it; however, 99 percent of the time an explicit for loop is more readable.’

##How does merge sort work?
A merge sort uses a technique called ‘divide and conquer.’ The list is repeatedly divided into two, until all the elements are separated individually. Pairs of elements are then compared, placed into order and combined. The process is then repeated until the list is recompiled as a whole.

Consider an unsorted list of eight numbers that we want to sort in ascending order. That list would be split in half as many times as necessary in order to isolate each element. At this point, the elements are compared as pairs. This allows the lower number to be put at the start of the list, and the higher number to be put at the end of the list. Once two pairs of two have been sorted, they become a combined four-item list. The other half of the original list is sorted in the same way. We then compare two four-item lists, starting with the left-most number of both lists and asking which is lower. Once the lower number has been selected, the algorithm goes back to the two lists, and asks the same question again. This is done repeatedly until the algorithm has processed all the numbers across both the half-lists, and so you have a full list, fully sorted.

##Generators - Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop. What is the use case?

Generators are beloved by programmers as an elegant and more Pythonic way to make an iterator. One of the benefits of using an iterator is that an iterator saves memory space, because it doesn’t compute the value of all of the items when instantiated - they only compute the next value when you ask for it. This is known as lazy evaluation. 

The downside of iterators is that they can only be iterated over once. If you try to iterate over an iterator again, no value will be returned. It will behave like an empty list. Generators, however, circumvent this problem because they save the state of the function (whereas an iterator function would not). 

Typical functions use return statements, in which all the local variables are destroyed and the resulting value is returned. If the same function is called again later, the function will get an entirely new set of variables. 

Instead of using a return statement like a typical function, generators use a yield statement. Yield also returns a value, but it doesn’t discard the local variables like a return statement would have. Instead, the next time the generator function is called, execution continues from where it left off, with the same variable values it had before yielding.
 
Generators are good for calculating large sets of results (especially calculations involving loops) in which you might need to retrieve some or all of the results, or where you don’t want to automatically consecrate a load of memory to storing data. 
 
Another use for generators is to replace callbacks with iteration. Sometimes a function needs to carry out operations and then report back to whoever called it. Traditionally one might use a specific callback function on top of your worker function for this. Instead, you could make the worker function into a generator, which could then yield to report something. 
 
You can also use generators to create functions that can be interrupted, which would allow things like updates or running several jobs simultaneously (i.e. by alternating between them) while not using threads.

##Decorators - A page for useful (or potentially abusive?) decorator ideas. What is the return type of the decorator? 

Python decorators let you "wrap" a function with another function. This is useful because you may want to alter a function (after you have written it) to amend its functionality in certain situations; a decorator saves you having to rewrite the whole function, which could lead to errors elsewhere in a program, or falling foul of the SOLID programming principles. Essentially, decorators change how a function behaves, without needing to change the code inside them. Using them can help improve code readability.

To be specific, a decorator is a callable object that takes (an) object(s) and returns an object, although many people think of a decorator as ‘a function that takes a function and returns a function.’ In most cases, we want the object our decorator returns to mimic the function we decorated. This means that the object the decorator returns needs to be a function itself. 

**GOOD USE OF DECORATORS:**

Let’s say you have created some software, and then a client wants you to tack something onto it, e.g. caching, logging. If you changed your functions to incorporate caching, you could fall foul of the SOLID principles, e.g. single-responsibility and open-closed.
Using a decorator allows you to use your previously created code, and wrap it in another function that could improve or add to its functionality.

Decorators can be used for: 
* Annotation, i.e. you can label a function to determine which kind of tests it requires
* Registration i.e. if you wanted to create a central registry of all the functions in a program, you could create a registration function and then apply it to all the other functions in a program with a decorator, which would mean that they were all added to said registry
* Dispatch i.e. if you need to select between different implementations of the same abstract method based on certain parameters, like the type of input (as in, how the + function in Python works differently for integers and strings). 
* Verification i.e. you can write a decorator function that will verify the legitimacy of the inputs into the function it will be used to decorate, e.g. if a function requires only positive integers as inputs, a decorator function could check inputs before they are entered into said function.

**BAD USE OF DECORATORS**

When you apply a @decorator to a function the function itself is effectively lost from the namespace and there's no easy way to call it in its original un-decorated form. This might be a problem, especially in a reusable library-style piece of code, because when writing code, you can’t anticipate all the ways it might be used in the future. To solve this, Python provides a utility decorator called `functools.wraps`, that copies attributes like name and docstring from the wrapped function.



###Resources

https://www.youtube.com/watch?v=C2QfkDcQ5MU&t=602s
https://www.forecast.app/faqs/what-is-the-difference-between-agile-and-waterfall
https://project-management.com/agile-vs-waterfall/
https://www.aipm.com.au/blog/agile-vs-waterfall-whats-the-difference
https://www.toptal.com/elixir/process-oriented-programming-elixir-and-otp
https://phoenixnap.com/blog/software-development-life-cycle
https://www.bbc.co.uk/bitesize/guides/z7kkw6f/revision/10
https://timber.io/blog/decorators-in-python/
https://medium.com/swlh/decorators-in-python-why-and-how-to-use-them-and-write-your-own-c1da4ed9f3a9
https://news.ycombinator.com/item?id=16084238
https://github.com/hchasestevens/hchasestevens.github.io/blob/master/notebooks/the-decorators-they-wont-tell-you-about.ipynb
https://realpython.com/python-reduce-function/
https://docs.python.org/3/whatsnew/3.0.html
https://www.freecodecamp.org/news/how-and-why-you-should-use-python-generators-f6fb56650888/
https://stackoverflow.com/questions/102535/what-can-you-use-python-generator-functions-for
https://www.python.org/dev/peps/pep-0255/
https://medium.com/@ankurpan96/a-handy-validator-using-decorators-in-python-a8722da02fba
https://softwaremaniacs.org/blog/2012/07/09/when-to-use-decorators/
https://codewithoutrules.com/2017/08/10/python-decorators/
https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing
https://github.com/GrahamDumpleton/wrapt/blob/develop/blog/01-how-you-implemented-your-python-decorator-is-wrong.md


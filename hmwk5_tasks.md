# HOMEWORK WEEK 5-6

##TASK 1 (Agile Techniques)
###Question 1
Complete definitions for scrum-related key terminology provided below. 

**SCRUM CEREMONIES**
* **Product backlog refinement** - when the product owner and some/all of the team review items on the backlog to ensure the backlog contains the appropriate items, that they are prioritized, and that the items at the top of the backlog are ready for delivery.
* **Sprint planning** - before the scrum starts, there is a planning meeting to work out the best strategy for the sprint, i.e. which features to focus on first, how to split tasks and assign tasks to different team members, decide how to measure progress etc.
* **Daily scrum** - a daily stand-up meeting where members of the scrum team update each other on how they're doing, answering the following questions: 
  * What did I do yesterday? 
  * What am I going to do today? 
  * What is impeding my work?
* **Sprint review** - takes place at the end of the sprint, and is designed to gather feedback on what the team has completed. Also known as the demo, the sprint review is an opportunity for the team to showcase its work and to inspect the overall roadmap for the product
* **Sprint retrospective** - a recurring meeting held at the end of a sprint, used to discuss what went well during the previous sprint cycle, and what can be improved for the next sprint.

**SCRUM ROLES**
* **Scrum Master** - a team member who ensures the scrum framework is followed, keeps track of how everyone's doing and helps people to keep in line with the scrum plan
* **Product Owner** - a team member who represents the interests of the customer/client with regards to the scrum. They make sure the scrum keeps in line with what the customer might want (so engineers don't go off track or waste time on unwanted features), and prioritise the backlog
* **Development Team** - a group of people that work together to create software; if the dev team are using a scrum framework, then the dev team will include a scrum master. 

---
---

###Question 2
You are leading a development team that was given a task to create a new yoga booking system.

High level description of the system is as follows:
* It has a very simple interface to accept user input (bookings) and display classes information
* All bookings, appointments, schedules etc. should be stored in a SQL database.
* There is a ‘backend’ system that should be written in Python to handle the logic and manage the data flow.
* Your team has two weeks to build a simple prototype that will be shown to the client to seek their feedback and discuss further enhancements.

Task
* Break this task into smaller stories (chunks of work) for the team to work on.
* Assume that one person works on one task.
* Mark tasks that can be worked on in parallel and perhaps those that need to be worked on in particular order.

---

#####FIRST TASK - Build SQL database. 

Tables to build include: 

* master schedule; 
* instructors; 
* a table for each yoga class; 
* customer details table.

If possible, populate tables:
* instructors, with instructor names and contact details
* master schedule, with times and dates of classes
* each yoga class table should have a constraint on the place number column of the maximum number of attendees, i.e. if only 10 people can attend a yoga class, then there should be a constraint meaning that the place numbers can only go up to 10

####SUBSEQUENT TASKS (CAN BE CARRIED OUT IN PARALLEL, AFTER DATABASE IS BUILT)

####TASK A - Build schedule/availability view for customers
* build connection between Python backend and SQL DB
* retrieve schedule info from SQL DB
* display this info to the customer
* allow customer to filter schedule view by: day, time, instructor, type of yoga, classes with availability

####TASK B - Build 'make a booking' function for customers
* build connection between Python backend and SQL DB
* allow customer to select the class they would like to book
* allow customer to enter their name and contact details
* update class table in DB with customer name, and subsequently reduce capacity in said class in main schedule table
* update customer details table with customer name and contact details
* print confirmation message for consumer

####SUBSEQUENT TASKS (TO BE DONE AFTER TASKS 1, A AND B)

####TASK C - Maintenance of DB
* check tables in DB - no duplicate data or inaccurate records
* check dependencies

---
####COMPONENTS AND TOOLS TO BE USED
* SQL and an SQL editor e.g. Workbench
* Python and a Python editor e.g. PyCharm
* Python module - MySQL Connector
* Python module - unittest

---
---

##TASK 2 (SQL)

###Question 1
Design a cinema booking system. Think how you would approach the problem and what are potential ways of solving it? 
You do not need to write actual code, but describe the high-level approach. 

Draw a list of key requirements:
* What are your main considerations?
* What would be your common or biggest problems?
* What components or tools would you potentially use?
* You are welcome to draw a diagram (a very simple one) for the process ﬂow to explain how it is going to work.

---

A cinema booking system needs to:
display different films and what times they're showing
allow tickets to be booked. The user interface should allow users to see the schedule of what films are showing when; 
filter by film and date; book tickets for available shows;
put in your user details and pay for tickets; and apply members' discounts. 
There should be a database that stores key information such as film times, capacity of screens, and customer details.

###Jobs to be done

#### Database design

I would design a database in MySQL, which would have the following tables:
* a table for each film, listing title, running time, synopsis, age rating, top-starring cast, and screening times
* a table with the capacity of the different screen rooms in the cinema
* a table that shows the schedule of the films' showing times for the week ahead
* a table for customer names and details, with a column denoting whether they are loyalty members or not
* a table for each customer showing each film they've been to see
* a table for members, showing their membership number and when they started being members

### User interface design
* the customer should be able to view film screening times, in a view that allows them to see every film currently being shown at the cinema. This would require a call to the database by the customer, and some code to make sure the information displays in a legible way. This would also require the generation of hyperlinks for each film
* once they have selected a film they want to see, they should be able to click on it, and find out more info, and see specific screening times (only ones where there are still available seats). This would require a call to the database (or potentially an API if there is one for film information) to supply basic information about the film and the film screening times
* from there, they should be able to select a film screening, and reserve the number of tickets they would like. This would require designing places for user input so that they can select their seats, the number of tickets, and display the prices for each e.g. adults/children/concessions.
* once the tickets have been selected, the booking page should give a summation of the order to be processed, showing the number of tickets, the price, any booking fees and the total price. This requires a simple maths program summing it up.
* when making the booking, customers must enter their name and card details, and potentially start an account which will track what films they've watched and save them time in future checkouts. This would require design of spaces for user inputs, a safe database that can take customer details, a secure connection to an online payment platform.
* there should be a message on booking pages for age-rated films that IDs will be checked/underage people will be turned away. This requires a program to show this conditional message only when films are age-rated.
* members should be able to enter their membership number for their members' discounts. This would require a call to the members table in the database to check the membership code, and if successful, the application of a discount, using a mathematical program. 
* once that booking has gone through, the customer should get a confirmation message on screen and sent to them via email, and also the capacity for each screen must be decreased accordingly. This would require firstly, the design of a confirmation message that pops up when a transaction is successful. It would also require triggering an automated email, presumably by calling the database and retrieving the email address of the customer. It would also require updating the capacity field for the relevant screening, and if the screening is full, greying out that screening time and displaying SOLD OUT next to it. 

###Main considerations:
making sure that film screening times are accurate and easy to read
taking customer details and storing them safely

###Biggest problems:
keeping customer details safe
making sure that customers can't book tickets for sold-out screenings

###Components or tools:
* Python and an editor
* MySQL and an editor
* a MySQL database
* unittest module
* an API with cinema film information 



"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""

# import random 

# class CFGStudent:

#     def __init__(self, fname, surname, age, email, student_id=None):
#         self.fname = fname
#         self.surname = surname
#         self.age = age
#         self.email = email
#         self.student_id = student_id

#         if not self.student_id:
#             self.student_id = CFGStudent.generate_id()

#     @staticmethod
#     def generate_id():
#         # 'your code goes here'
#         # 'create a random new id, which is any number between 1,000 and 10,000'
#         # 'return id as a string'
#         # "Example '8754' "
#         student_id = random.randint(1000, 10000)
#         student_id = str(student_id)
#         return student_id

#     def get_id(self):
#         # 'your code goes here'
#         # 'fetch student id'
#         return self.student_id

#     def get_fullname(self):
#         # "Expected outcome should be 'Name Surname' "
#         # 'your code goes here'
#         fullname = f"{self.fname} {self.surname}"
#         return fullname


# class NanoStudent(CFGStudent):

#     def __init__(self, fname, surname, age, email, specialization, course_grades={}, student_id=None):
#         self.fname = fname
#         self.surname = surname
#         self.age = age
#         self.email = email
#         self.specialization = specialization
#         self.course_grades = course_grades
        
#         self.student_id = student_id

#         if not self.student_id:
#             self.student_id = CFGStudent.generate_id()

#     @staticmethod
#     def generate_id():
#         # 'your code goes here'
#         # 'create a random new id, which is a word NANO followed by any number between 1,000 and 10,000'
#         # 'return id as a string'
#         # "Example '8754' "
#         id_num = str(random.randint(1000, 10000))
#         student_id = ("NANO" + id_num)
#         return student_id

#     def add_new_grade(self, subject=str, mark=int):
#         # 'your code goes here'
#         # 'update course_grades container'
#         # "Example: pass in a task name and its grade, so that both are added to course_grades"

#         # subject, mark = {key: value}
#         self.course_grades.update({subject:mark})
#         return self.course_grades       

#     def get_course_grades(self):
#         # 'your code goes here'
#         # 'fetch course grades container and its values'
#         return self.course_grades



############################################

# Example run

# s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
# print(s.get_fullname())
# # returns 'Anna Smith'
# print(s.student_id)
# # returns '3868' or some other random number

# cfg_s = NanoStudent('Software', fname='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
# cfg_s = NanoStudent('Mia', 'Papandopulu', 20, 'mia@mail.com', 'Software')

# print(cfg_s.get_fullname())
# # returns 'Mia Papandopulu'
# print(cfg_s.get_id())
# # returns 'NANO6180' or some other random number

# cfg_s.add_new_grade('theory', 95)
# cfg_s.add_new_grade('project', 78)
# print(cfg_s.get_course_grades())
# # returns {'theory': 95, 'project': 78}



"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""

# def even_fibonacci_sum(index_limit):
# # an empty list to put fibonacci numbers in
#     fibonacci_list = []

# # a function to return the nth fibonacci number
#     def get_fibonacci(n):
#         if n < 0:
#             print("Incorrect input")
#         elif n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         elif n == 2:
#             return 1
#         else:
#             return get_fibonacci(n-1)+get_fibonacci(n-2)

# # calculating the fibonacci numbers up to an index limit
#     for i in range(index_limit):
#         j = get_fibonacci(i)
#         fibonacci_list.append(j)

#     # print("The Fibonacci sequence for the given index limit of {} is {}".format(index_limit, fibonacci_list))

# #an empty list for all the even numbers    
#     fibonacci_even_nums = []

# # working out which numbers are even and then adding it to the even numbers list
#     for k in fibonacci_list:
#         if k % 2 == 0:
#             fibonacci_even_nums.append(k)
#     # print("The even numbers are: {}".format(fibonacci_even_nums))

#  # getting the sum of the even numbers   
#     even_nums_sum = sum(fibonacci_even_nums)

#     return("The sum of the even numbers is: {}".format(even_nums_sum))


# #### TESTS ####

# print(even_fibonacci_sum(10))  # should be 44
# print(even_fibonacci_sum(15))  # should be 188
# print(even_fibonacci_sum(1))   # should be 0





"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""

def is_valid_subsequence(array, sequence):
# if the first value of the sequence IS in the array, but is too close to the end for
# the other values to follow it, then it can be filtered out
    len_array = len(array)
    len_sequence = len(sequence)

# if the first value of the sequence is not in the array, then it can be filtered out
    if sequence[0] not in array:
        return "False because the first num in the sequence isn't in the array"

# if all the numbers in the sequence are in the array, it's theoretically possible that
# the sequence is a valid subsequence, but further checks would be needed
    else:
        for i in sequence:
            if i not in array:
                return("False because one of the numbers in the sequence isn't in the array")
                array.remove(i)
        
        if array == sequence:
            return True
    
# you could go through the array, comparing each number to the sequence, and then pop 
# any numbers that aren't in the sequence, then compare the amended list with the sequence
# and see if they are the same

    # for i in sequence:
    #     if i not in array:
    #         array.remove(i)
    
    # if array == sequence:
    #     return True




#### TESTS ####

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE



"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)
"""

"""

The code could be improved in the following ways:

To follow the Single Responsibility Principle (SRP) from the SOLID principles, 
a class should only have one responsibility i.e. reason to change. The Employee class as 
it now stands has more than one responsibility; not only are we instantiating
an employee, but we are also adding/removing an employee to a database
i.e. employee DB management, and also printing an employee report. This is 
falling foul of the SRP, and so ideally you would split the class up into several smaller
classes that each have one responsibility. 
You could have one class Employee that instantiates the employee and updates their 
attributes i.e. with the methods update_department(), update_status(). Then you would have a separate class
that saves all employees i.e. class EmployeeDB, which would take the attribute db_engine from 
class Employee. Class EmployeeDB would contain the methods save_employee(), remove_employee(). 
And then you could have another class for WorkforceReport which would 
have the method print_employee_report(). 

Creating a separate class for EmployeeDB would help the written code conform with the 
Interface Segregation Principle (ISP) and the Dependency Inversion Principle (DIP),
because as the code is currently written, any instantiation of the class Employee would have 
loads of different methods and attributes that it might not necessarily need. 
Creating the EmployeeDB class is like creating an interface that both the high-level
class of Employee and also the low-level class of WorkforceReport can use, without the two
having to be coupled too closely together (which might create problems down the line, should
either of those classes need to be adjusted).

"""





"""
TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self, total_items={}, total_price=0, discount=0):
        self.total_items = total_items
        self.total_price = total_price
        self.discount = discount

    def add_item(self, new_item_name, new_item_price):
        self.total_items.update({new_item_name: new_item_price})

    def remove_item(self, removed_item):
        self.total_items.pop(removed_item)

    def get_total(self):
        prices = self.total_items.values()
        self.total_price = sum(prices)
        print("The total price is: {:.2f}".format(self.total_price))

    def apply_discount(self, discount):
        self.discount = discount/100
        self.discount = self.total_price * self.discount
        self.total_price -= self.discount
        print("The new price, once discount of {}% has been added, is £{:.2f}".format(discount, self.total_price))

    def show_items(self):
        if len(self.total_items) > 0:
            print(self.total_items)
        else:
            print("Your basket is empty.")

    def reset_register(self):
        self.total_items.clear()


# shopping_list = {
#     "onions": 2,
#     "carrots": 3,
#     "bread": 1
# }

daisy_shop = CashRegister()
daisy_shop.add_item('coconut', 5)
daisy_shop.show_items()
daisy_shop.add_item('carrots', 6)
daisy_shop.show_items()
daisy_shop.add_item('oat milk', 2)
daisy_shop.show_items()
daisy_shop.remove_item('oat milk')
daisy_shop.show_items()
daisy_shop.get_total()
daisy_shop.apply_discount(10)

daisy_shop.reset_register()
daisy_shop.show_items()




"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

"""


# class Student:
#
#     def __init__(self, name, age, id):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.subjects = dict()
#
#
# class SoftwareStudent(Student):
#     # new class that inherits from parent class Student
#     def add_new_subject(self, subject_name, subject_grade):
#         # add new key-value pair to subjects dictionary
#         self.subjects.update({subject_name: subject_grade})
#
#     def remove_subject(self, subject_name):
#         # remove key-value pair from subjects dictionary
#         self.subjects.pop(subject_name)
#
#     def view_all_subjects(self):
#         # print out the subjects dictionary
#         print(self.subjects)
#
#     def average_grade(self):
#         # average of all the values in the subjects dictionary
#         marks_list = self.subjects.values()
#         average_grade = sum(marks_list) / len(marks_list)
#         print(f" {self.name}'s average grade is {average_grade}")
#         return average_grade







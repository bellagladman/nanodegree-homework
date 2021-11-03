"""
Write a function that takes in a non-empty array of distinct integers
and an integer representing a target sum. If any two numbers in the
input array sum up to the target sum, the function should return
them in an array, in any order. If no to numbers sum up to the target
sum, the function should return an empty array.
Note that the target sum has to be obtained by summing two
different integers in the array. You cannot add a single integer to
itself in order to obtain the target sum.
You can assume that there will be at most one pair of numbers
summing up to the target sum.

Sample Input:
numbers = [3, 5, -4 ,8, 11, 1, -1, 6]
target_sum = 10

Sample Output:
[-1, 11]
the numbers can be in any order, it does not matter.
"""

"""
Assumptions: We are only looking for one pair of numbers that makes the target sum
(even though there may be more than one pair)
Constraints: You can't add the same number to itself to get the target sum
"""

my_array = [3, 5, -4, 8, 11, 1, -1, 6]
my_target_sum = 10


def calc_target_sum(array, target_sum):
    new_array = []
    empty_array = []

    for first_number in array:
        for second_number in array:
            if first_number != second_number and first_number + second_number == target_sum:
                new_array.append(first_number)
                new_array.append(second_number)
                return new_array
    else:
        return empty_array


print(calc_target_sum(my_array, my_target_sum))


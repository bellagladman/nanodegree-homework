"""
SEARCH IN MATRIX
--------

You are give a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

EXAMPLE OUTPUT

result = [3,3]

"""

# I managed to write functions that did the required outputs but didn't manage to combine them
# I spent about eight hours on these (and attempts to combine them)
# Would appreciate feedback on this!

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target = 100

# this works to get the position, but not for returning [-1, -1] if the target isn't there
def count_through_matrix(matrix, target):
    row_count = 0
    for row in matrix:
        item_count = 0
        row_count += 1
        # print("Row count: {}".format(row_count))
        for item in row:
            item_count += 1
            # print("Item count: {}".format(item_count))
            if item == target:
                return print("[{}, {}]".format(row_count, item_count))
    return print("[-1, -1]")

# count_through_matrix(matrix, target)


# this works to check if the item is there and if not returns [-1,-1]
def search_in_matrix(matrix, target):
    for item in matrix:
        if target not in item:
            continue
        else:
            print("[-1, -1]")

# search_in_matrix(matrix, target)

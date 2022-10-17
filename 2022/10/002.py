# DAILY CODING PROBLEM FOR 10/16/2022

# Given an array of integers, 
# return a new array such that each element at index i of the new array 
# is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def function1(array: list) -> list:
    outputarray = []
    
    for i in range(len(array)):
        product = helper1(array[0:i]) * helper1(array[i+1:])
        outputarray.append(int(product))
    return outputarray

def helper1(array: list) -> int:
    product = 1
    for digit in array:
        product *= digit
    return product

# ALTERNATE SOLUTION

# def function2(array: list) -> list:
#     outputarray = []
#     product = 1
#     for digit in array:
#         product *= digit

#     for i in range(len(array)):
#         outputarray.append(int(product / array[i]))
#     return outputarray

if __name__ == '__main__':
    array1 = [1, 2, 3, 4, 5]
    array2 = [3, 2, 1]
    print(function1(array1))
    print(function1(array2))

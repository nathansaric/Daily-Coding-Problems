# DAILY CODING PROBLEM FOR 10/18/2022

# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

def function1(array: list) -> int:
    if len(array) < 1:
        return None
    
    maximum = len(array)
    minimum = min(array)

    for digit in range(1, maximum + 1):
        if digit not in array:
            minimum = digit
            break
        if minimum == min(array):
            minimum = maximum + 1
    return minimum

if __name__ == '__main__':
    array1 = [3, 4, -1, 1]
    array2 = [1, 2, 0]
    print(function1(array1))
    print(function1(array2))

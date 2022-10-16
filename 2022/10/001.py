# DAILY CODING PROBLEM FOR 10/15/2022

# Given a list of numbers and a number k, 
# return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def function1(list: list, k: int) -> bool:
    set = []
    for digit in list:
        set.append(digit)
        print(set)
        if (k - digit) in set and (k-digit) != set[-1]:
            return True
    return False

if __name__ == '__main__':
    list = [10, 15, 3, 7]
    k = 17
    print(function1(list, k))

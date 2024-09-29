"""
A function that calculate the sum of all elements from an array.
"""
def array_sum(arr):
    """
    Calculate the sum of all elements in the array.
    Params
        :dtype arr: A list of integers.
        :rtype: integers.
    """
    total = 0
    for num in arr:
        total += num
    return total

# Test the function
array_list = [1, 2, 3, 4, 5]
print(array_sum(array_list))

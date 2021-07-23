"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    # Your code goes here
    temp=len(input_array)
    low=0
    high=temp-1
    mid=low+high//2

    l1=input_array[:mid]
    l2=input_array[mid:]

    if(value<input_array[mid]):
        if value in l1:
            return input_array.index(value)
        else:
            return -1
    else:
        if value in l2:
            return input_array.index(value)
        else:
            return -1


    pass

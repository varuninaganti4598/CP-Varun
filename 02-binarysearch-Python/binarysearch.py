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

# def binary_search(input_array, value):
#     # Your code goes here
#     temp=len(input_array)
#     low=0
#     high=temp-1
#     mid=low+high//2

#     l1=input_array[:mid]
#     l2=input_array[mid:]

#     if(value<input_array[mid]):
#         if value in l1:
#             return input_array.index(value)
#         else:
#             return -1
#     else:
#         if value in l2:
#             return input_array.index(value)
#         else:
#             return -1


#     pass

def isPrime(n):
    if(n==2):
        return True
    else:
        for i in range(2,int(n/2)+1):
            if(n%i==0):
                return False
    return True


def palindrome(n):
    copy=n
    a=0
    if(n<10):
        return True
    while(n>0):
        rem=n%10
        a=(a*10)+rem
        n=n//10
    if(copy==a):
        return True
    else:
        return False


def isPalindromicPrime(n):

    if(isPrime(n) and palindrome(n)):
        return True
    else:
        return False
    
assert (isPalindromicPrime(2) == True)
assert (isPalindromicPrime(10) == False)
assert (isPalindromicPrime(104) == False)
assert (isPalindromicPrime(235) == False)
assert (isPalindromicPrime(131) == True)
assert (isPalindromicPrime(900) == False)
assert (isPalindromicPrime(101) == True)
assert (isPalindromicPrime(383) == True)
assert (isPalindromicPrime(373) == True)
assert (isPalindromicPrime(121) == False)
print("All test cases passed... :-)")

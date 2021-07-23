# isPalindromicPrime() 
# Write a function isPalindromicPrime that takes a value n as 
# a parameter and returns True if the given n is a palindrome and prime and False otherwise.
# assert (isPalindromicPrime(2) == True)
# assert (isPalindromicPrime(10) == False)
# assert (isPalindromicPrime(104) == False)
# assert (isPalindromicPrime(235) == False)
# assert (isPalindromicPrime(131) == True)
# assert (isPalindromicPrime(900) == False)
# assert (isPalindromicPrime(101) == True)
# assert (isPalindromicPrime(383) == True)
# assert (isPalindromicPrime(373) == True)
# assert (isPalindromicPrime(121) == False)
# print("All test cases passed... :-)")


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


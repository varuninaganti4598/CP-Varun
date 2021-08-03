# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

def isPrime(n):
    if(n==0):
        return False
    if(n==2):
        return True
    else:
        for i in range(2,int(n/2)+1):
            if(n%i==0):
                return False
    return True

def check(n):
    # if(isPrime(n)):
        sum=0
        while(1):
            a=n%10
            sum+=a*a
            n=n//10
            if(n==0):
                if(sum<10):
                    return sum
                n=sum
                sum=0
    # else:
    #     return False



def ishappyprimenumber(n):
    # Your code goes here
    res=check(n)
    print(res)

    if(res==1 and isPrime(n)):
        return True
    elif(res<10):
        return False

# print(ishappyprimenumber(833))
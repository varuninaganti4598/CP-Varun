# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.
def check(n,v):
	c=0
	while(n>0):
		if(n%10==v):
			c+=1
		n=n//10
	return c

def mostfrequentdigit(n):
	# your code goes here
	max=0
	r=0
	for i in range(10):
		result=check(n,i)
		if(result>max):
				max=result
				r=i
		if(result==max):
				if(r<i):
						r=r
				else:
    					r=i
    		
	return r
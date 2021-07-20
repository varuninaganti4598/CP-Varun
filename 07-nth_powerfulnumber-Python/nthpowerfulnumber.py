# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
import math
def prime(n):
		if(n==2):
				return True
		else:
    			for i in range(2,int(n/2)+1):
    					if(n%i==0):
    							return False
		return True



def check(n):
		if(n==1):
			return True
		else:
			count=0
			count1=0
			for i in range(2,int(n/2)+1):
						if(n%i==0 and prime(i)):
								count+=1
								if(n%(i*i)==0):
									count1+=1
						print(count)
						print(count1)
			if(count==0 or count1==0):
					return False
			elif(count==count1):
					return True
		return False
	
def nthpowerfulnumber(n):
	# Your code goes here
	found=1
	guess=1
	count=0
	while(found):
		if(check(guess)):
			if(n==count):
						found=0
						return guess
			guess+=1
			count+=1
		else:
			guess+=1
	

    								

    		
    		





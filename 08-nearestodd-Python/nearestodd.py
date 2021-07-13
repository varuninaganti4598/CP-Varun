# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.

def fun_nearestodd(n):
	a=int(n)
	b=a-1
	c=a+1
	if(b%2==0 and c%2==0):
		return int(a)
	elif(b%2!=0):
		if(c%2!=0):
			if(n-b<c-n):
					return int(b)
			elif(n-b==c-n):
    				return int(b)
			else:
					return int(c)




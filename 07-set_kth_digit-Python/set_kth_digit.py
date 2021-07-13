# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 

def check(n,k,d):
	emp=[]
	if(n>0):
		while(n>0):
			a=n%10
			emp.append(a)
			n=n//10
		print(emp)
	if(k>=len(emp)):
		emp.append(d)
		result=emp[::-1]
		print(result)
		e=""
		for i in range(len(emp)):
			e+=str(result[i])
		return int(e)
	else:
		emp[k]=d
		result=emp[::-1]
		e=""
		for i in range(len(emp)):
			e+=str(result[i])
		return int(e)

def fun_set_kth_digit(n, k, d):
	if(n<0):
		n=abs(n)
		a=(check(n,k,d))
		return -abs(a)
	else:
		return check(n,k,d)





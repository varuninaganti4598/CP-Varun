# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).




def nthpronicnumber(n):
	# Your code goes here
	if(n==0):
    		return 0
	else:
		a=n+1
		res=n*a
		return res




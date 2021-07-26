# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
    # your code goes here
	if(len(a)==1 or len(a)==0):
						return True
	else:
		n=len(a)
		m=min(a)
		maxi=max(a)
		c=0
		for i in range(n):
				if(type(a[i])!=int ):
						return False
				if(m==maxi):
    						return True
				if(a[0]==m):
					if(a[i-1]<a[i]):
						c+=1
				if(a[0]==maxi):
					if(a[i-1]>a[i]):
    						c+=1
		if(c==len(a)-1):
				return True
		else:
				return False
						

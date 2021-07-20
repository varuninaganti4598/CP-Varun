# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.


def fun_recursions_alternatingsum(l): 
	length=len(l)
	sum=0
	odd=0
	i=0
	a=l[i]
	sum+=l[i]
	l.remove(l[i])
	i+=1
	fun_recursions_alternatingsum(l)
	
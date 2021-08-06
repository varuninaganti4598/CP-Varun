# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]




def getallpermutations(x,i,l):
	# Your code goes here
	if(i==l):
    		return(''.join(x))
	else:
			for j in range(i,l):
					x[i],x[j]=x[j],x[i]
					getallpermutations(x,i+1,l)
					x[i],x[j]=x[j],x[i]


# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def diagonalCheck(a,rows,cols):
	d1=0
	d2=0
	for i in range(rows):
		d1+=a[i][i]
		d2+=a[i][-1 - i]
						
	if(d1==d2):
    		return True
	else:
    		return False
		

def ismostlymagicsquare(a):
	# Your code goes here
	rows=len(a)
	cols=len(a[0])
	rowsum=0
	colsum=0
	l=[]
	if(rows==1):
    		return True
	elif(diagonalCheck):
		for i in range(rows):
			for j in range(cols):
				rowsum+=a[i][j]
				colsum+=a[j][i]
				# print(sum)
			l.append(rowsum)
			l.append(colsum)
			rowsum=0
			colsum=0
		final=len(set(l))
		# print(len(final))
		if(final==1):
			return True
		else:
			return False
			
		
	else:
    		return False
	
    				
	
# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

import math
def distance(x1,y1,x2,y2):
    dis=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return dis

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	a1=distance(x1,y1,x2,y2)**2
	a2=distance(x2,y2,x3,y3)**2
	a3=distance(x3,y3,x1,y1)**2

	if(math.isclose(a1+a2,a3) or math.isclose(a2+a3,a1) or math.isclose(a3+a1,a2)):
		return True
	else:
		return False

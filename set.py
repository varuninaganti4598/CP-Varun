# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]
import math
def limitedPowerSet(n, k):
    # Your code goes here...
    a = (int) (math.pow(2,k));
    counter = 0;
    j = 0;
    r=[]

    for counter in range(0, a):
        for j in range(0,k):

            if((counter & (1 << j)) > 0):
                r.append(set[j])
    return r

assert limitedPowerSet(5,7) == [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]
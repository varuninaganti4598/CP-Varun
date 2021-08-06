# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]

def limitedPowerSet(n, k):
    # Your code goes here...
    l=[]
    res=[{}]
    for i in range(1,n+1):
        l.append(i)
        res.append(i)
    
    for j in range(1,1<<n):
        result=[]
        result.append({l[m] for m in range(n) if(j&(1<<m))})
        for k in result:
            if k not in res:
                res.append(k)

    return res[:k]

    
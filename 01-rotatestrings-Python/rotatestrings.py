# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	res=''

	if(n>=0 and n<len(s)):
		res+=s[n:]+s[:n]

	else:
		if(n>len(s)):
			res+=s[len(s)+1-n:]+s[0:len(s)+1-n]	
		# print(s[:len(s)-n])
		# print(s[len(s)-n:])
		else:
			n=abs(n)
			res+=s[len(s)-n:]+s[0:len(s)-n]

	return res


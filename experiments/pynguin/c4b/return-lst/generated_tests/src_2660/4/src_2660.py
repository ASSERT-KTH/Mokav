def func(*args):
	ret_values = []
	
	
	def sumOfDigits(s):
	    sum = 0
	    s = str(s)
	    for i in range(len(s)):
	        sum = (sum + int(s[i]))
	    return sum
	
	def binSearch(s, l, u):
	    if ((((((l + u) // 2) + 1) - sumOfDigits((((l + u) // 2) + 1))) >= s) and ((((l + u) // 2) - sumOfDigits(((l + u) // 2))) < s)):
	        return ((l + u) // 2)
	    if ((((l + u) // 2) - sumOfDigits(((l + u) // 2))) < s):
	        return binSearch(s, (((l + u) // 2) + 1), u)
	    if ((((l + u) // 2) - sumOfDigits(((l + u) // 2))) >= s):
	        return binSearch(s, l, (((l + u) // 2) - 1))
	(n, s) = args[0].strip().split(' ')
	s = int(s)
	if ((int(n) - sumOfDigits(n)) < s):
	    ret_values.append(0)
	else:
	    d = binSearch(s, 1, int(n))
	    ret_values.append((int(n) - d))

	return ret_values

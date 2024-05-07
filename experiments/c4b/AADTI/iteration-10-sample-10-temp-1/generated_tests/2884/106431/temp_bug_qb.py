def original_func(*args):
	global_list = []
	
	
	def sumOfDigits(s):
	    sum = 0
	    s = str(s)
	    for i in range(len(s)):
	        sum = (sum + int(s[i]))
	    return sum
	
	def binSearch(s, l, u):
	    if (((((l + u) // 2) + 1) - sumOfDigits((((l + u) // 2) + 1))) >= s):
	        return ((l + u) // 2)
	    if (((((l + u) // 2) + 1) - sumOfDigits((((l + u) // 2) + 1))) < s):
	        return binSearch(s, (((l + u) // 2) + 1), u)
	(n, s) = args[0].strip().split(' ')
	s = int(s)
	if ((int(n) - sumOfDigits(n)) < s):
	    global_list.append(0)
	else:
	    d = binSearch(s, 1, int(n))
	    global_list.append((int(n) - d))
	return global_list
def func(*args):
	ret_values = []
	
	
	def numdig(n):
	    if (n == 0):
	        return 1
	    else:
	        ans = 0
	        while (n > 0):
	            ans += 1
	            n = (n // 10)
	        return ans
	s1 = str(args[0])
	h = int(s1[0:2])
	m = int(s1[3:])
	n = int(args[1])
	m1 = ((m + n) % 60)
	if (numdig(m1) == 1):
	    m2 = ('0' + str(m1))
	else:
	    m2 = str(m1)
	if ((m + n) >= 60):
	    h1 = ((h + ((m + n) // 60)) % 24)
	else:
	    h1 = h
	if (numdig(h1) == 1):
	    h2 = ('0' + str(h1))
	else:
	    h2 = str(h1)
	ret_values.append(((h2 + ':') + m2))

	return ret_values

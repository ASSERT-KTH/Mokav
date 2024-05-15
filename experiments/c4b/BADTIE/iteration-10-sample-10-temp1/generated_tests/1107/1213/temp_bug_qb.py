def original_func(*args):
	global_list = []
	
	(a, b, n) = args[0].split()
	a = int(a)
	b = int(b)
	n = int(n)
	count = 1
	
	def gcd(a, b):
	    if (b == 0):
	        return a
	    return gcd(b, (a % b))
	while (n > (- 1)):
	    x = gcd(a, n)
	    if (n >= x):
	        n = (n - x)
	    else:
	        conut = 1
	        break
	    x = gcd(b, n)
	    if (n >= x):
	        n = (n - x)
	    else:
	        count = 2
	        break
	    global_list.append(n)
	global_list.append(count)
	if (count == 1):
	    global_list.append('1')
	else:
	    global_list.append('0')
	return global_list
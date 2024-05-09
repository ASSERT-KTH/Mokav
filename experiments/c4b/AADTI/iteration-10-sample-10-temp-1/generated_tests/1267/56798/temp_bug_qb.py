def original_func(*args):
	global_list = []
	
	n = int(args[0])
	z = args[1]
	x = int(z)
	
	def half(z, n):
	    x = 0
	    for i in range((n // 2)):
	        x = (x + int(z[i]))
	    return x
	
	def sd(x):
	    a = 0
	    while (x > 0):
	        b = int((x % 10))
	        if ((b != 4) and (b != 7)):
	            return (- 10000000000000)
	        a = (a + b)
	        x = (x // 10)
	    return a
	if (half(z, n) == (sd(x) // 2)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list
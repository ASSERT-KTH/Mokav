def patched_func(*args):
	global_list = []
	
	
	def kasra(n):
	    m = 0
	    a = 0
	    while (n != 0):
	        y = (n % 10)
	        n = (n // 10)
	        if (y != 0):
	            m = ((m * 10) + y)
	    while (m != 0):
	        t = (m % 10)
	        m = (m // 10)
	        a = ((a * 10) + t)
	    return a
	a = int(args[0])
	b = int(args[1])
	if (kasra((a + b)) == (kasra(a) + kasra(b))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list
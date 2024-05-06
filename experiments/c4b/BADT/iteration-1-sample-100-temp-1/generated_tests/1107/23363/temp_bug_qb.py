def original_func(*args):
	global_list = []
	
	
	def gcd(a, b):
	    while ((a != 0) and (b != 0)):
	        if (a > b):
	            a = (a % b)
	        else:
	            b = (b % a)
	    return (a + b)
	(a, b, c) = map(int, args[0].split(' '))
	tern = a
	while (c > 0):
	    c = (c - gcd(tern, c))
	    if (tern == a):
	        tern = b
	    else:
	        tern = a
	if (tern == a):
	    global_list.append(1)
	else:
	    global_list.append(0)
	return global_list
def func(*args):
	ret_values = []
	
	
	def gcd(a, b):
	    while ((a != 0) and (b != 0)):
	        if (a > b):
	            a = (a % b)
	        else:
	            b = (b % a)
	    return (a + b)
	(a, b, c) = map(int, args[0].split(' '))
	t = 0
	while (c > 0):
	    if (t == 0):
	        c = (c - gcd(a, c))
	        t = 1
	    else:
	        c = (c - gcd(b, c))
	        t = 0
	if (t == 1):
	    if (c == 0):
	        ret_values.append(0)
	    else:
	        ret_values.append(1)
	elif (c == 0):
	    ret_values.append(1)
	else:
	    ret_values.append(0)

	return ret_values

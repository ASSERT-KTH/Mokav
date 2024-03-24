def func(*args):
	ret_values = []
	
	
	def bmm(a, b):
	    if (a == 0):
	        return b
	    elif (b == 0):
	        return a
	    if (a == b):
	        return a
	    elif (a > b):
	        z = 0
	        for i in range(b, 0, (- 1)):
	            if (((a % i) == 0) and ((b % i) == 0)):
	                z = i
	                break
	        return z
	    elif (a < b):
	        z = 0
	        for i in range(a, 0, (- 1)):
	            if (((a % i) == 0) and ((b % i) == 0)):
	                z = i
	                break
	        return z
	(a, b, n) = [int(i) for i in args[0].split()]
	z = n
	f = (- 1)
	while (f == (- 1)):
	    if (bmm(a, z) <= z):
	        z = (z - bmm(a, z))
	    else:
	        f = 1
	        break
	    if (bmm(b, z) <= z):
	        z = (z - bmm(b, z))
	    else:
	        f = 0
	        break
	ret_values.append(f)

	return ret_values

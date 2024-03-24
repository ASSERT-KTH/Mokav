def func(*args):
	ret_values = []
	
	
	def gcd(a, b):
	    while b:
	        (a, b) = (b, (a % b))
	    return a
	(a, b, c) = map(int, args[0].split())
	g = gcd(a, b)
	if ((c % g) != 0):
	    ret_values.append('No')
	else:
	    a //= g
	    b //= g
	    c //= g
	    for i in range(((c // a) + 1)):
	        done = False
	        for j in range(((c // b) + 1)):
	            v = ((a * i) + (b * j))
	            if (v == c):
	                ret_values.append('Yes')
	                done = True
	                break
	            elif (v > c):
	                break
	        if done:
	            break
	    else:
	        ret_values.append('No')

	return ret_values

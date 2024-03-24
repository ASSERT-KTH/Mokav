def func(*args):
	ret_values = []
	
	
	def gcd(a, b):
	    while b:
	        (a, b) = (b, (a % b))
	    return a
	(a, b) = map(int, args[0].split())
	(c, d) = map(int, args[1].split())
	A = (d // a)
	D = (d % a)
	C = (b // c)
	B = (b % c)
	g = gcd(a, c)
	aa = (a // g)
	cc = (c // g)
	delta = (D - B)
	if ((delta % g) != 0):
	    ret_values.append((- 1))
	else:
	    delta //= g
	    for x in range((- A), (((- A) + cc) + 100)):
	        done = False
	        for y in range((- C), (((- C) + aa) + 100)):
	            if (((aa * x) - (cc * y)) == delta):
	                ret_values.append((b + ((g * aa) * (x + A))))
	                done = True
	                break
	        if done:
	            break
	    else:
	        ret_values.append((- 1))

	return ret_values

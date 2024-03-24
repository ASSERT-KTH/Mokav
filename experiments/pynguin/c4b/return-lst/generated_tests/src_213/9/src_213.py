def func(*args):
	ret_values = []
	
	
	def bmm(n, m):
	    if (min(n, m) == 0):
	        return max(n, m)
	    return bmm((max(n, m) % min(n, m)), min(n, m))
	(a, b, n) = map(int, args[0].split())
	B = 0
	while True:
	    if (B == 0):
	        n -= bmm(n, a)
	        if (n < 0):
	            B = 1
	            break
	    else:
	        n -= bmm(b, n)
	        if (n < 0):
	            B = 0
	            break
	    B += 1
	    B = (B % 2)
	ret_values.append(B)

	return ret_values

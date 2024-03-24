def func(*args):
	ret_values = []
	
	import math
	
	def f(m):
	    if (m < 8):
	        return (m, m)
	    c = math.floor((m ** (1.0 / 3)))
	    if (not (((c ** 3) <= m) and (m < ((c + 1) ** 3)))):
	        if ((((c + 1) ** 3) <= m) and (m < ((c + 2) ** 3))):
	            c = (c + 1)
	        elif ((((c - 1) ** 3) <= m) and (m < (c ** 3))):
	            c = (c - 1)
	        else:
	            assert False
	    (ans1, x1) = f((m - (c ** 3)))
	    (ans2, x2) = f((((c ** 3) - 1) - ((c - 1) ** 3)))
	    return max(((1 + ans1), (x1 + (c ** 3))), ((1 + ans2), (x2 + ((c - 1) ** 3))))
	if (__name__ == '__main__'):
	    m = int(args[0])
	    ret_values.append(*f(m))

	return ret_values

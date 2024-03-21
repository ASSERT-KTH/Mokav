def func(*args):
	ret_values = []
	
	
	def po(a, b, m):
	    if (b == 0):
	        return 1
	    if ((b % 2) == 0):
	        return ((po(a, (b // 2), m) ** 2) % m)
	    return ((po(a, (b - 1), m) * a) % m)
	
	def rev(a, m):
	    return po(a, (m - 2), m)
	
	def fact(a, m):
	    t = a
	    for i in range(1, a):
	        t = ((t * i) % m)
	    return t
	
	def main(n):
	    m = ((10 ** 9) + 7)
	    if (n == 1):
	        return 1
	    return (((2 * (fact(((2 * n) - 1), m) * rev((fact(n, m) * fact((n - 1), m)), m))) - n) % m)
	ret_values.append(main(int(args[0])))

	return ret_values

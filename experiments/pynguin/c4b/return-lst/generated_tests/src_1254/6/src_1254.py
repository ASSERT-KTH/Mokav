def func(*args):
	ret_values = []
	
	from math import factorial as fact
	
	def c(x, y):
	    return (fact(x) // (fact(y) * fact((x - y))))
	(n, m, t) = [int(i) for i in args[0].split()]
	if ((n < 4) or (m < 1)):
	    ret_values.append(0)
	    exit(0)
	res = 0
	for i in range(4, (n + 1)):
	    if (((t - i) <= m) and ((t - i) > 0)):
	        res += (c(n, i) * c(m, (t - i)))
	ret_values.append(res)

	return ret_values

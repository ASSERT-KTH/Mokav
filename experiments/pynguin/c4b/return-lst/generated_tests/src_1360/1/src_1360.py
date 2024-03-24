def func(*args):
	ret_values = []
	
	n = int(args[0])
	minimo = int((n // 7))
	maximo = int((n // 4))
	
	def fun(n):
	    for i in range(maximo, (- 1), (- 1)):
	        v = (n - (7 * i))
	        if (v >= 0):
	            x = (v % 4)
	            if (x == 0):
	                string = (('4' * int((v // 4))) + ('7' * i))
	                return string
	    return (- 1)
	ret_values.append(fun(n))

	return ret_values

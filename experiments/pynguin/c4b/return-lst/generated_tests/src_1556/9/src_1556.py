def func(*args):
	ret_values = []
	
	s = args[0]
	a = []
	a = s.split()
	for i in range(len(a)):
	    a[i] = int(a[i])
	
	def fac(x):
	    sum = 1
	    for i in range(1, (x + 1)):
	        sum *= i
	    return sum
	if (a[0] < a[1]):
	    ret_values.append(fac(a[0]))
	else:
	    ret_values.append(fac(a[1]))

	return ret_values

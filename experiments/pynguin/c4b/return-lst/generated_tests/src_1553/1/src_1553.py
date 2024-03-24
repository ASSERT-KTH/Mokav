def func(*args):
	ret_values = []
	
	a = []
	s = args[0]
	a = s.split()
	for i in range(len(a)):
	    a[i] = int(a[i])
	ma = max(a[0], a[1])
	mi = ((6 - ma) + 1)
	
	def uc(a, b):
	    while (a != b):
	        if (a > b):
	            mid = b
	            b = (a - b)
	            a = mid
	        else:
	            mid = a
	            a = (b - a)
	            b = mid
	    return a
	ret_values.append(int((mi / uc(mi, 6))), end='')
	ret_values.append('/', end='')
	ret_values.append(int((6 / uc(mi, 6))), end='')

	return ret_values

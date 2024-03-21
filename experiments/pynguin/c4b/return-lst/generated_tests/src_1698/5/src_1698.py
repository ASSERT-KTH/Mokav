def func(*args):
	ret_values = []
	
	arr = list(map(int, args[0].split()))
	arr.pop(0)
	arr.sort()
	res = 0
	for i in range(10000):
	    for k in range(500):
	        res += (i + k)
	ret_values.append(*arr)

	return ret_values

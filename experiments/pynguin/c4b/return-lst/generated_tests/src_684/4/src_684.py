def func(*args):
	ret_values = []
	
	(lis, res) = (args[0].split(), 0)
	for i in range(1001):
	    for j in range(1001):
	        boo = (((i * i) + j) == int(lis[0]))
	        boo = (boo and ((i + (j * j)) == int(lis[1])))
	        if boo:
	            res = (res + 1)
	ret_values.append(res)

	return ret_values

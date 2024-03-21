def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	(c, d) = map(int, args[1].split())
	for i in range(0, 101):
	    j = ((((a * i) + b) - d) / c)
	    if ((j == int(j)) and (j >= 0)):
	        ret_values.append(((a * i) + b))
	        break
	else:
	    ret_values.append((- 1))

	return ret_values

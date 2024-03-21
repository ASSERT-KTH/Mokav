def func(*args):
	ret_values = []
	
	(last, res) = ((- 1), 0)
	s = args[0]
	for (i, c) in enumerate(s):
	    if (c in 'AEIOUY'):
	        res = max(res, (i - last))
	        last = i
	res = max(res, (len(s) - last))
	ret_values.append(res)

	return ret_values

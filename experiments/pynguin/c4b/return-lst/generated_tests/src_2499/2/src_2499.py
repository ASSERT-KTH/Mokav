def func(*args):
	ret_values = []
	
	(n, *delta) = map(int, args[0].split())
	values = {n: 0}
	for i in range(n, 0, (- 1)):
	    if (i not in values):
	        continue
	    v = values.get(i, 0)
	    del values[i]
	    for d in delta:
	        if ((i - d) < 0):
	            continue
	        values[(i - d)] = max((v + 1), values.get((i - d), 0))
	ret_values.append(values[0])

	return ret_values

def func(*args):
	ret_values = []
	
	n = int(args[0])
	l = [list(map(int, args[1].split())) for _ in range(n)]
	x = set()
	y = set()
	for (xx, yy) in l:
	    x |= {xx}
	    y |= {yy}
	x = list(x)
	y = list(y)
	if ((len(x) == 1) or (len(y) == 1)):
	    ret_values.append((- 1))
	else:
	    ret_values.append((abs((x[0] - x[1])) * abs((y[0] - y[1]))))

	return ret_values

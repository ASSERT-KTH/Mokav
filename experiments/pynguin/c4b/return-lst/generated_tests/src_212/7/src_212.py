def func(*args):
	ret_values = []
	
	l = sorted(list(map(int, args[0].split())))
	p = l[(len(l) // 2)]
	sh = 0
	for i in l:
	    sh += abs((i - p))
	ret_values.append(sh)

	return ret_values

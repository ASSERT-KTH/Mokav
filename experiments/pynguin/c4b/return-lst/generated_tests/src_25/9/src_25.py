def func(*args):
	ret_values = []
	
	(a, b, c) = map(int, args[0].split())
	(x, y, z) = map(int, args[1].split())
	a = (a - x)
	b = (b - y)
	c = (c - z)
	have = 0
	need = 0
	for i in (a, b, c):
	    if (i > 0):
	        have += (i // 2)
	    elif (i < 0):
	        need += i
	if (have >= abs(need)):
	    ret_values.append('Yes')
	else:
	    ret_values.append('No')

	return ret_values

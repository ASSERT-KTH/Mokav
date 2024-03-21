def func(*args):
	ret_values = []
	
	inp = args[0].split()
	s = eval(inp[1])
	x = (eval(inp[2]) - eval(inp[0]))
	if ((((x % s) == 0) or ((((x - 1) % s) == 0) and ((x - 1) != 0))) and (x >= 0)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values

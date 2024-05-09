def original_func(*args):
	global_list = []
	
	inp = args[0].split()
	s = eval(inp[1])
	x = (eval(inp[2]) - eval(inp[0]))
	if (((x % s) == 0) or ((((x - 1) % s) == 0) and ((x - 1) != 0))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list
def patched_func(*args):
	global_list = []
	
	(x1, y1, x2, y2) = map(int, args[0].split())
	a = abs((x1 - x2))
	b = abs((y1 - y2))
	(x, y) = map(int, args[1].split())
	if (((a % x) != 0) or ((b % y) != 0)):
	    global_list.append('NO')
	else:
	    par1 = (a / x)
	    par2 = (b / y)
	    par1 = (par1 % 2)
	    par2 = (par2 % 2)
	    if (par1 != par2):
	        global_list.append('NO')
	    else:
	        global_list.append('YES')
	return global_list
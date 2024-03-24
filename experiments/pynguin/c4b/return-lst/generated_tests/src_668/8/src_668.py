def func(*args):
	ret_values = []
	
	(x1, y1, x2, y2) = map(int, args[0].split())
	a = abs((x1 - x2))
	b = abs((y1 - y2))
	(x, y) = map(int, args[1].split())
	if (((a % x) != 0) or ((b % y) != 0)):
	    ret_values.append('NO')
	else:
	    par1 = (a / x)
	    par2 = (b / y)
	    par1 = (par1 % 2)
	    par2 = (par2 % 2)
	    if (par1 != par2):
	        ret_values.append('NO')
	    else:
	        ret_values.append('YES')

	return ret_values

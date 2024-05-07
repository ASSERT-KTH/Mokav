def patched_func(*args):
	global_list = []
	
	(x, y) = map(int, args[0].split())
	while True:
	    a = min(2, x)
	    x -= a
	    b = min((22 - (10 * a)), y)
	    y -= b
	    if (((10 * a) + b) < 22):
	        global_list.append('Hanako')
	        break
	    a = min(2, x)
	    x -= a
	    b = min((22 - (10 * a)), y)
	    y -= b
	    if (((10 * a) + b) < 22):
	        global_list.append('Ciel')
	        break
	    while ((a > 0) and (y >= 10)):
	        a -= 1
	        x += 1
	        y -= 10
	return global_list
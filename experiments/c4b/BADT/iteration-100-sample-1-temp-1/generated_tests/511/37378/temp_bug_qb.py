def original_func(*args):
	global_list = []
	
	
	def gank(a, b, c):
	    d = (b - a)
	    if (d == 0):
	        return True
	    elif (c == 0):
	        return False
	    elif (((d < 0) and (c > 0)) or ((c < 0) and (d > 0))):
	        return False
	    elif (c < 0):
	        d *= (- 1)
	        c *= (- 1)
	    elif ((d % c) == 0):
	        return True
	    else:
	        return False
	(a, b, c) = map(int, args[0].split(' '))
	if gank(a, b, c):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list
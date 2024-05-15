def patched_func(*args):
	global_list = []
	
	(a, b, c) = [int(i) for i in args[0].split()]
	if (c == 0):
	    if (a == b):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	elif (c > 0):
	    if (((b % c) == (a % c)) and (b >= a)):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	elif ((a >= b) and ((b % (- c)) == (a % (- c)))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list
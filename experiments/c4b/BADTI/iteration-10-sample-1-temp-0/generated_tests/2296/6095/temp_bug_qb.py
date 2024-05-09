def original_func(*args):
	global_list = []
	
	(m, n) = map(int, args[0].split(' '))
	if ((n == 1) or (m == 1)):
	    if (n == 1):
	        global_list.append((m // 2))
	    elif (m == 1):
	        global_list.append((n // 2))
	elif (((m % 2) != 0) and ((n % 2) != 0)):
	    if (m > n):
	        e = m
	        r = n
	    else:
	        e = n
	        r = m
	    u = (e - 1)
	    b = ((u * r) // 2)
	    v = (e // 2)
	    global_list.append((b + v))
	else:
	    fuck = ((m * n) // 2)
	    global_list.append(fuck)
	return global_list
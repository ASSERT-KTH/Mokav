def original_func(*args):
	global_list = []
	
	(a, b) = [int(i) for i in args[0].split()]
	ans = 1
	if ((a <= 2) and (b <= 2)):
	    global_list.append(0)
	else:
	    while ((b > 2) or (a > 2)):
	        while (b > 2):
	            ans += 1
	            a += 1
	            b -= 2
	        while (a > 2):
	            ans += 1
	            b += 1
	            a -= 2
	    global_list.append(ans)
	return global_list
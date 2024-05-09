def original_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n == 2):
	    global_list.append(3)
	else:
	    ans = ((n // 2) + 1)
	    n %= 4
	    if (n and (not (ans & 1))):
	        ans += 1
	    if ((n > 1) and (ans <= 3)):
	        ans += 2
	    global_list.append(ans)
	return global_list
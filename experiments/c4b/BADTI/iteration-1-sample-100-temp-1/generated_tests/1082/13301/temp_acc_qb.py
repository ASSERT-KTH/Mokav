def patched_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	res = k
	cnt = 0
	while (res < l):
	    res *= k
	    cnt += 1
	if (res == l):
	    global_list.append('YES')
	    global_list.append(cnt)
	else:
	    global_list.append('NO')
	return global_list
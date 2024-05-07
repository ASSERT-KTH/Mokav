def original_func(*args):
	global_list = []
	
	(n, m, z) = map(int, args[0].split(' '))
	i = (n * m)
	if ((n > z) or (m == 0)):
	    ans = 0
	else:
	    ans = 1
	    while ((i < z) and (abs((z - i)) >= (n * m))):
	        i += (n * m)
	        ans += 1
	global_list.append(ans)
	return global_list
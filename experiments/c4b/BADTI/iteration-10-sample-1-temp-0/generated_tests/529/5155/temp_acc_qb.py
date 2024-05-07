def patched_func(*args):
	global_list = []
	
	(a, b, n, x) = map(int, args[0].split())
	e = ((10 ** 9) + 7)
	if (a == 1):
	    ans = ((x + (b * n)) % e)
	else:
	    ans = (((pow(a, n, e) * x) + ((b * (pow(a, n, e) - 1)) * pow((a - 1), (e - 2), e))) % e)
	global_list.append(int(ans))
	return global_list
def original_func(*args):
	global_list = []
	
	cont = 0
	(n, a, b) = map(int, args[0].split())
	for i in range(n):
	    if (((i - 1) <= b) and ((n - i) >= a)):
	        cont += 1
	global_list.append((cont - 1))
	return global_list
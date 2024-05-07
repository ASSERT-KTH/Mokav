def original_func(*args):
	global_list = []
	
	al = 'abcdefghijklmnopqrstuvwxyz'
	(size, distinct) = map(int, args[0].split())
	same = ((size - distinct) + 1)
	ans = ''
	for i in range(same):
	    ans += al[0]
	size -= same
	for i in range(1, (size + 1)):
	    ans += al[i]
	global_list.append(ans)
	return global_list
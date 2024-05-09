def patched_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	chars_dis = (((n // k) + 1) * [chr((i + 97)) for i in range(k)])
	global_list.append(''.join(chars_dis[:n]))
	return global_list
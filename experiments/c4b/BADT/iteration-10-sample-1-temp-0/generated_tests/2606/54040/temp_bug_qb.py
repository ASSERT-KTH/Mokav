def original_func(*args):
	global_list = []
	
	import random
	(n, k) = map(int, args[0].split())
	chars_dis = (((n // k) + 1) * [chr(random.randint(97, 122)) for _ in range(k)])
	global_list.append(''.join(chars_dis[:n]))
	return global_list
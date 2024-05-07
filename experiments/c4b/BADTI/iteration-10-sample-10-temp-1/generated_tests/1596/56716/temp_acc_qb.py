def patched_func(*args):
	global_list = []
	
	i = args[0]
	let = max(i)
	global_list.append((let * i.count(let)))
	return global_list
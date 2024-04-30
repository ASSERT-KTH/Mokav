def patched_func(*args):
	global_list = []
	
	
	def get_int():
	    return map(int, args[0].split())
	(t, s, x) = get_int()
	global_list.append(['NO', 'YES'][(((((x - t) / s) == ((x - t) // s)) or (((((x - t) - 1) // s) > 0) and ((((x - t) - 1) / s) == (((x - t) - 1) // s)))) and (x >= t))])
	return global_list
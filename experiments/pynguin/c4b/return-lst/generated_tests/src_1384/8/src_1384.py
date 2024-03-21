def func(*args):
	ret_values = []
	
	
	def get_int():
	    return map(int, args[0].split())
	(t, s, x) = get_int()
	ret_values.append(['NO', 'YES'][(((((x - t) / s) == ((x - t) // s)) or (((((x - t) - 1) // s) > 0) and ((((x - t) - 1) / s) == (((x - t) - 1) // s)))) and (x >= t))])

	return ret_values

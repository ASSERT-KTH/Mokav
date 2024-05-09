def original_func(*args):
	global_list = []
	
	x = [int(n) for n in args[0].split()]
	total_drinks = (x[1] * x[2])
	total_limes = (x[3] * x[4])
	salt = x[5]
	drinks_per_shot = (x[6] * x[0])
	salt_per_shot = (x[7] * x[0])
	global_list.append(min([(total_drinks // drinks_per_shot), total_limes, (salt // salt_per_shot)]))
	return global_list
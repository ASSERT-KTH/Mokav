def original_func(*args):
	global_list = []
	
	shoes = [int(x) for x in args[0].split()]
	count = 0
	for shoe in shoes:
	    if (shoes.count(shoe) > 1):
	        count += 1
	global_list.append([0, (count - 1)][(count != 0)])
	return global_list
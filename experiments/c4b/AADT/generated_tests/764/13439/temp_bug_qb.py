def original_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	gem = (((a + b) + c) // 3)
	afstand = ((abs((gem - a)) + abs((gem - b))) + abs((gem - c)))
	global_list.append(afstand)
	return global_list
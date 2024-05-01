def original_func(*args):
	global_list = []
	
	string = args[0]
	string = string.lower()
	list1 = list(string)
	list2 = ['a', 'e', 'i', 'o', 'u']
	res = list(filter((lambda x: (x not in list2)), list1))
	string2 = '.'.join(res)
	global_list.append(('.' + string2))
	return global_list
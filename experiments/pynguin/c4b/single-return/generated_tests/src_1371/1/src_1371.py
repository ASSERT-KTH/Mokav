def func(*args):
	
	string = args[0]
	string = string.lower()
	list1 = list(string)
	list2 = ['a', 'e', 'i', 'o', 'u', 'y']
	res = list(filter((lambda x: (x not in list2)), list1))
	string2 = '.'.join(res)
	return(('.' + string2))

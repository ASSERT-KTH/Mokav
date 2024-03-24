def func(*args):
	ret_values = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	d = int(args[3])
	e = int(args[4])
	list1 = []
	i = 1
	while (i <= e):
	    if (((i % a) == 0) or ((i % b) == 0) or ((i % c) == 0) or ((i % d) == 0)):
	        list1.append(i)
	    i += 1
	ret_values.append(len(list1))

	return ret_values

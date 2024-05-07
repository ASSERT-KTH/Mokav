def original_func(*args):
	global_list = []
	
	'th, hu, do, un = map(str, input())\nyear = int(th + hu + do + un)'
	year = int(args[0])
	for i in range((year + 1), 9000):
	    i = str(i)
	    if ((i[0] != i[1]) and (i[2] != i[3]) and (i[1] != i[3]) and (i[0] != i[2]) and (i[1] != i[2]) and (i[0] != i[3])):
	        global_list.append(i)
	        break
	return global_list
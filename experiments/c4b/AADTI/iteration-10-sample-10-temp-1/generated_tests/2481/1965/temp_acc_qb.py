def patched_func(*args):
	global_list = []
	
	import math
	nStr = args[0]
	n = int(nStr)
	nameList = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	i = 1
	while (n > (5 * i)):
	    n = (n - (5 * i))
	    i = (i * 2)
	j = 0
	while (n > i):
	    n = (n - i)
	    j = (j + 1)
	global_list.append(nameList[j])
	return global_list
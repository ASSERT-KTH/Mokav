def original_func(*args):
	global_list = []
	
	from math import *
	names = ['sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	p = 1
	n = int(args[0])
	sum = 0
	i = 1
	while (sum < n):
	    sum += (i * 5)
	    i *= 2
	    if (sum > n):
	        i //= 2
	        sum -= (i * 5)
	        break
	diff = (n - sum)
	index = (diff // i)
	if (n <= 5):
	    global_list.append(names[(index - 1)])
	else:
	    global_list.append(names[index])
	return global_list
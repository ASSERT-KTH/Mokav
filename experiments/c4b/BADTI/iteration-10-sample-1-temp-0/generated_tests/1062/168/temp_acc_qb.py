def patched_func(*args):
	global_list = []
	
	a = args[0]
	num = (a.count('4') + a.count('7'))
	num = str(num)
	if (len(num) == (num.count('4') + num.count('7'))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list
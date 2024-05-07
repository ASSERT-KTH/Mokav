def patched_func(*args):
	global_list = []
	
	num = args[0]
	fours = num.count('4')
	sevens = num.count('7')
	summ = (fours + sevens)
	if ((summ == 4) or (summ == 7)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list